# Example-20.py
from __future__ import print_function
import sys
import libvirt
from xml.dom import minidom

filename = '/var/lib/libvirt/save/deb901.img'

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

#print(conn.lookupByName('deb901'))
dom = conn.lookupByName('deb901')
if dom == None:
    print('Cannot find guest to be saved.', file=sys.stderr)
    exit(1)

state,maxmem,mem,cpus,cput = dom.info()

#print(dom)
print(type(dom))
print(dom.ID(),dom.OSType())
#print("dom.info type is: " + type(dom.info()))

info = dom.info()
if info == None:
    print('Cannot check guest state', file=sys.stderr)
    exit(1)
#print("dom.info() type is:")
#print(type(info))
#print("info is:")
#print(info)
#print("dom.state is:")
#print(state)

state,reason=dom.state()
print("dom.state() is:")
print(state)
print("dom.reason() is:")
print(reason)
print("testing state VIR_DOMAIN_NOSTATE:")
print(libvirt.VIR_DOMAIN_NOSTATE)
print("testing state VIR_DOMAIN_RUNNING:")
print(libvirt.VIR_DOMAIN_RUNNING)
print("testing state VIR_DOMAIN_BLOCKED:")
print(libvirt.VIR_DOMAIN_BLOCKED)
print("testing state VIR_DOMAIN_PAUSED:")
print(libvirt.VIR_DOMAIN_PAUSED)
print("testing state VIR_DOMAIN_SHUTDOWN")
print(libvirt.VIR_DOMAIN_SHUTDOWN)
print("testing state VIR_DOMAIN_SHUTOFF")
print(libvirt.VIR_DOMAIN_SHUTOFF)
print("testing state VIR_DOMAIN_CRASHED")
print(libvirt.VIR_DOMAIN_CRASHED)
print("testing state VIR_DOMAIN_PMSUSPENDED")
print(libvirt.VIR_DOMAIN_PMSUSPENDED)

if dom.state == libvirt.VIR_DOMAIN_SHUTOFF:
    print('Not saving guest that is not running', file=sys.stderr)
    exit(1)

if dom.save(filename) < 0:
    print('Unable to save guest to '+filename, file=sys.stderr)

print('Guest state saved to '+filename, file=sys.stderr)

conn.close()
exit(0)
