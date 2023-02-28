import pytest, itertools, pathlib
import pandas as pd
import networkx as nx
from pathlib import Path
from bokeh.plotting import figure
from ..src.wonderD149Data.data import helper as hp
from ..src.wonderD149Data.wonderD149Data import WonderD149Data

@pytest.fixture(scope='session')
def birth_data():
   '''run once per session. All test methods and functions share one setup and teardown'''
   return hp.getBirthAnalysisData()

@pytest.fixture(scope='session')
def graph_data(birth_data):
    '''run once per session. All test methods and functions share one setup and teardown'''
    corr_matrix = birth_data.corr()

    # Find features with correlation greater than 0.995
    to_investigate = [(row,column) for row,column in itertools.product(corr_matrix.index,corr_matrix.columns) if corr_matrix[column][row] < -0.75 and hp.is_Different_Category(row,column)]
    # print(len(to_investigate),'combinations')
    return hp.createCorrelationGraph(corr_matrix,to_investigate)

@pytest.fixture(scope='session')
def plot_data(graph_data):
    return hp.plotNetworkGraph(graph_data,'Test',Path(str(pathlib.Path(__file__).parent.absolute())+'/test_outputs'))

@pytest.fixture(scope='session')
def col_data():
    columns = hp.getColumns()
    measure_selection = {
    'M_002': 'D149.M002', # Births
    }
    observation_selection = {}
    variable_filter = {}
    code = list(columns.keys())[0]
    dataObj = WonderD149Data([code],measure_selection,observation_selection,variable_filter)
    data_col = dataObj.getData()
    col_data = pd.Series(data_col['Births'])
    col_data.name = columns[code]
    return col_data

def test_getGroupByCategories():
    '''
        Test if Group by category is working as expected
    '''
    categories = hp.getGroupByCategories()
    assert(isinstance(categories,set))
    assert('Maternal morbidity' in categories)
    assert(' Maternal morbidity ' not in categories)

def test_getCodeDetailsForGivenCategory():
    '''
        Test if get code details for given category is working
    '''
    result = hp.getCodeDetailsForGivenCategory('Maternal morbidity')
    with pytest.raises(AssertionError):
        hp.getCodeDetailsForGivenCategory('jfbajf')
    assert(isinstance(result,dict))
    assert('D149.V102' in result)
    assert result['D149.V102'] == 'Maternal Transfusion'

def test_getFilterValuesForGivenCode():
    '''
        Test to get filter values for given code
    '''
    result = hp.getFilterValuesForGivenCode('D149.V102')
    with pytest.raises(AssertionError):
        hp.getFilterValuesForGivenCode('D149mbbm2')
    assert(isinstance(result,dict))
    assert '1' in result
    assert result['9']=='Unknown or Not Stated'

def test_getMeasureCodesAndDescription():
    '''
        Test to measure code and description
    '''
    result = hp.getMeasureCodesAndDescription()
    assert isinstance(result,dict)
    assert 'M_071' in result
    assert 'D149.M080' in result['M_080']
    assert result['M_090']['D149.M091'] == 'Average LMP Gestational Age (weeks)'

def test_getParameterObject():
    '''
        Test parameter object
    '''
    results = [hp.getParameterObject(x) for x in ['B','F','I','M','O','V','MISC']]
    for result in results:
        assert(isinstance(result,dict))

def test_sortParameters():
    '''
        Test sort parameters
    '''
    result = hp.sort_parameters({'he':1,'ab':3})
    assert isinstance(result,dict)
    assert list(result.keys())[0]=='ab'

def test_createParameterList():
    '''
        Test create parameter list
    '''
    result = hp.createParameterList({'he':1,'ab':[3,2,1]})
    assert isinstance(result,str)

def test_getColumns():
    '''
        Test get columns
    '''
    result = hp.getColumns()
    assert isinstance(result,dict)

def test_is_Different_Category():
    '''
        Test if 2 columns belong to same category
    '''
    with pytest.raises(AssertionError):
        hp.is_Different_Category('D149mbbm2','jhgjhf')
    
    assert hp.is_Different_Category('Maternal Transfusion','OE Gestational Age Recode 11')

def test_getBirthAnalysisData(birth_data):
    '''
        Test to get Birth analysis data
    '''
    assert isinstance(birth_data,pd.DataFrame)

def test_createCorrelationGraph(graph_data):
    '''
        Test to get Correlation Graph
    '''
    assert isinstance(graph_data,nx.Graph)

def test_interpolateSeries(col_data):
    '''
        Test of interpolateSeries
    '''
    result = hp.interpolateSeries(col_data,10)
    assert isinstance(col_data,pd.Series)
    assert isinstance(result,pd.Series)
    assert len(result) == 10

def test_plotNetworkGraph(plot_data):
    '''
        Test plot
    '''
    assert isinstance(plot_data,figure)