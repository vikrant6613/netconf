from ncclient import manager, xml_
import json

device_cred = json.loads(open("device_login.json").read())

with manager.connect(host=device_cred["host"], username=device_cred["username"],
                     password=device_cred["password"], port="830", hostkey_verify=False) as man:
    device_output = man.get_config("running")
    # print(device_output)
    open("running.xml", 'w').write(str(device_output))
