from ncclient import manager, xml_

host = "10.10.20.48"
port = "830"
username = "developer"
password = "C1sco12345"

with manager.connect(host=host, port=port, username=username,
                     password=password, hostkey_verify=False) as man:
    man.connected

    device_output = man.get_config("running")
    print(device_output)

with open("running.xml", 'w') as save:
    save.write(str(device_output))
