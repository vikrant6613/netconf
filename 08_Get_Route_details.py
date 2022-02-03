from ncclient import manager

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
            <ip>
                <route></route>
            </ip>
        </native>
    </filter>"""

    running_conf = man.get_config("running", configuration_filter)
    print(running_conf)
