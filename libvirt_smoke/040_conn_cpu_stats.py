# Example-30.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

index = 0
stats = conn.getCPUStats(index)
#index = "all"
#stats = conn.getCPUStats(libvirt.VIR_NODE_CPU_STATS_ALL_CPUS)

def cpu_stat_index(index,stats):
  print("CPU: " + str(index))
  print("------")
  kernel_hz = stats['kernel']
  kernel_mhz = kernel_hz / 1024
  idle_hz = stats['idle']
  user_hz = stats['user']
  iowait_hz = stats['iowait']
  #kernel_ghz = (kernel_hz / 1024) / 1024
#  idle_mhz = idle_hz / 1024
#  user_mhz = user_hz / 1024
#  iowait_mhz = iowait_hz / 1024
#  print(str(kernel_mhz))
#  print(str(idle_mhz))
#  print(str(user_mhz))
#  print(str(iowait_mhz))
#  print("kernel: " + str(stats['kernel']))
#  print("idle:   " + str(stats['idle']))
#  print("user:   " + str(stats['user']))
#  print("iowait: " + str(stats['iowait']))
  print(str(stats['kernel']))
  print(str(stats['idle']))
  print(str(stats['user']))
  print(str(stats['iowait']))
  print(kernel_mhz)
  #print(kernel_ghz)

cpu_stat_index(index,stats)

conn.close()
exit(0)
