from ncclient import manager, xml_

host = "10.10.20.48"
port = "830"
username = "developer"
password = "C1sco12345"

with manager.connect(host=host, port=port, username=username,
                     password=password, hostkey_verify=False) as man:
    man.connected

    configuration_filter = """
    <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface><GigabitEthernet>
                <name>2</name>
            </GigabitEthernet></interface>
        </native>
    </filter>"""

    device_output = man.get_config("running", configuration_filter)
    print(device_output)



with open("int_running.xml", 'w') as save:
    save.write(str(device_output)+"\n")
