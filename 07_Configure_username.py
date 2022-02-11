from ncclient import manager
import json

configuration_filter = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <username>
            <name>netconf_test</name>       
            <privilege>15</privilege>
            <secret>
                <encryption>0</encryption>
                <secret>cisco6532</secret>
            </secret>
        </username>
    </native>
</config>"""

device_cred = json.loads(open("device_login.json").read())

with manager.connect(host=device_cred["host"], username=device_cred["username"],
                     password=device_cred["password"], port="830", hostkey_verify=False) as man:

    conf_output = man.edit_config(configuration_filter, target="running")
    print(conf_output)
