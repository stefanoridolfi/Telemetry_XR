import os

print("nome del file: "+__file__)

from ncclient import manager
from  lxml import etree
host='1.1.1.1'
print("get_config di:"+host) 
with manager.connect(host=host, port=830, username='admin', password='admin',hostkey_verify=False) as m2:
    c2=m2.server_capabilities
#print(c2)
#print(c2.data_ele)
#print(c2.data)
#print(etree.tostring(c2.data))
for elem in c2:
    print(elem)
