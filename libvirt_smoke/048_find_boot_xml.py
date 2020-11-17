import os
import glob, re
import time
import string
import sys
sys.path.append('/home/whitemage/workspace/pys/libvirt_smoke/bin')
import input_target_actual_999 as ait
import vm_check_004 as vm_checker
from collections import Counter 

# target_file = /run/libvirt/qemu/deb9xx.xml

#def refac(new_name):
#  for root, dirs, files in os.walk(project_rootdir):
#    for a_root in root:
#      if "barebones" in a_root:
#        print("DEBUG: root: " + a_root)
#    for a_dir in dirs:
#      if "barebones" in a_dir:
#        print("DEBUG: dir: " + a_dir)
#        os.rename(a_dir, new_name)
#    for a_file in files:
#      a_file=os.path.realpath(a_file)
#      if "barebones" in a_file:
#        print("DEBUG: file: " + a_file)
#        os.rename(a_file, new_name)
#      s = open(a_file,"r+")
#      for line in s.readlines():
#        if "barebones" in line:
#          print line
#          string.replace(line,'barebones',new_name)
#          print line
#      s.close()

# input_fuzz() calls input_target_actual to
# evaluate the input provided to sys.args[0]
# versus target_args provided to python
def input_fuzz():
  # target_args refers to input_target_actual
  # can be any number of args
  target_args = ('domain','vm_directory')
  #sys_argvs = (sys.argv)
  #ait.input_check1(target_arg_count, sys_argvs)
  #ait.input_check2(target_arg_count, target_args, sys_argvs)
  #ait.input_check3(target_args, sys_argvs)
  #ait.input_check(___,___)
  ait.input_check(target_args,(sys.argv)) 
  arg_list = list(sys.argv)
  #domain = print(sys.argv[1])
  #print("DEBUG: 048: arg_list[1] is:")
  #print(arg_list[1])
  # assigns this_dom as arg_list[1] which 
  # should be a domain in the system
  this_dom = (arg_list[1])
  #print("DEBUG: 048: this_dom is:")
  #print(this_dom)
  print("DEBUG: vm_checker result:")
  #print(vm_checker.dom_check(this_dom))
  try:
    print("DEBUG: vm_checker result:")
    vm_checker.dom_check(this_dom)
  except:
    print("Debug: Oops")
    sys.exit(1)

def find_config():
  print("DEBUG: find_config() running....")
  arg_list = list(sys.argv)
  this_dom = (arg_list[1])
  root_dir = (arg_list[2])
#  print("DEBUG: this_dom:")
#  print(this_dom)
#  print("DEBUG: root_dir:")
#  print(root_dir)
  for root, dirs, files in os.walk(root_dir):
    for file in files:
      if file.endswith("xml") and file.startswith(this_dom):
        #print("DEBUG: found it!")
        #print(file)
        return file
      else:
        pass
        #print("DEBUG: failed womp womp")

def main():
  input_fuzz()
  this_config = find_config()
  print(this_config)

main()

