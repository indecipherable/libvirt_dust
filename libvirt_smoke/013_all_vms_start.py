
# Example-5.py
from __future__ import print_function
import sys
import libvirt


conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

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

print("All (active and inactive) domain names:")
if len(domainNames) == 0:
    print('  None')
else:
    for domainName in domainNames:
        print('  ' + domainName)
        print("Trying to start: " + domainName)
        try:
          this_dom = conn.lookupByName(domainName)
          this_dom.create()
        except libvirt.libvirtError:
          print("DEBUG: libvirt.libvirtError")
          raise
        except libvirtError:
          print("DEBUG: libvirtError")
          raise
        except:
          print("Unexpected error:", sys.exc_info()[0])
          raise

conn.close()
exit(0)
