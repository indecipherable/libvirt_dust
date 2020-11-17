# Example-6.py
from __future__ import print_function
import sys
import libvirt
# this isn't a real module of libvirt??
# import libvirt-domain

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

print("All (active and inactive) domain names:")
domains = conn.listAllDomains(0)
if len(domains) != 0:
    for domain in domains:
        print('  '+domain.name())
        #print('  '+domain.VIR_CONNECT_LIST_DOMAINS_RUNNING())
else:
    print('  None')

conn.close()
exit(0)
