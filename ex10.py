#!/usr/bin/env python

import re
from ciscoconfparse import CiscoConfParse

cfg_file = 'cisco_ipsec.txt'

cfg = CiscoConfParse(cfg_file)

# Find crypto maps that are not using AES

crypto_maps = cfg.find_objects_wo_child(parentspec=r'crypto map CRYPTO',
                                       childspec=r'AES')


for entry in crypto_maps:
  for child in entry.children:
    if 'transform' in child.text:
      # grab set from "set transform-set 3DES-SHA"
      match = re.search(r"set transform-set (.*)$", child.text)
      tset = match.group(1)
  print("{} >>> {}".format(entry.text.strip(), tset))




'''
 debugging with ipython
 type(crypto_maps)
 len(crypto_maps)
 dir(crypto_maps)
 dir(crypto_maps[0])
 crypto_maps[0].text
 crypto_maps[0].children
 crypto_maps[0].children[0].text
'''
