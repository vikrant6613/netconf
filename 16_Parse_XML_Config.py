import xml.etree.ElementTree as ET

tree = ET.parse('int_running.xml')
root = tree.getroot()

# print(root[0])
# print(root[0].tag)
# print(root[0].text)
# print(root.attrib)

# print(root[0][0][0].tag)
# print(root[0][0][0][0][0])
# print(root[0][0][0][0][0].text)
# print(root[0][0][0][0][1].text)
#
# int_number = list(root)[0][0][0][0][0].text
# ip_number = list(root)[0][0][0][0][2][0][0][0].text
# print(f"GigabitEthernet {int_number} : {ip_number}")

num = int(input("enter the interface number : "))
num = num - 1
int_number = list(root)[0][0][0][num][0].text
ip_number = list(root)[0][0][0][num][2][0][0][0].text
print(f"GigabitEthernet {int_number} : {ip_number}")
