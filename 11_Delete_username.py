from ncclient import manager
import json

device_cred = json.loads(open("device_login.json").read())

configuration_filter = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <username operation="delete">
            <name>netconf_test</name>
            <privilege>15</privilege>
            <secret>
                <encryption>5</encryption>
                <secret>$1$ipo8$AHJsqmnVaf7apFmVQzDBp0</secret>
            </secret>
        </username>
    </native>
</config>"""

with manager.connect(host=device_cred["host"], username=device_cred["username"],
                     password=device_cred["password"], port="830", hostkey_verify=False) as man:

    conf_output = man.edit_config(configuration_filter, target="running")
    print(conf_output)
