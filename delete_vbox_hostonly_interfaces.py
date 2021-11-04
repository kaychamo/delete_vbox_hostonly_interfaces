import subprocess
import re
import os

interfaces = subprocess.check_output("VBoxManage list hostonlyifs")
#print(type(interfaces))
interfaces = interfaces.decode('ISO-8859-1')
#print(interfaces)

interface = re.compile('Name:   .*\r')
interface_names = interface.findall(interfaces)

for interface in enumerate(interface_names):
    interface=interface[1]
    separator="VirtualBox"
    todelete = separator + interface.split(separator, 1)[-1]
    print(f"deleting {todelete}")
    os.system(f'vboxmanage hostonlyif remove "{todelete}"')