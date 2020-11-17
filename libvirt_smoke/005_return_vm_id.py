import os
import sys


def return_id(a_dom):
  try:
    # get the VM ID of "a_dom\ "
    bash_command = "virsh list --all | grep %s\ | awk '{print $1}'" % a_dom
    #os.system(bash_command)
    print("DEBUG: os.system(bash_command) is:")
   # print(os.system(bash_command)[0])
    return os.system(bash_command)
    #print("DEBUG: this_id is:")
    #print(this_id)
  except:
    print("No such domain %s") % a_dom

return_id(sys.argv[1])
