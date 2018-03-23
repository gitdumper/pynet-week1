#!/usr/bin/env python

import re
from ciscoconfparse import CiscoConfParse

cfg_file = 'cisco_ntp.txt'
template_file = 'template.cfg'

cfg = CiscoConfParse(cfg_file)
template = CiscoConfParse(template_file)

ntp_servers = cfg.find_objects('ntp server')
ntp_servers_template = template.find_objects('ntp server')

# Dump the found ntp servers
#for ntp_server in ntp_servers:
#  print(ntp_server.re_match_typed(regex=r'ntp server (\S+)'))

ntp_array = []
[ntp_array.append(ntp_server.text) 
        for ntp_server in ntp_servers]
ntp_array = set(ntp_array)

ntp_array_template = []
[ntp_array_template.append(ntp_server.text) 
        for ntp_server in ntp_servers_template]
ntp_array_template = set(ntp_array_template)

print("In template but not in config")
print(ntp_array_template.difference(ntp_array))
print("In config but not in template")
print(ntp_array.difference(ntp_array_template))
