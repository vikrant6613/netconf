from ncclient import manager
import re
import json

device_cred = json.loads(open("device_login.json").read())

with manager.connect(host=device_cred["host"], username=device_cred["username"],
                     password=device_cred["password"], port="830", hostkey_verify=False) as man:
    capabilites = []
    for caps in man.server_capabilities:
        # storing the capabilites
        capabilites.append(caps)
    # sorting the capabilites
    capabilites = sorted(capabilites)

    module_lists = []
    for capability in capabilites:
        # pulling the module name from the capability
        # regex string = starts with module= , after that any characters(.*), ends with &
        search_module = re.search("module=(.*)&", capability)
        if search_module is not None:
            module_lists.append(search_module.groups()[0])

    models_desired = ['openconfig-extensions', 'openconfig-interfaces']
    # Iterate each desired model and write it to file
    for model in models_desired:
        schema = man.get_schema(model)
        open(f"./{model}.yang", 'w').write(schema.data)
