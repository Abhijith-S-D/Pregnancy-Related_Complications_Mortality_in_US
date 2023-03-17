import collections, math, pathlib, json, itertools, os
import pandas as pd
import networkx as nx
from bokeh.io import save
from bokeh.models import Range1d, Circle, NodesAndLinkedEdges, MultiLine,EdgesAndLinkedNodes
from bokeh.plotting import figure, from_networkx
from bokeh.palettes import Spectral4
import plotly_express as px
from ..data import B_ATTR as _B_ATTR, V_ATTR as _V_ATTR, M_ATTR as _M_ATTR, F_ATTR as _F_ATTR, O_ATTR as _O_ATTR, MISC_ATTR as _MISC_ATTR, log as logger
from ..wonderD149Data import WonderD149Data

def getGroupByCategories():
    '''
        A helper method that returns all the possible broad categories of columns of the database

        Returns:
        A set of different categories
    '''
    return { x['category'] for x in _B_ATTR.values()}

def getCodeDetailsForGivenCategory(category):
    '''
        A helper function that gives info about all the table key codes for a particular category.

        Attributes
        ------------

        category : str
        The allowed set of categories

        Returns a dictionary of variable codes and descriptions
    '''
    try:
        assert isinstance(category,str),f'the parameter of method should be a string but {type(category)} given'
        assert category in getGroupByCategories(),f'the provided category invalid. It must be among {getGroupByCategories()}'
    except AssertionError as er:
        logger.error(str(er))
        raise er

    return { x:_B_ATTR[x]['name'] for x in _B_ATTR if _B_ATTR[x]['category']==category}

def getFilterValuesForGivenCode(code):
    '''
        A helper function that gives info about all the filter values for a given column code.

        Attributes
        ------------

        code : str
        The allowed set of codes

        Returns a list of values possible for the given code
    '''
    try:
        assert isinstance(code,str),f'the parameter of method should be a string but {type(code)} given'
        assert code in _B_ATTR.keys(),f'the provided code is invalid. It must be among {_B_ATTR.keys()}'
    except AssertionError as er:
        logger.error(str(er))
        raise er
    return _V_ATTR[f'V_{code}']

def getMeasureCodesAndDescription():
    '''
        A helper method that returns all the possible measures to be retrived from the database

        Returns:
        A dict of possible M codes with corresponding values and column names
    '''
    return _M_ATTR

