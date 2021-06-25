#!/usr/bin/env python3 

import subprocess as s
import os
from randmac import RandMac
import re

if not os.geteuid() == 0:
    print("[-] Script must be run as root !")
    exit()

i = 1

#s.call("clear",shell=True)

def change_mac(interface,new_mac):
    print(f"{interface} ---> {new_mac}")
    s.call(f"ifconfig {interface} down",shell=True)
    s.call(f"ifconfig {interface} hw ether {new_mac}",shell=True)
    s.call(f"ifconfig {interface} up",shell=True)
    print(f"[+] MAC Address changed from {current_mac.group(0)} to {new_mac}")

interfaces = os.listdir('/sys/class/net')

print("Available Interfaces : \n\n")

for interface in interfaces:
    print(f"{i} - {interface}")
    i += 1

print("\n")
index = int(input("Choose interface to change MAC > "))

dev = interfaces[index-1]

ifconfig_res = s.check_output("ifconfig " + str(dev),shell=True)

current_mac = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(ifconfig_res))

print(f"Current MAC for {dev} is {current_mac.group(0)}")
new_mac = input(f"Enter new MAC for {dev} , press ENTER for randomized mac > ")

if not new_mac:
    change_mac(dev,RandMac())

else:
    change_mac(dev,new_mac)
