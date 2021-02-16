#! /usr/bin/env python3
from ncclient import manager
from  lxml import etree
import sys
#GigabitEthernet0/0/0/2
if len(sys.argv)<3:
    print("usage: ",sys.argv[0]," interface (ex. GigabitEthernet0/0/0/2) db (running/candidate)")
    exit()
interface=sys.argv[1]
db=sys.argv[2]
host='1.1.1.1'
#if_filter = '''<interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"/>'''
#if_filter = '''<interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>'''


if_filter = '''<interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
   <interface-configuration>
   <interface-name>'''+interface+'''</interface-name>
   </interface-configuration>
   </interface-configurations>
                                '''

print("get_config di:"+host)

with manager.connect(host=host, port=830, username='admin', password='admin',hostkey_verify=False) as m:
    c2=m.get_config(source=db, filter=('subtree', if_filter))
print(c2)
