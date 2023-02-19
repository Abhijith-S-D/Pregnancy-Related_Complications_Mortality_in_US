from wonderD149Data.data import B_ATTR as _B_ATTR, V_ATTR as _V_ATTR, M_ATTR as _M_ATTR, F_ATTR as _F_ATTR, O_ATTR as _O_ATTR, MISC_ATTR as _MISC_ATTR
import collections

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
    assert isinstance(category,str),f'the parameter of method should be a string but {type(category)} given'
    assert category in getGroupByCategories(),f'the provided category invalid. It must be among {getGroupByCategories()}'

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
    assert isinstance(code,str),f'the parameter of method should be a string but {type(code)} given'
    assert code in _B_ATTR.keys(),f'the provided code is invalid. It must be among {_B_ATTR.keys()}'
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
    assert isinstance(param_type,str) , f'the parameter of method should be a string but {type(param_type)} given'
    param_type = param_type.upper()
    assert param_type in ['B','F','I','M','O','V','MISC'] , f"the parameter of method should be one among {['B','F','I','M','O','V','MISC']} but {param_type} given"

    if param_type == 'B':
        if parameter_selections == {}:
            parameter_selections = []
        assert isinstance(parameter_selections,list), f"the parameter selections of B must be a list of B codes"
        assert len(parameter_selections)<6, f"A max of 5 codes can be selected in order for group by operation"
        assert set(parameter_selections) <= set(_B_ATTR.keys()), f"The list of selections can be only from among the B codes"
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
        assert isinstance(parameter_selections,dict), f"the parameter selections of M must be a dict of M codes"
        assert all([ x in list(_M_ATTR.keys()) and list(_M_ATTR[x].keys())[0] == parameter_selections[x] for x in parameter_selections]), f"The dict must follow M_ATTR data"
        m_parameters = {
            "M_002": "D149.M002",   # Births, must be included
        }
        for m_key in parameter_selections:
            m_parameters[m_key] = parameter_selections[m_key]
        return m_parameters
    elif param_type == 'F':
        assert parameter_selections == {}, f"cant select for F type"
        f_parameters = {k:[list(v.keys())[0]] for (k,v) in _F_ATTR.items()}
        return f_parameters
    elif param_type == 'I':
        assert parameter_selections == {}, f"cant select for I type"
        i_parameters = {f'I{k[1:]}':[list(v.values())[0]] for (k,v) in _F_ATTR.items()}
        return i_parameters
    elif param_type == 'O':
        assert isinstance(parameter_selections,dict), f"the parameter selections of O must be a dict of B codes"
        assert isinstance(o_params,dict), f"the o params selections of O must be a dict of O codes"
        assert len(parameter_selections.keys())<6, f"A max of 5 codes can be selected in order for group by operation"
        assert set([ x for x in parameter_selections.values() if x != '*None*']) <= set(_B_ATTR.keys()), f"The list of selections can be only from among the B codes"
        assert set(o_params.keys()) <= set(_O_ATTR.keys()), f"The list of selections can be only from among the O codes"
        assert all([ o_params[x] in _O_ATTR[x] for x in o_params]), f"The list of selections can be only from among the O codes"
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
        assert parameter_selections == {}, f"cant select for MISC type"
        return _MISC_ATTR
    else:
        assert isinstance(parameter_selections,dict), f"The parameter selection can be only dict but {type(parameter_selections)}observed"
        assert set(parameter_selections.keys()) <= set(_V_ATTR.keys()), f"The V codes must be valid"
        assert all(isinstance(x[1],list) and set(x[1]) <= set(_V_ATTR[x[0]].keys()) for x in parameter_selections.items())
        v_parameters = {k:[list(v.keys())[0]] for (k,v) in _V_ATTR.items()}
        for v_key in parameter_selections:
            v_parameters[v_key] = parameter_selections[v_key]
        return v_parameters
    
def sort_parameters(parameters):
    '''
    A helper method to sort dict based on keys
    '''
    assert isinstance(parameters,dict),f"parameters must be dict"
    return collections.OrderedDict(sorted(parameters.items()))

def createParameterList(parameterList):
    """Helper function to create a parameter list from a dictionary object"""
    assert isinstance(parameterList,dict),f"parameters must be dict"

    parameterString = ""
    
    for key in parameterList:
        parameterString += "<parameter>\n"
        parameterString += "<name>" + key + "</name>\n"
        
        if isinstance(parameterList[key], list):
            for value in parameterList[key]:
                parameterString += "<value>" + value + "</value>\n"
        else:
            parameterString += "<value>" + parameterList[key] + "</value>\n"
        
        parameterString += "</parameter>\n"
        
    return parameterString


__all__ = ['getGroupByCategories', 'getCodeDetailsForGivenCategory', 'getFilterValuesForGivenCode', 'getMeasureCodesAndDescription','getParameterObject','sort_parameters','createParameterList']