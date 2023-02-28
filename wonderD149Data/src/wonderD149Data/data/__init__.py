import json, pathlib

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

__all__ = ['B_ATTR','F_ATTR','I_ATTR','M_ATTR','MISC_ATTR','O_ATTR','V_ATTR','helper']