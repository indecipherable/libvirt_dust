
import libvirt
import sys

def inst_conn():
  conn = libvirt.openReadOnly(None)
  if conn == None:
      print('Failed to open connection to the hypervisor')
      sys.exit(1)
  try:
      dom0 = conn.lookupByName("deb900")
  except:
      print('Failed to find the main domain')
      sys.exit(1)
  print("Domain 0: id %d running %s" % (dom0.ID(), dom0.OSType()))
  print(dom0.info())
  print("inst_comm() completed")

# inst_conn_test(index) - accepts index and gets domain.info() 
def inst_conn_test(index):
  # deb90%r hardcodes deb90# domains
  this_dom = "deb90%r" % index
  # prints hardcoded deb90#
  print("\nDEBUG: this_dom")
  # opens connection to libvirt hypervisor
  conn = libvirt.openReadOnly(None)
  if conn == None:
      print('Failed to open connection to the hypervisor')
      sys.exit(1)
  try:
      dom_n = conn.lookupByName(this_dom)
  except:
      print('Failed to find the main domain')
      sys.exit(1)
  print("Domain 0: id %d running %s" % (dom_n.ID(), dom_n.OSType()))
  print(dom_n.info())
  print("inst_comm() completed")

#inst_conn()
inst_conn_test(0)
inst_conn_test(1)
inst_conn_test(2)
inst_conn_test(3)
