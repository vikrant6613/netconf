from ncclient import manager
import json

device_cred = json.loads(open("device_login.json").read())

configuration_filter = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <ip><route>
            <ip-route-interface-forwarding-list>
                <prefix>192.198.2.0</prefix>
                <mask>255.255.255.0</mask>
                <fwd-list>
                    <fwd>GigabitEthernet1</fwd>
                    <interface-next-hop>
                        <ip-address>192.168.2.1</ip-address>
                    </interface-next-hop>
                </fwd-list>
            </ip-route-interface-forwarding-list>
        </route></ip>
    </native>
</config>"""

with manager.connect(host=device_cred["host"], username=device_cred["username"],
                     password=device_cred["password"], port="830", hostkey_verify=False) as man:

    conf_output = man.edit_config(configuration_filter, target="running")
    print(conf_output)
