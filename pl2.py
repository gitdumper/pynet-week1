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

ntp_set = []
[ntp_set.append(ntp_server.text) 
        for ntp_server in ntp_servers]
ntp_set = set(ntp_set)

ntp_set_template = []
[ntp_set_template.append(ntp_server.text) 
        for ntp_server in ntp_servers_template]
ntp_set_template = set(ntp_set_template)

print("In template but not in config")
print(ntp_set_template.difference(ntp_set))
print("In config but not in template")
print(ntp_set.difference(ntp_set_template))
