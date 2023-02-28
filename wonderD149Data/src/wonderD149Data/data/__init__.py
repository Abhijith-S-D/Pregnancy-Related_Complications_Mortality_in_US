import json, pathlib, logging, sys


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

del f
del json
del pathlib

__all__ = ['B_ATTR','F_ATTR','I_ATTR','M_ATTR','MISC_ATTR','O_ATTR','V_ATTR','log','helper']