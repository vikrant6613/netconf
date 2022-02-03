from ncclient import manager

host = "10.10.20.48"
port = "830"
username = "developer"
password = "C1sco12345"

with manager.connect(host=host, port=port, username=username,
                     password=password, hostkey_verify=False) as man:

    man.connected

    configuration_filter = """
    <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <hostname>csr1000v-1-test</hostname>
        </native>
    </config>"""

    conf_output = man.edit_config(configuration_filter, target="running")
    print(conf_output)
