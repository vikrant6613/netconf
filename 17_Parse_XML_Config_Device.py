import xml.etree.ElementTree as ET
from ncclient import manager, xml_
import json

device_cred = json.loads(open("device_login.json").read())

configuration_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface></interface>
    </native>
</filter>"""

with manager.connect(host=device_cred["host"], username=device_cred["username"],
                     password=device_cred["password"], port="830", hostkey_verify=False) as man:

    device_output = man.get_config("running", configuration_filter)

root = ET.fromstring(str(device_output))

num = int(input("enter the interface number : "))
num = num - 1
int_number = list(root)[0][0][0][num][0].text
ip_number = list(root)[0][0][0][num][2][0][0][0].text
print(f"GigabitEthernet {int_number} : {ip_number}")
