#! /usr/bin/env python3
from ncclient import manager
from  lxml import etree
import datetime
import sys

if len(sys.argv) <2:
    print("usage: ",sys.argv[0],"running/candidate")
    sys.exit()
db=sys.argv[1]
interface='GigabitEthernet0/0/0/0'
host='1.1.1.1'
#if_filter = '''<interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"/>'''
#if_filter = '''<interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>'''
datetime=datetime.datetime.strftime(datetime.datetime.now(),'%y-%m-%d %H:%M:%S')

if_filter = '''<config>
<interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
<interface-configuration>
<interface-name>GigabitEthernet0/0/0/2</interface-name>
</interface-configuration></interface-configurations>
</config>'''

print("edit_config di:"+host)


config_if='''<config><interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"> 
<interface-configuration><active>act</active><interface-name>GigabitEthernet0/0/0/2</interface-name> <description>Giga 0/0/2 edit by nccclient: data time  '''+datetime+'''</description>
</interface-configuration></interface-configurations></config>'''






config_if2='''<config><interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
   <interface-configuration>
    <active>act</active>
    <interface-name>GigabitEthernet0/0/0/2</interface-name>
    <description>test single IF Netconf ncclient</description>
    <ipv4-network xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-io-cfg">
     <addresses>
      <primary>
       <address>9.9.9.9</address>
       <netmask>255.255.255.0</netmask>
      </primary>
     </addresses>
    </ipv4-network>
   </interface-configuration>
  </interface-configurations></config>
'''

config_if3='''<config><interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
   <interface-configuration>
  
       <active>act</active>
    <interface-name>GigabitEthernet0/0/0/2</interface-name>
 <shutdown/>
    <description>Giga 0/0/2 edit by nccclient: data time (config_if3) '''+datetime+'''</description>
    <ipv4-network xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-io-cfg">
 <addresses>
 <primary>
 <address>9.9.9.9</address>
 <netmask>255.255.255.0</netmask>
 </primary>
 </addresses>
    </ipv4-network>
      </interface-configuration>
  </interface-configurations></config>
'''


config_if4='''<config><interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
   <interface-configuration>
  
       <active>act</active>
    <interface-name>GigabitEthernet0/0/0/2</interface-name>
 <shutdown/>
    <description>Giga 0/0/2 edit by nccclient: data time (config_if3) '''+datetime+'''</description>
    <ipv4-network xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-io-cfg">
 <addresses>
 <primary>
 <address>9.9.9.9</address>
 <netmask>255.255.255.0</netmask>
 </primary>
 </addresses>
    </ipv4-network>
      </interface-configuration>
  </interface-configurations></config>
'''


with manager.connect(host=host, port=830, username='admin', password='admin',hostkey_verify=False) as m:
    c1=m.locked(target='candidate')
    #c2=m.edit_config(target='candidate',config=config_if4,default_operation='replace')
    c2=m.edit_config(target="candidate",config=config_if4,default_operation='merge')
    c3=m.validate()

    if db=="running":
        print(" edit in running")
        c4=m.commit()

print("edit candidate ",c2)
print("validate ",c3)
if db=="running":
    print("commit ",c4)
else:
    print("Not commited")

