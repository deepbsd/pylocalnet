#!/usr/bin/env python3

import socket

hosts = ['zencat','scee','pumpkin','juno','jarhead',
        'dixie','peach','peanut','erica','debbie',
        'blub','omalley','Maui','daisy','milo']

local_dict = {}

def resolve(hostname):
    return socket.gethostbyname(hostname)

for host in hosts:
    ip = socket.gethostbyname(host)
    local_dict[host] = str(ip)

for hostname, ip in local_dict.items():
    print("{0}: {1}".format(hostname, ip))
