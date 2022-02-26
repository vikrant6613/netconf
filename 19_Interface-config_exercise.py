from ncclient import manager
import xmltodict
import json


def int_configuration(man, interface_filter):
    # print(man.connected)
    device_conf = man.get(interface_filter)
    interfaces_details = xmltodict.parse(device_conf.xml)["rpc-reply"]["data"]
    int_config = interfaces_details["interfaces"]["interface"]
    int_state = interfaces_details["interfaces-state"]["interface"]

    print("\nBelow are the Interfaces details : \n")

    for i in range(len(int_config)):
        print(f"Name: {int_config[i]['name']}")
        if 'description' in int_config[i].keys():
            print(f"Description: {int_config[i]['description']}")
        if 'address' in int_config[i]['ipv4'].keys():
            if isinstance(int_config[i]['ipv4']['address'], list):
                for _index_, ip_address in enumerate(int_config[i]['ipv4']['address']):
                    print(f"IP Address: {ip_address['ip']}")
            else:
                print(f"IP Address: {int_config[i]['ipv4']['address']['ip']}")
        print(f"Type: {int_config[i]['type']['#text']}")
        print(f"MAC Address: {int_state[i]['phys-address']}")
        print(f"Packets Input: {int_state[i]['statistics']['in-unicast-pkts']}")
        print(f"Packets Output: {int_state[i]['statistics']['out-unicast-pkts']}")
        print("----------------------------------------------")

if __name__ == '__main__':
    # pulling devices and credential details from device_login.json file
    device_cred = json.loads(open("device_login.json").read())
    # pulling filter from interface_filter.xml file
    _interface_filter_ = open("interface_filter.xml").read()
    man_obj = manager.connect(host=device_cred["host"], username=device_cred["username"],
                              password=device_cred["password"], port="830", hostkey_verify=False)
    int_configuration(man_obj, _interface_filter_)
    man_obj.close_session()
