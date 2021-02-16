#! /usr/bin/env python3
from ncclient import manager
from  lxml import etree
interface='GigabitEthernet0/0/0/0'
host='1.1.1.1'
#if_filter = '''<interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"/>'''
#if_filter = '''<interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>'''


if_filter = '''<interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
   <interface-configuration>
   <interface-name>GigabitEthernet0/0/0/2</interface-name>
   </interface-configuration>
   </interface-configurations>
                                '''
all_if_filter = '''<interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
   <interface-configuration>
      </interface-configuration>
   </interface-configurations> '''

print("get_config di:"+host)

with manager.connect(host=host, port=830, username='admin', password='admin',hostkey_verify=False) as m:
    c2=m.get_config(source='running', filter=('subtree', all_if_filter))
print(c2)
