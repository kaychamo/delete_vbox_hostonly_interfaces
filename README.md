# DELETE VIRTUALBOX HOSTONLY INTERFACES

Simple python3 script (#don't mess with powershell)  
Used to delete "VirtualBox Host-Only Ethernet Adapter" under Windows (that you may have in excess when using vagrant)  

- Activate these interfaces (Win+R keyboard shortcut => "ncpa.cpl" )
- then run the script

`python delete_vbox_hostonly_interfaces.py`

results:

![image](result.png "result")
