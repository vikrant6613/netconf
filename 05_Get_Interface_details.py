from ncclient import manager
import json

configuration_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <GigabitEthernet>
                <name>2</name>
            </GigabitEthernet>
        </interface>
    </native>
</filter>"""

device_cred = json.loads(open("device_login.json").read())

with manager.connect(host=device_cred["host"], username=device_cred["username"],
                     password=device_cred["password"], port="830", hostkey_verify=False) as man:

    running_conf = man.get_config("running", configuration_filter)
    print(running_conf)
