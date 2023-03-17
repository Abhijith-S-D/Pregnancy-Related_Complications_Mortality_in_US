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

## Folder Structure
```bash
.
├── README.md
├── presentation_materials
│   ├── ece143-final_presentation-cues.docx
│   ├── ece143-final_presentation.pptx
│   └── ece143-final_presentation_PDF.pdf
├── requirements.txt
└── wonderD149Data
    ├── LICENSE
    ├── README.md
    ├── __init__.py
    ├── __pycache__
    │   └── __init__.cpython-39.pyc
    ├── examples
    │   ├── All_Visualisation.ipynb                                       # All visualizations shown
    │   ├── Pregnancy_related_births_data_high_negative_correlation.html  # bokeh plot of high negative correlation
    │   ├── Pregnancy_related_births_data_high_positive_correlation.html  # bokeh plot of high positive correlation
    │   ├── data_column_birth_analysis.json
    │   ├── sampledataexploration.ipynb                                   # sample data exploration
    │   ├── wonderD149Data.log
    │   ├── wonderD149DataCorrelation.ipynb                               # notebook showing the correlation analysis
    │   └── wonderD149DataExample.ipynb                                   # Example usage 
    ├── htmlcov                                                           # coverage folder
    │   ├── __init___py.html
    │   ├── coverage_html.js
    │   ├── d_8873eea2b2d06a6e___init___py.html
    │   ├── d_8873eea2b2d06a6e_wonderD149Data_py.html
    │   ├── d_a44f0ac069e85531___init___py.html
    │   ├── d_a44f0ac069e85531_test_helper_py.html
    │   ├── d_d8d24d3066ba3a1f___init___py.html
    │   ├── d_d8d24d3066ba3a1f_helper_py.html
    │   ├── favicon_32.png
    │   ├── index.html
    │   ├── keybd_closed.png
    │   ├── keybd_open.png
    │   ├── status.json
    │   └── style.css
    ├── pyproject.toml
    ├── src
    │   ├── __pycache__
    │   │   └── __init__.cpython-39.pyc
    │   └── wonderD149Data                                                # main module
    │       ├── __init__.py
    │       ├── __pycache__
    │       │   ├── __init__.cpython-39.pyc
    │       │   └── wonderD149Data.cpython-39.pyc
    │       ├── data
    │       │   ├── __init__.py
    │       │   ├── __pycache__
    │       │   │   ├── __init__.cpython-39.pyc
    │       │   │   └── helper.cpython-39.pyc
    │       │   ├── abnormal_conditions_by_prenatal_total.csv
    │       │   ├── b_attr.json
    │       │   ├── data_column_birth_analysis.json
    │       │   ├── f_attr.json
    │       │   ├── helper.py                                             # helper file
    │       │   ├── i_attr.json
    │       │   ├── m_attr.json
    │       │   ├── misc_attr.json
    │       │   ├── o_attr.json
    │       │   ├── pregnancy_timeline
    │       │   │   ├── 1-during_pregnancy_deaths.csv
    │       │   │   ├── 2-day_of_delivery_deaths.csv
    │       │   │   ├── 3-before_42_days_deaths.csv
    │       │   │   ├── 4-total_lmd_by_year.csv
    │       │   │   └── 5-total_deaths_include_lmd_by_year.csv
    │       │   ├── races-total_births.csv
    │       │   ├── races-total_deaths.csv
    │       │   ├── states-total_births.csv
    │       │   ├── states-total_deaths.csv
    │       │   └── v_attr.json
    │       └── wonderD149Data.py                                         # main module file
    ├── tests
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-39.pyc
    │   │   └── test_helper.cpython-39-pytest-7.2.1.pyc
    │   ├── test_helper.py                                                # tests file
    │   └── test_outputs
    │       └── Test.html
    └── wonderD149Data.log
```

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