def getParameterObject(param_type,parameter_selections={},o_params = {}):
    '''
        A helper function that creates the parameter object given its type info and some specified selections

        Attributes
        ------------

        param_type : str
        The allowed set of parametes include 'B','F','I','M','O','V','MISC'

        parameter_selections: dict
        The initial selection of params

        Returns a parameter object
    '''
    try:
        assert isinstance(param_type,str) , f'the parameter of method should be a string but {type(param_type)} given'
        param_type = param_type.upper()
        assert param_type in ['B','F','I','M','O','V','MISC'] , f"the parameter of method should be one among {['B','F','I','M','O','V','MISC']} but {param_type} given"
    except AssertionError as er:
        logger.error(str(er))
        raise er

    if param_type == 'B':
        if parameter_selections == {}:
            parameter_selections = []
        try:
            assert isinstance(parameter_selections,list), f"the parameter selections of B must be a list of B codes"
            assert len(parameter_selections)<6, f"A max of 5 codes can be selected in order for group by operation"
            assert set(parameter_selections) <= set(_B_ATTR.keys()), f"The list of selections can be only from among the B codes"
        except AssertionError as er:
            logger.error(str(er))
            raise er
        b_parameters = {
            "B_1": "D149.V20", # default selection is year
            "B_2": "*None*",
            "B_3": "*None*",
            "B_4": "*None*",
            "B_5": "*None*"
        }
        b_keys = list(b_parameters.keys())
        for i in range(len(parameter_selections)):
            b_parameters[b_keys[i]]=parameter_selections[i]
        return b_parameters
    elif param_type == 'M':
        try:
            assert isinstance(parameter_selections,dict), f"the parameter selections of M must be a dict of M codes"
            assert all([ x in list(_M_ATTR.keys()) and list(_M_ATTR[x].keys())[0] == parameter_selections[x] for x in parameter_selections]), f"The dict must follow M_ATTR data"
        except AssertionError as er:
            logger.error(str(er))
            raise er
        m_parameters = {
            "M_002": "D149.M002",   # Births, must be included
        }
        for m_key in parameter_selections:
            m_parameters[m_key] = parameter_selections[m_key]
        return m_parameters
    elif param_type == 'F':
        try:
            assert parameter_selections == {}, f"cant select for F type"
        except AssertionError as er:
            logger.error(str(er))
            raise er
        f_parameters = {k:[list(v.keys())[0]] for (k,v) in _F_ATTR.items()}
        return f_parameters
    elif param_type == 'I':
        try:
            assert parameter_selections == {}, f"cant select for I type"
        except AssertionError as er:
            logger.error(str(er))
            raise er
        i_parameters = {f'I{k[1:]}':[list(v.values())[0]] for (k,v) in _F_ATTR.items()}
        return i_parameters
    elif param_type == 'O':
        try:
            assert isinstance(parameter_selections,dict), f"the parameter selections of O must be a dict of B codes"
            assert isinstance(o_params,dict), f"the o params selections of O must be a dict of O codes"
            assert len(parameter_selections.keys())<6, f"A max of 5 codes can be selected in order for group by operation"
            assert set([ x for x in parameter_selections.values() if x != '*None*']) <= set(_B_ATTR.keys()), f"The list of selections can be only from among the B codes"
            assert set(o_params.keys()) <= set(_O_ATTR.keys()), f"The list of selections can be only from among the O codes"
            assert all([ o_params[x] in _O_ATTR[x] for x in o_params]), f"The list of selections can be only from among the O codes"
        except AssertionError as er:
            logger.error(str(er))
            raise er
        o_parameters = {}
        for (k,v) in _O_ATTR.items():
            for key in v:
                if key in parameter_selections.values():
                    o_parameters[k] = key
                    break
            if k not in o_parameters:
                o_parameters[k] = list(v.keys())[0]

        o_parameters['O_precision'] = '2'
        o_parameters['O_timeout'] = '600'
        o_parameters['O_show_suppressed'] = 'false'
        o_parameters['O_show_zeros'] = 'false'
        for o_key in o_params:
            o_parameters[o_key] = o_params[o_key]
        return o_parameters
    elif param_type == 'MISC':
        try:
            assert parameter_selections == {}, f"cant select for MISC type"
        except AssertionError as er:
            logger.error(str(er))
            raise er
        return _MISC_ATTR
    else:
        try:
            assert isinstance(parameter_selections,dict), f"The parameter selection can be only dict but {type(parameter_selections)}observed"
            assert set(parameter_selections.keys()) <= set(_V_ATTR.keys()), f"The V codes must be valid"
            assert all(isinstance(x[1],list) and set(x[1]) <= set(_V_ATTR[x[0]].keys()) for x in parameter_selections.items())
        except AssertionError as er:
            logger.error(str(er))
            raise er
        v_parameters = {k:[list(v.keys())[0]] for (k,v) in _V_ATTR.items()}
        for v_key in parameter_selections:
            v_parameters[v_key] = parameter_selections[v_key]
        return v_parameters
    
def sort_parameters(parameters):
    '''
    A helper method to sort dict based on keys
    '''
    try:
        assert isinstance(parameters,dict),f"parameters must be dict"
    except AssertionError as er:
        logger.error(str(er))
        raise er
    return collections.OrderedDict(sorted(parameters.items()))

def createParameterList(parameterList):
    """Helper function to create a parameter list from a dictionary object"""
    try:
        assert isinstance(parameterList,dict),f"parameters must be dict"
    except AssertionError as er:
        logger.error(str(er))
        raise er

    parameterString = ""
    
    for key in parameterList:
        parameterString += "<parameter>\n"
        parameterString += "<name>" + key + "</name>\n"
        
        if isinstance(parameterList[key], list):
            for value in parameterList[key]:
                parameterString += "<value>" + str(value) + "</value>\n"
        else:
            parameterString += "<value>" + str(parameterList[key]) + "</value>\n"
        
        parameterString += "</parameter>\n"
        
    return parameterString

