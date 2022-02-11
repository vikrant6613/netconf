from ncclient import manager
import json

device_cred = json.loads(open("device_login.json").read())

with manager.connect(host=device_cred["host"], username=device_cred["username"],
                     password=device_cred["password"], port="830", hostkey_verify=False) as man:

    schema = man.get_schema("Cisco-IOS-XE-native")
    print(schema)
