import os
print("nome del file: "+__file__)

from ncclient import manager
from  lxml import etree
host='1.1.1.1'
hostname_filter = '''
                         <host-names xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-shellutil-cfg"/>
                          '''

print("get_config di:"+host)

with manager.connect(host=host, port=830, username='admin', password='admin',hostkey_verify=False) as m:
    c2=m.get_config(source='running', filter=('subtree', hostname_filter))
print(c2)
