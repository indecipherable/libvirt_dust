
# Example-5.py
from __future__ import print_function
import sys
import libvirt

# opens qemu:///system as conn
conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)
# lists defined domains as domainNames
domainNames = conn.listDefinedDomains()
if conn == None:
    print('Failed to get a list of domain names', file=sys.stderr)

domainIDs = conn.listDomainsID()
if domainIDs == None:
    print('Failed to get a list of domain IDs', file=sys.stderr)
if len(domainIDs) != 0:
    for domainID in domainIDs:
        domain = conn.lookupByID(domainID)
        domainNames.append(domain.name)

print("Active domain IDs:")
if len(domainIDs) == 0:
    print('  None')
else:
    for domainID in domainIDs:
        print('  '+str(domainID))
        print("Killing active domain IDs:")
        print(conn.lookupByID(domainID))
        this_dom = conn.lookupByID(domainID)
        this_dom.destroy()

#print("All (active and inactive) domain names:")
#if len(domainNames) == 0:
#    print('  None')
#else:
#    for domainName in domainNames:
#        print('  ' + domainName)
#        print("Trying to kill: " + domainName)
#        this_dom = conn.lookupByName(domainName)
#        this_dom.destroy()

conn.close()
exit(0)
