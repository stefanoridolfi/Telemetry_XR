import os
import re
print("nome del file: "+__file__)

from ncclient import manager
from  lxml import etree
import  xml.etree.ElementTree as ET
import xmltodict
host='1.1.1.1'
#filter = "native/hostname"
#filter = "native/counters"
#filter = "interfaces/interface"
filter = "interfaces/interface[name='GigabitEthernet1']"
#filter = "interfaces/interface[name='GigabitEthernet1']/description"

print("get_config di:"+host)

with manager.connect(host=host, port=830, username='admin', password='admin',hostkey_verify=False,device_params={'name':'iosxr'}) as m:
    c2=m.get_config(source='running', filter=('xpath', filter))
c2_data=c2.data_xml


#print("c2:",c2)
#print("\n\n c2 type:",type(c2))
print("c2_data\n",c2_data)
#print("c2_data type::  \n",type(c2_data))

print("\n############################################################\n")
#print("c2_data type\n", type(c2_data))
#print("c2.data type:",  type(c2.data))
#print("\n\n tree_string:  ",tree_string=etree.tostring(c2.data))
d=xmltodict.parse(c2_data)
#print(tree_string)
#print("etree to dict\n")
#print(etree_to_dict(c2.data))
#print("c2.data_ele")
#tree=ET.fromstring(c2)
#print("type tree_string", type(tree_string))
#print("type tree",type(tree))
#print("tree\n\n")
#print(tree)
#for child in tree:
#    print("tag:", child.tag,"   attribute:    ", child.attrib)
#print("dizionario type :    \n ",type(d))
#print("dizionario:    \n ",d)
#c2_data_list=c2_data.split("</")


def diz_iter(di):
    if isinstance(di,dict):
        for k in di:
            print("k:",k,"v:",di[k],"++++++++  type di",di[k],"+++", type(di[k]),"+++\n")
            diz_iter(di[k])
diz_iter(d)
'''
c2_data_list=re.split('</(\w+)>',c2_data)
for elem in c2_data_list:
    print(elem)
'''

''''

print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV\n\n")
def tt(di):
    for ele in di.values():
        if isinstance(ele,dict):
           for k, v in ele.items():
               print("key:",k,"value:",v,"type value:", type(v),"\n\n")
               
tt(d)



for k in d:
    print("\n k=",k,"-----","v=",d[k])
    for k1 in d[k]:
        print("\n k1=",k1,"----","v1=",d[k][k1])



print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ\n\n")
root=ET.fromstring(c2_data)
for child in root:
    print("tag:", child.tag, "  attrib:  ",child.attrib)

'''