def interpolateSeries(col,MAX_COL_LEN):
    '''
    A helper method to interpolate a given pandas series object to MAX_COL_LEN size
    '''
    try:
        assert(isinstance(col,pd.Series))
        assert(isinstance(MAX_COL_LEN,int))
        assert(MAX_COL_LEN>0)
    except AssertionError as er:
        logger.error(str(er))
        raise er
    curr_col_len = len(col)
    new_index = list(range(0,MAX_COL_LEN,math.floor(MAX_COL_LEN/curr_col_len)))[:curr_col_len]
    col.index = new_index
    return col.reindex(range(MAX_COL_LEN),method='ffill')
  
def is_Different_Category(col_name1,col_name2):
    '''
    A helper method to verify if col_name1 and col_name2 belong to different category
    '''
    try:
        assert(isinstance(col_name1,str))
        assert(isinstance(col_name2,str))
    except AssertionError as er:
        logger.error(str(er))
        raise er
    cat1=''
    cat2=''
    categories = getGroupByCategories()
    for category in categories:
        colnames = getCodeDetailsForGivenCategory(category).values()
        if col_name1 in colnames:
            cat1 = category
        if col_name2 in colnames:
            cat2 = category
    try:
        assert cat1 != '','category 1 is invalid'
        assert cat2 != '','category 2 is invalid'
    except AssertionError as er:
        logger.error(str(er))
        raise er
    return cat1 != cat2

def getColumns():
    '''
        A helper method that returns all the possible columns of the database

        Returns:
        A dictionary of different columns with code
    '''
    list_of_codes = [getCodeDetailsForGivenCategory(category) for category in getGroupByCategories()]
    columns = {}
    for ele in list_of_codes:
        columns = {**columns,**ele}
    return columns

def getBirthAnalysisDataManually():
    '''
    A helper method to manually get birth data and build cache
    Returns a pandas dataframe
    '''
    print('Starting manual retrieval')
    columns = getColumns()
    measure_selection = {
    'M_002': 'D149.M002', # Births
    }
    observation_selection = {}
    variable_filter = {}
    col_list = []
    for code in columns:
        dataObj = WonderD149Data([code],measure_selection,observation_selection,variable_filter)
        data_col = dataObj.getData()
        col_data = pd.Series(data_col['Births'])
        col_data.name = columns[code]
        col_list.append(col_data)
        print(columns[code],'done')
    print(len(col_list), 'columns encountered')
    max_col = max(col_list,key=lambda x:len(x))
    MAX_COL_LEN = len(max_col)
    converted_col_list  =map(lambda x: interpolateSeries(x,MAX_COL_LEN),col_list)
    converted_col_list = [*converted_col_list]
    col_data_cleaned = pd.DataFrame(converted_col_list).T

    print('Data succesfully created and being cached')
    with open("data_column_birth_analysis.json", "w") as outfile:
        json.dump(col_data_cleaned.to_dict(), outfile, indent=4, sort_keys=False)
    return col_data_cleaned

def getBirthAnalysisData(cache=True):
    '''
        A helper method to query birth measure for all columns and create and interpolated dataframe of births database.

        --------------------
        Paramaters
        --------------------
        cache : bool
            this tels whether to look for cached value forcefully or not
        
        Returns a pandas dataframe
    '''
    try:
        assert(isinstance(cache,bool))
    except AssertionError as er:
        logger.error(str(er))
        raise er
    error_to_catch = getattr(__builtins__,'FileNotFoundError', IOError)
    if cache:
        try:
            logger.info('looking for cached values')
            f = open(str(pathlib.Path(__file__).parent.absolute()) +'/data_column_birth_analysis.json','r')
            DATA = json.load(f)
            print('cached data found')
            return pd.DataFrame.from_dict(DATA)
        except error_to_catch:
            logger.error('Cache not found hence falling back to manual retrieval')
            return getBirthAnalysisDataManually()
    return getBirthAnalysisDataManually()

