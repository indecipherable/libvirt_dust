import libvirt
import sys
sys.path.append('/home/whitemage/workspace/pys/libvirt_smoke/bin')
import input_target_actual_999 as ait

def derp():
  print(derp)
def dom_check(some_domain):
  #print("DEBUG: some_domain is:")
  #print(some_domain)
  #target_args = 'a_domain'
  #ait.input_check(target_args,(sys.argv))
  conn = libvirt.openReadOnly(None)
  if conn == None:
      print('Failed to open connection to the hypervisor')
      sys.exit(1)
  try:
    this_domain = conn.lookupByName(some_domain)
  #  print("DEBUG: 004.1: trying to try")
  #  print("DEBUG: 004.2: this_domain is:")
  #  print(this_domain)
  #  sys.exit(0)
  #  return 0
    #return this_domain.ID()
    print("DEBUG: 004.3: this_domain.info():")
    print(this_domain.info())
    print("DEBUG: 004.2: this_domain.ID() is:")
    print(this_domain.ID())
  except:
      print('Failed to find the main domain')
      sys.exit(1)
#  print("DEBUG: 004: some_domain.ID():")
#  print(this_domain.ID())
#  print("DEBUG: 004: some_domain.OSType():")
#  print(this_domain.OSType())
#  #print("Domain 0: id %d running %s" % (some_domain.ID(), some_domain.OSType()))
#  print(this_domain.info())

dom_check("fed801")
