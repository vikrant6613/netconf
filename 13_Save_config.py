from ncclient import manager, xml_

host = "10.10.20.48"
port = "830"
username = "developer"
password = "C1sco12345"

with manager.connect(host=host, port=port, username=username,
                     password=password, hostkey_verify=False) as man:
    man.connected

    save_config = """
    <cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>
    """
    reply = man.dispatch(xml_.to_ele(save_config))
    print(reply)
