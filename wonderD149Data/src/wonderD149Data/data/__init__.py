import json, pathlib, logging, sys
import pandas as pd


log = logging.getLogger() #name of logger
log.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)

filehandler = logging.FileHandler('wonderD149Data.log')
filehandler.setLevel(logging.ERROR)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s") # set format

handler.setFormatter(formatter) # setup format
filehandler.setFormatter(formatter) # setup format
log.addHandler(handler) # read to go
log.addHandler(filehandler) # read to go

f = open(str(pathlib.Path(__file__).parent.absolute()) +'/b_attr.json','r')
B_ATTR = json.load(f)

f = open(str(pathlib.Path(__file__).parent.absolute()) +'/f_attr.json','r')
F_ATTR = json.load(f)

f = open(str(pathlib.Path(__file__).parent.absolute()) +'/i_attr.json','r')
I_ATTR = json.load(f)

f = open(str(pathlib.Path(__file__).parent.absolute()) +'/m_attr.json','r')
M_ATTR = json.load(f)

f = open(str(pathlib.Path(__file__).parent.absolute()) +'/misc_attr.json','r')
MISC_ATTR = json.load(f)

f = open(str(pathlib.Path(__file__).parent.absolute()) +'/o_attr.json','r')
O_ATTR = json.load(f)

f = open(str(pathlib.Path(__file__).parent.absolute()) +'/v_attr.json','r')
V_ATTR = json.load(f)

f.close()

races_deaths_df = pd.read_csv(str(pathlib.Path(__file__).parent.absolute()) +"/races-total_deaths.csv").drop(columns=["Notes", "Single Race 6 Code", "Year Code", "Population", "Crude Rate", "Hispanic Origin Code"])
races_births_df = pd.read_csv(str(pathlib.Path(__file__).parent.absolute()) +"/races-total_births.csv").drop(columns=["Notes", "Mother's Single Race 6 Code", "Year Code", "Mother's Hispanic Origin Code"])
states_death_df = pd.read_csv(str(pathlib.Path(__file__).parent.absolute()) +"/states-total_deaths.csv").drop(columns=["Notes", "State Code", "Year Code", "Population", "Crude Rate"])
states_births_df = pd.read_csv(str(pathlib.Path(__file__).parent.absolute()) +"/states-total_births.csv").drop(columns=["Notes", "State of Residence Code", "Year Code"])
pregnancy_deaths_df = pd.read_csv(str(pathlib.Path(__file__).parent.absolute()) +"/pregnancy_timeline/1-during_pregnancy_deaths.csv").drop(columns=["Notes", "Year Code", "Population", "Crude Rate"])
delivery_deaths_df = pd.read_csv(str(pathlib.Path(__file__).parent.absolute()) +"/pregnancy_timeline/2-day_of_delivery_deaths.csv").drop(columns=["Notes", "Year Code", "Population", "Crude Rate"])
before_42_deaths_df = pd.read_csv(str(pathlib.Path(__file__).parent.absolute()) +"/pregnancy_timeline/3-before_42_days_deaths.csv").drop(columns=["Notes", "Year Code", "Population", "Crude Rate"])
lmd_df = pd.read_csv(str(pathlib.Path(__file__).parent.absolute()) +"/pregnancy_timeline/4-total_lmd_by_year.csv").drop(columns=["Notes", "Year Code", "Population", "Crude Rate"])
total_deaths_df = pd.read_csv(str(pathlib.Path(__file__).parent.absolute()) +"/pregnancy_timeline/5-total_deaths_include_lmd_by_year.csv").drop(columns=["Notes", "Year Code", "Population", "Crude Rate"])
abnormal_conditions_df = pd.read_csv(str(pathlib.Path(__file__).parent.absolute()) +"/abnormal_conditions_by_prenatal_total.csv").drop(columns=["Notes", "Number of Prenatal Visits Code", "Year Code", "Abnormal Conditions Checked Code"])
del f
del json
del pathlib

__all__ = ['B_ATTR','F_ATTR','I_ATTR','M_ATTR','MISC_ATTR','O_ATTR','V_ATTR','log','helper','races_deaths_df','races_births_df','states_death_df','states_births_df','pregnancy_deaths_df','delivery_deaths_df','before_42_deaths_df','lmd_df','total_deaths_df','abnormal_conditions_df']