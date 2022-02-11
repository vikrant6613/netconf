from ncclient import manager
import json

device_cred = json.loads(open("device_login.json").read())

configuration_filter = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <GigabitEthernet>
                <name>2</name>
                <description>Configured by Netconf</description>
                <ip><address><primary>
                    <address>192.168.0.1</address>
                    <mask>255.255.255.0</mask>
                </primary></address></ip>
            </GigabitEthernet>
        </interface>
    </native>
</config>"""

with manager.connect(host=device_cred["host"], username=device_cred["username"],
                     password=device_cred["password"], port="830", hostkey_verify=False) as man:

    conf_output = man.edit_config(configuration_filter, target="running")
    print(conf_output)
