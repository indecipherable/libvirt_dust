# Example-23.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
  print('Failed to open connection to qemu:///system', file=sys.stderr)
  exit(1)

mem = conn.getFreeMemory()
print("Free memory on node (host) is: " + str(mem) + " bytes.")
kmem = mem / 1024
print("Free memory on node (host) is: " + str(kmem) + " kbytes.")
mmem = kmem / 1024
print("Free memory on node (host) is: " + str(mmem) + " mbytes.")
gmem = mmem / 1024
print("Free memory on node (host) is: " + str(gmem) + " gbytes.")

conn.close()
exit(0)
