from ncclient import manager

host = "10.10.20.48"
port = "830"
username = "developer"
password = "C1sco12345"

with manager.connect(host=host, port=port, username=username,
                     password=password, hostkey_verify=False) as man:

    man.connected

    running_conf = man.get_config("running")
    print(running_conf)
