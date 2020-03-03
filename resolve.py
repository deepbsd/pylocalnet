#!/usr/bin/env python3

import socket

hosts = ['zencat','scee','pumpkin','juno','jarhead',
        'dixie', 'peach', 'peanut','debbie', 'blub',
        'omalley','Maui','daisy','milo','tweety', 
        'erica', 'kitty', 'jazzcat', 'dolly' ]

local_dict = {}

for host in hosts:
    try:
        ip = socket.gethostbyname(str(host+'.lan'))
    except:
        ip = 'host not available'
    local_dict[host] = ip

for hostname, ip in local_dict.items():
    print("{0}:   \t{1}".format(hostname, ip))