def createCorrelationGraph(corr_matrix,edges):
    '''
        A helper method to generate a network graph with nodes as selected columns and edges with correlation values.

        -----------------
        Parameters
        -----------------
        corr_matrix : pd.DataFrame (A square matrix of same column and row length)
        edges: tuples of size 2 with column names
        Returns a Graph
    '''
    try:
        assert(isinstance(corr_matrix,pd.DataFrame))
        assert(isinstance(edges,list))
        list_of_possible_tuples = itertools.product(corr_matrix.index,corr_matrix.columns)
        assert(all([x in list_of_possible_tuples for x in edges]))
    except AssertionError as er:
        logger.error(str(er))
        raise er
    set_of_nodes = set()
    for combi in edges:
        set_of_nodes = set_of_nodes.union(combi)
    nodes = list(set_of_nodes)
    G = nx.Graph()
    for combi in edges:
        left,right = combi
        G.add_nodes_from([(nodes.index(left),{'name': left}),(nodes.index(right),{'name': right})])
        G.add_edge(nodes.index(left),nodes.index(right))
    correlation_edge_attrs = {}
    name_edge_attrs = {}
    for start_node, end_node, _ in G.edges(data=True):
        correlation_edge_attrs[(start_node, end_node)] = (corr_matrix[G.nodes[start_node]["name"]][G.nodes[end_node]["name"]])
        name_edge_attrs[(start_node, end_node)] = f'({G.nodes[start_node]["name"]}:{G.nodes[end_node]["name"]})'
    nx.set_edge_attributes(G, correlation_edge_attrs, "edge_length")
    nx.set_edge_attributes(G, name_edge_attrs, "edge_nodes")
    return G

def plotNetworkGraph(G,title,path):
    '''
        A helper method to plot network graph using bokeh
        -------------------------
        Parameters
        -------------------------

        G : nx.Graph

        title: str

        path: os.PathLike

        Returns plot

    '''
    try:
        assert(isinstance(G,nx.Graph))
        assert(isinstance(title,str))
        assert(isinstance(path,os.PathLike))
    except AssertionError as er:
        logger.error(str(er))
        raise er
    #Establish which categories will appear when hovering over each node
    HOVER_TOOLTIPS = [("Feature Names", "@edge_nodes" ),("Correlation","@edge_length")]

    #Create a plot — set dimensions, toolbar, and title
    plot = figure(tooltips = HOVER_TOOLTIPS,
                tools="pan,wheel_zoom,save,reset", active_scroll='wheel_zoom',
                x_range=Range1d(-10.1, 10.1), y_range=Range1d(-10.1, 10.1), title=title)

    #Create a network graph object with spring layout
    # https://networkx.github.io/documentation/networkx-1.9/reference/generated/networkx.drawing.layout.spring_layout.html
    network_graph = from_networkx(G, nx.spring_layout, scale=10, center=(0, 0))

    #Set node size and color
    network_graph.node_renderer.glyph = Circle(size=15, fill_color='skyblue')
    network_graph.node_renderer.selection_glyph = Circle(size=15, fill_color=Spectral4[2])
    network_graph.node_renderer.hover_glyph = Circle(size=15, fill_color=Spectral4[1])

    #Set edge opacity and width
    network_graph.edge_renderer.glyph = MultiLine(line_alpha=0.8, line_width=1)
    network_graph.edge_renderer.selection_glyph = MultiLine(line_color=Spectral4[2], line_width=1)
    network_graph.edge_renderer.hover_glyph = MultiLine(line_color=Spectral4[1], line_width=1)

    network_graph.selection_policy = NodesAndLinkedEdges()
    network_graph.inspection_policy = EdgesAndLinkedNodes()

    #Add network graph to the plot
    plot.renderers.append(network_graph)
    logger.info(f'plot saving to file {path}/{title}.html')
    save(plot, filename=f"{path}/{title}.html")
    return plot

def get_percent_data(data,issue_column,major_column):
    '''
    get percent data for yes and no

    Returns data
    '''
    assert isinstance(data,pd.DataFrame)
    assert isinstance(issue_column,str)
    assert isinstance(major_column,str)
    assert 'Births' in data.columns
    yes = data[data[issue_column]=='Yes']
    no = data[data[issue_column]=='No']
    yes['Total'] = yes['Births'].to_numpy()+no['Births'].to_numpy()
    yes['Percent of Mother Facing Issue'] = (yes['Births']/yes['Total'])*100
    yes['Issue']=issue_column
    res =yes[[major_column,"Percent of Mother Facing Issue","Issue"]].reset_index()[[major_column,"Percent of Mother Facing Issue","Issue"]]
    return res

