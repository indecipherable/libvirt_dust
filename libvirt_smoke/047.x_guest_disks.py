# Example-39.py
from __future__ import print_function
import sys
import libvirt
from xml.dom import minidom
# replace with dynamic `cwd`
sys.path.append('/home/whitemage/workspace/pys/libvirt_smoke/bin')
import return_vm_id_005 as rvi

def get_dom_id():
  ##dom_name = 'Fedora22-x86_64-1'
  #dom_name = 'deb9xx'
  dom_name = sys.argv[1]
  #print("This dom_name is:")
  #print(dom_name)
  print("DEBUG: this_dom_id is:")
  return rvi.return_id(dom_name)
  #print(this_dom_id)
  #dom_ID = rvi.return_id(dom_name)
  #print(dom_ID)

####print("this_dom_id is:")
####a = get_dom_id()
####print(a)
####exit

#this_dom_id = get_dom_id()
#print("this_dom_id is:")
#print(this_dom_id)

def check_domain():
  conn = libvirt.open('qemu:///system')
  if conn == None:
      print('Failed to open connection to qemu:///system', file=sys.stderr)
      exit(1)
  dom_name = sys.argv[1]
  this_dom_id = rvi.return_id(dom_name)
  #dom = conn.lookupByID(9)
  #dom = conn.lookupByID(this_dom_id)
  #dom = conn.lookupByID(dom_name)
  dom = conn.lookupByID(this_dom_id)
  if dom == None:
      print('Failed to find the domain '+dom_name, file=sys.stderr)
      exit(1)

def return_disks():
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
check_domain()
#return_disks()
#conn.close()
exit(0)
