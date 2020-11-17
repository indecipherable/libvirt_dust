# Example-39.py
from __future__ import print_function
import sys
import libvirt
from xml.dom import minidom

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

print("DEBUG: thisDomName sys.argv[1] is:")
thisDomName = sys.argv[1]
print(thisDomName)
print("DEBUG: thisDomName is:")
print("%s" % thisDomName)
thisDom = conn.lookupByName("%s" % thisDomName)
print("DEBUG: thisDom = ")
print(thisDom)
print("DEBUG: thisDom.ID() is:")
print(thisDom.ID())
thisDomID = thisDom.ID()
print("DEBUG: thisDomID is:")
print(thisDomID)


try:
  print("Debug: lookupByID:")
  dom = conn.lookupByID(thisDomID)
  #print(conn.lookupByID(thisDomID))
  print(conn.lookupByID(thisDomID))
  if dom == None:
      print('Failed to find the domain '+domName, file=sys.stderr)
      exit(1)
except:
  print("Oops")

try:
  raw_xml = dom.XMLDesc(0)
  xml = minidom.parseString(raw_xml)
  diskTypes = xml.getElementsByTagName('disk')
  for diskType in diskTypes:
      print('disk: type='+diskType.getAttribute('type')+' device='+diskType.getAttribute('device'))
      diskNodes = diskType.childNodes
      for diskNode in diskNodes:
          if diskNode.nodeName[0:1] != '#':
              print('  '+diskNode.nodeName)
              for attr in diskNode.attributes.keys():
                  print('    '+diskNode.attributes[attr].name+' = '+
                   diskNode.attributes[attr].value)
except:
  print("Oops - domain has to be running for virsh to get disk details")

conn.close()
exit(0)
