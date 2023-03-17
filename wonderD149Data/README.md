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