def merge_dataframe_on_yes_and_no(yes_data,no_data,column,issue):
    '''
    a method to create yes no data required for plotting

    Returns required dataframe
    '''
    assert isinstance(yes_data,pd.DataFrame)
    assert isinstance(no_data,pd.DataFrame)
    assert 'Births' in yes_data.columns
    assert 'Births' in no_data.columns
    assert isinstance(column,str)
    assert isinstance(issue,str)
    yes_data[issue]='Yes'
    no_data[issue]='No'
    yes = yes_data['Births'].to_numpy()
    no =no_data['Births'].to_numpy()
    percent = (yes/(yes+no))*100
    yes_data['Percent of Mother Facing Issue'] = percent
    yes_data = yes_data[[column,"Percent of Mother Facing Issue"]]
    yes_data['Issue'] = issue
    return yes_data

def plot_line(final_df,x_col,title_text):
    '''
      Method to plot line graph

      Returns a fig
    '''
    assert isinstance(final_df,pd.DataFrame)
    assert isinstance(x_col,str)
    assert isinstance(title_text,str)
    assert x_col in final_df.columns
    assert "Percent of Mother Facing Issue" in final_df.columns
    assert "Issue" in final_df.columns
    fig = px.line(final_df,
              x=x_col,
              y="Percent of Mother Facing Issue",
              color="Issue",
              color_discrete_sequence=["rgb(255, 152, 90)", "rgb(119, 158, 204)", "rgb(255, 179, 71)", "rgb(48, 153, 217)"],
            #   trendline="ols",
            #    marginal_x="violin",
            #    marginal_y="box",
              width=1800,height=900)
    fig.update_layout(title={
                      'text':title_text,
                      'xanchor': 'center',
                      'yanchor': 'top',
                      'x': 0.5},
                      yaxis_title={'text': 'Percent of Mother Facing Issue'},
                      xaxis_title={'text': x_col})

    fig.update_layout(
        font_family="Verdana",
        font_color="black",
        font_size = 24,
        title_font_family="Verdana",
        title_font_color="black",
        title_font_size=28,
        legend_title_font_color="black"
    )
    return fig

def plot_histogram(final_df,x_col,title_text):
    '''
      Method to plot histogram graph

      Returns a fig
    '''
    assert isinstance(final_df,pd.DataFrame)
    assert isinstance(x_col,str)
    assert isinstance(title_text,str)
    assert x_col in final_df.columns
    assert "Percent of Mother Facing Issue" in final_df.columns
    assert "Issue" in final_df.columns
    fig = px.histogram(final_df,
              x=x_col,
              y="Percent of Mother Facing Issue",
              color="Issue",
              color_discrete_sequence=["rgb(255, 152, 90)", "rgb(119, 158, 204)", "rgb(255, 179, 71)", "rgb(48, 153, 217)"],
            #   trendline="ols",
            #    marginal_x="violin",
            #    marginal_y="box",
              width=1800,height=900)
    fig.update_layout(title={
                      'text':title_text,
                      'xanchor': 'center',
                      'yanchor': 'top',
                      'x': 0.5},
                      yaxis_title={'text': 'Percent of Mother Facing Issue'},
                      xaxis_title={'text': x_col})

    fig.update_layout(
        font_family="Verdana",
        font_color="black",
        font_size = 24,
        title_font_family="Verdana",
        title_font_color="black",
        title_font_size=28,
        legend_title_font_color="black"
    )
    return fig

__all__ = ['getGroupByCategories', 'getColumns', 'getCodeDetailsForGivenCategory', 'getFilterValuesForGivenCode', 'getMeasureCodesAndDescription','getParameterObject','sort_parameters','createParameterList','interpolateSeries','is_Different_Category','getBirthAnalysisData','createCorrelationGraph','plotNetworkGraph','get_percent_data','merge_dataframe_on_yes_and_no','plot_line','plot_histogram']