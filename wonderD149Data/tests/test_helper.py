import pytest, itertools, pathlib
import pandas as pd
import networkx as nx
from pathlib import Path
from bokeh.plotting import figure
import plotly_express as px
from plotly.graph_objects import Figure
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

@pytest.fixture(scope='session')
def induction_of_labour_data():
    group_by_list = [
        'D149.V71', # Mother's Pre-pregnancy BMI
        'D149.V91', #Induction of Labor
    ]
    measure_selection = {
        'M_002': 'D149.M002', # Births
    }
    observation_selection = {}
    variable_filter = {
        'V_D149.V91': ['1','2'], # filtering only yes and no
        'V_D149.V71': ['1','2','3','4','5','6'], # filtering only required BMI
    }
    dataObj = WonderD149Data(group_by_list,measure_selection,observation_selection,variable_filter)
    induction_of_labour = dataObj.getData()
    data = hp.get_percent_data(induction_of_labour,'Induction of Labor',"Mother's Pre-pregnancy BMI")
    return data

@pytest.fixture(scope='session')
def preterm_birth_cigar_yes_data():
    group_by_list = [
    'D149.V144', # Number of Cigarettes 1st Trimester Recode
    ]
    measure_selection = {
        'M_002': 'D149.M002', # Births
    }
    observation_selection = {
        'O_oe_gestation':'D149.V33'
    }
    variable_filter = {
        'V_D149.V33': ['01','02','03','04','05'], # filtering only yes and no
        'V_D149.V144': ['0','1','2','3','4'], # filtering only cigar values
    }
    dataObj = WonderD149Data(group_by_list,measure_selection,observation_selection,variable_filter)
    data_col = dataObj.getData()
    return data_col

@pytest.fixture(scope='session')
def preterm_birth_cigar_no_data():
    group_by_list = [
    'D149.V144', # Number of Cigarettes 1st Trimester Recode
    ]
    measure_selection = {
        'M_002': 'D149.M002', # Births
    }
    observation_selection = {
        'O_oe_gestation':'D149.V33'
    }
    variable_filter = {
        'V_D149.V33': ['06','07','08','09','10'], # filtering only yes and no
        'V_D149.V144': ['0','1','2','3','4'], # filtering only required cigar values
    }
    dataObj = WonderD149Data(group_by_list,measure_selection,observation_selection,variable_filter)
    data_col = dataObj.getData()
    return data_col

@pytest.fixture(scope='session')
def abnormalities_cigar_yes_data():
    group_by_list = [
    'D149.V144', # Number of Cigarettes 1st Trimester Recode
    ]
    measure_selection = {
        'M_002': 'D149.M002', # Births
    }
    observation_selection = {
    }
    variable_filter = {
        'V_D149.V122': ['0'], # filtering only yes and no
        'V_D149.V144': ['0','1','2','3','4'], # filtering only required cigar values
    }
    dataObj = WonderD149Data(group_by_list,measure_selection,observation_selection,variable_filter)
    data_col = dataObj.getData()
    return data_col

@pytest.fixture(scope='session')
def abnormalities_cigar_no_data():
    group_by_list = [
    'D149.V144', # Number of Cigarettes 1st Trimester Recode
    ]
    measure_selection = {
        'M_002': 'D149.M002', # Births
    }
    observation_selection = {
    }
    variable_filter = {
        'V_D149.V122': ['1','9'], # filtering only yes and no
        'V_D149.V144': ['0','1','2','3','4'], # filtering only required cigar values
    }
    dataObj = WonderD149Data(group_by_list,measure_selection,observation_selection,variable_filter)
    data_col = dataObj.getData()
    return data_col

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

def test_get_percent_data(induction_of_labour_data):
    '''
        Test percent data
    '''
    assert isinstance(induction_of_labour_data,pd.DataFrame)

def test_merge_dataframe_on_yes_and_no(preterm_birth_cigar_yes_data,preterm_birth_cigar_no_data):
    '''
        Test the working of yes and no
    '''
    preterm_birth_cigar = hp.merge_dataframe_on_yes_and_no(preterm_birth_cigar_yes_data,preterm_birth_cigar_no_data,'Number of Cigarettes 1st Trimester Recode','Pre Term Birth')
    assert isinstance(preterm_birth_cigar,pd.DataFrame)

def test_plot_line(preterm_birth_cigar_yes_data,preterm_birth_cigar_no_data,abnormalities_cigar_yes_data,abnormalities_cigar_no_data):
    '''
        Test plot line
    '''
    preterm_birth_cigar = hp.merge_dataframe_on_yes_and_no(preterm_birth_cigar_yes_data,preterm_birth_cigar_no_data,'Number of Cigarettes 1st Trimester Recode','Pre Term Birth')
    abnormalities_cigar = hp.merge_dataframe_on_yes_and_no(abnormalities_cigar_yes_data,abnormalities_cigar_no_data,'Number of Cigarettes 1st Trimester Recode','Abnormality')
    final_df_cigar = pd.concat([preterm_birth_cigar,abnormalities_cigar]).reset_index()[["Number of Cigarettes 1st Trimester Recode","Percent of Mother Facing Issue","Issue"]]
    fig = hp.plot_line(final_df_cigar,"Number of Cigarettes 1st Trimester Recode",'Effect of Cigarettes on Pregnancy')
    assert isinstance(fig,Figure)


def test_plot_histogram(preterm_birth_cigar_yes_data,preterm_birth_cigar_no_data,abnormalities_cigar_yes_data,abnormalities_cigar_no_data):
    '''
        Test plot line
    '''
    preterm_birth_cigar = hp.merge_dataframe_on_yes_and_no(preterm_birth_cigar_yes_data,preterm_birth_cigar_no_data,'Number of Cigarettes 1st Trimester Recode','Pre Term Birth')
    abnormalities_cigar = hp.merge_dataframe_on_yes_and_no(abnormalities_cigar_yes_data,abnormalities_cigar_no_data,'Number of Cigarettes 1st Trimester Recode','Abnormality')
    final_df_cigar = pd.concat([preterm_birth_cigar,abnormalities_cigar]).reset_index()[["Number of Cigarettes 1st Trimester Recode","Percent of Mother Facing Issue","Issue"]]
    fig = hp.plot_histogram(final_df_cigar,"Number of Cigarettes 1st Trimester Recode",'Effect of Cigarettes on Pregnancy')
    assert isinstance(fig,Figure)