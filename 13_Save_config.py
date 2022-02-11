from ncclient import manager, xml_
import json

device_cred = json.loads(open("device_login.json").read())

save_config = """
<cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>
"""

with manager.connect(host=device_cred["host"], username=device_cred["username"],
                     password=device_cred["password"], port="830", hostkey_verify=False) as man:

    reply = man.dispatch(xml_.to_ele(save_config))
    print(reply)
