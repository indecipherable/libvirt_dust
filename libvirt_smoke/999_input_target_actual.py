# 048_check_boot.py
# this program accepts 2 args:
# 1. target_var_count
# 2. actual_var_count


import os
import glob, re
import time
import string
import sys
from collections import Counter 


#def input_check1(target_argcount, sys_argvs):
#  #if valid_check != 1:
#  #  print("we have not yet checked input")
#  #arguments = len(sys.argv) - 1
#  arguments = len(sys_argvs) - 1
#  print("the script is called with %i arguments" % (arguments))
#  print("sys.argv is:")
#  print(sys.argv)
#  if arguments < 2:
#    print("wrong number of args; expected 2; got %i" % (arguments))
#    exit
#  elif arguments > 2:
#    print("wrong number of args; expected 2; got %i" % (arguments))
#    exit
#  else:
#    return
#   # print("right number of args, continuing ..")
#def input_check2(target_argcount, target_args, sys_argvs):
#  #if valid_check != 1:
#  #  print("we have not yet checked input")
#  #arguments = len(sys.argv) - 1
#  arguments = len(sys_argvs) - 1
#  print("the script is called with %i arguments" % (arguments))
#  print("DEBUG: sys.argv is:")
#  print(sys.argv)
#  print("DEBUG: target args is:")
#  print(target_args)
#  if arguments < 2:
#    print("wrong number of args; expected 2; got %i" % (arguments))
#    exit
#  elif arguments > 2:
#    print("wrong number of args; expected 2; got %i" % (arguments))
#    exit
#  else:
#    return
def input_check(target_args, sys_argvs):
  target_argcount = len(target_args)
  actual_argcount = len(sys_argvs) - 1
  these_sysargvs = list(sys_argvs)
#  print("Debug: 999.0: this script is:")
#  print(these_sysargvs[0])
#  print("DEBUG: the script is called with %i arguments" % (arguments))
#  print("DEBUG: sys.argv is:")
#  print(sys.argv)
#  print("DEBUG: target args is:")
#  print(target_args)
  if target_argcount < actual_argcount:
    print("expected %r; got %s" % (target_args, sys_argvs))
    sys.exit(1)
  elif target_argcount > actual_argcount:
    print("expected %r; got %s" % (target_args, sys_argvs))
    sys.exit(1)
  else:
    return
