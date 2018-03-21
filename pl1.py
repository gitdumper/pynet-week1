#!/usr/bin/env python

import re
from ciscoconfparse import CiscoConfParse

cfg_file = 'cisco_ntp.txt'

cfg = CiscoConfParse(cfg_file)

# Playing around with compliance and attempting to use components
# from Learning Python

ntp_servers = cfg.find_objects('ntp server')

# Dump the found ntp servers
for ntp_server in ntp_servers:
  print(ntp_server.re_match_typed(regex=r'ntp server (\S+)'))

ntp_template = [ 'ntp server 130.126.24.24',
                 'ntp server 152.2.21.1',
                 'ntp server 1.2.3.4' ]

ntp_array = []
[ntp_array.append(ntp_server.text) for ntp_server in ntp_servers]
    
ntp_template = set(ntp_template)
ntp_array = set(ntp_array)

print("--- Playing with Sets ----")
print("In template but not in config")
print(ntp_template.difference(ntp_array))
print("In config but not in template")
print(ntp_array.difference(ntp_template))
