# WonderD149Data Package

A small package to extract data from CDC Wonder API for Natality data

Setup:
    'conda create --name <env> python=3.9.16'
    'pip install -r requirements.txt'    

Examples:
    The example usage of our module and its analysis are performed within jupyter notebooks located at examples/ folder.

Testing:
    Go to wonderD149Data folder and run "pytest"

Coverage:
    Go to wonderD149Data folder and run "coverage run --source=. -m pytest -v tests && coverage report -m && coverage html"

## An Example Implementation:
```

  group_by_list = [

    'D149.V20', # Years

    'D149.V71', #Tobacco Use]

   measure_selection = {

    'M_002': 'D149.M002', # Births

    'M_007': 'D149.M007', # Percent of Total Births

    'M_070': 'D149.M070', # Average Age of Mother (years)}

   observation_selection = {}

   variable_filter = {

    'V_D149.V71': ['1','2','3','4'] # filtering only stated deliveries}

  dataObj = wd.WonderD149Data(group_by_list,measure_selection,observation_selection,variable_filter)

  dataObj.getData()

```