#!/usr/bin/env python3

import socket
import subprocess

hosts = ['zencat','scee','pumpkin','juno','jarhead',
        'dixie', 'peach', 'peanut','debbie', 'blub',
        'omalley','Maui','daisy','milo','tweety', 
        'erica', 'kitty', 'jazzcat', 'dolly' ]

local_dict = {}

def show_ips():
    available_hosts = []
    for host in hosts:
        try:
            ip = socket.gethostbyname(host+".lan")
        except:
            ip = 'host not available'
        local_dict[host] = ip
    for hostname, ip in local_dict.items():
        available_hosts.append("{0}:   \t{1}".format(hostname,ip))
    return available_hosts

def arpall():
    hosts = subprocess.check_output(("arp", "-a"))
    return hosts

if __name__ == "__main__":
    #for line in show_ips(): print(line)
    print(arpall())
