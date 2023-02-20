from  .data import helper as hp
from . import data as dt
import requests
# BeautifulSoup library facilitates parsing of XML response
import bs4 as bs
# This library faciliates 2-dimensional array operations and visualization
import pandas as pd

class WonderD149Data:
    '''
    A class which instantiates an object of requested Data based on query
    '''

    def __init__(self,group_by_list=[],measure_selection={},observation_selection={},variable_filter={}):
        '''
        Constructs an object with all the required query selections
        '''
        self.b_parameters = hp.getParameterObject('B',group_by_list)
        self.f_parameters = hp.getParameterObject('F')
        self.i_parameters = hp.getParameterObject('I')
        self.m_parameters = hp.getParameterObject('M',measure_selection)
        self.o_parameters = hp.getParameterObject('O',self.b_parameters,observation_selection)
        self.v_parameters = hp.getParameterObject('V',variable_filter)
        self.misc_parameters = hp.getParameterObject('MISC')
        self._createXMLRequest()
        self.url = "https://wonder.cdc.gov/controller/datarequest/D149"
    

    def _createXMLRequest(self):
        '''
        A method to create XML request for sending to wonder API
        '''
        xml_request = "<request-parameters>\n"
        xml_request += hp.createParameterList(hp.sort_parameters(self.b_parameters))
        xml_request += hp.createParameterList(hp.sort_parameters(self.f_parameters))
        xml_request += hp.createParameterList(hp.sort_parameters(self.i_parameters))
        xml_request += hp.createParameterList(hp.sort_parameters(self.m_parameters))
        xml_request += hp.createParameterList(hp.sort_parameters(self.o_parameters))
        xml_request += hp.createParameterList(hp.sort_parameters(self.v_parameters))
        xml_request += hp.createParameterList(hp.sort_parameters(self.misc_parameters))
        xml_request += "</request-parameters>"
        self.xml_request = xml_request
    
    def getData(self):
        '''A method which returns data from Wonder API'''
        self.response = requests.post(self.url, data={"request_xml": self.xml_request, "accept_datause_restrictions": "true"})

        if self.response.status_code == 200:
            self.xml_response = self.response.text
            data_frame = self._xml2df(self.xml_response)
            measure_columns = [ dt.M_ATTR[u][v] for u,v in self.m_parameters.items()]
            group_by_columns = [  dt.B_ATTR[x]['name'] for x in self.b_parameters.values() if x != '*None*']
            data_columns = group_by_columns + measure_columns
            return pd.DataFrame(data=data_frame, columns=data_columns)

        else:
            print("something went wrong")
            print(f'Error code: {self.response.status_code}')
            print(f'Reason: {self.response.reason}')
            raise Exception(self.response.content)
    
    def _xml2df(self,xml_data):
        """ This function grabs the root of the XML document and iterates over
            the 'r' (row) and 'c' (column) tags of the data-table
            Rows with a 'v' attribute contain a numerical value
            Rows with a 'l attribute contain a text label and may contain an
            additional 'r' (rowspan) tag which identifies how many rows the value
            should be added. If present, that label will be added to the following
            rows of the data table.
        
            Function returns a two-dimensional array or data frame that may be 
            used by the pandas library."""
        
        root = bs.BeautifulSoup(xml_data,"xml")
        all_records = []
        row_number = 0
        rows = root.find_all("r")
        # print(rows)
        
        for row in rows:
            if row_number >= len(all_records):
                all_records.append([])
                
            for cell in row.find_all("c"):
                if 'v' in cell.attrs:
                    try:
                        all_records[row_number].append(float(cell.attrs["v"].replace(',','')))
                    except ValueError:
                        all_records[row_number].append(cell.attrs["v"])
                else:
                    if 'r' not in cell.attrs:
                        try:
                            # print(all_records,row_number)
                            all_records[row_number].append(cell.attrs["l"])
                        except KeyError:
                            del all_records[-1]
                            row_number-=1
                            break

                    else:
                    
                        for row_index in range(int(cell.attrs["r"])):
                            if (row_number + row_index) >= len(all_records):
                                all_records.append([])
                                all_records[row_number + row_index].append(cell.attrs["l"])
                            else:
                                all_records[row_number + row_index].append(cell.attrs["l"])
                                            
            row_number += 1
        return all_records