# Example-7.py
from __future__ import print_function
import sys
import libvirt

#xmlconfig = '<domain>........</domain>'
xmlconfig = '<domain type=kvm><name>deb901</name></domain>'
#xmlconfig0 = """<domain> <domain type=kvm> <name>deb901</name> <uuid>a536b2dc-2619-4133-b832-d4d1637e4aab</uuid> <memory unit=KiB>1048576</memory> <currentMemory unit=KiB>1048576</currentMemory> <vcpu placement=static>1</vcpu> <os> <type arch=x86_64 machine=pc-i440fx-bionic>hvm</type> <boot dev=cdrom/> <boot dev=hd/> </os> <features> <acpi/> <apic/> <vmport state=off/> </features>"""
#xmlconfig1 = """<cpu mode=custom match=exact check=partial> <model fallback=allow>Westmere-IBRS</model> </cpu> <clock offset=utc> <timer name=rtc tickpolicy=catchup/> <timer name=pit tickpolicy=delay/> <timer name=hpet present=no/> </clock> <on_poweroff>destroy</on_poweroff> <on_reboot>restart</on_reboot> <on_crash>destroy</on_crash> <pm> <suspend-to-mem enabled=no/> <suspend-to-disk enabled=no/> </pm> <devices> <emulator>/usr/bin/kvm-spice</emulator> <disk type=file device=disk> <driver name=qemu type=raw/> <source file=/mnt/vms/vms01-VMsVol01/vm01/> <target dev=vda bus=virtio/> <address type=pci domain=0x0000 bus=0x00 slot=0x07 function=0x0/>"""
#xmlconfig2 = """</disk> <disk type=file device=cdrom> <driver name=qemu type=raw/> <target dev=hda bus=ide/> <readonly/> <address type=drive controller=0 bus=0 target=0 unit=0/> </disk> <controller type=usb index=0 model=ich9-ehci1> <address type=pci domain=0x0000 bus=0x00 slot=0x05 function=0x7/> </controller> <controller type=usb index=0 model=ich9-uhci1> <master startport=0/> <address type=pci domain=0x0000 bus=0x00 slot=0x05 function=0x0 multifunction=on/> </controller> <controller type=usb index=0 model=ich9-uhci2> <master startport=2/> <address type=pci domain=0x0000 bus=0x00 slot=0x05 function=0x1/> </controller>"""
#xmlconfig3 = """<controller type=usb index=0 model=ich9-uhci3> <master startport=4/> <address type=pci domain=0x0000 bus=0x00 slot=0x05 function=0x2/> </controller> <controller type=pci index=0 model=pci-root/> <controller type=ide index=0> <address type=pci domain=0x0000 bus=0x00 slot=0x01 function=0x1/> </controller> <controller type=virtio-serial index=0> <address type=pci domain=0x0000 bus=0x00 slot=0x06 function=0x0/> </controller> <interface type=network> <mac address=52:54:00:2e:27:54/> <source network=default/> <model type=virtio/> <address type=pci domain=0x0000 bus=0x00 slot=0x03 function=0x0/> </interface>"""
#xmlconfig4 = """<interface type=direct> <mac address=52:54:00:18:7d:71/> <source dev=enp1s0f0 mode=bridge/> <model type=rtl8139/> <address type=pci domain=0x0000 bus=0x00 slot=0x0a function=0x0/> </interface> <serial type=pty> <target type=isa-serial port=0> <model name=isa-serial/> </target> </serial> <console type=pty> <target type=serial port=0/> </console> <channel type=unix> <target type=virtio name=org.qemu.guest_agent.0/> <address type=virtio-serial controller=0 bus=0 port=1/> </channel> <channel type=spicevmc> <target type=virtio name=com.redhat.spice.0/> <address type=virtio-serial controller=0 bus=0 port=2/>"""
#xmlconfig5 = """</channel> <input type=tablet bus=usb> <address type=usb bus=0 port=1/> </input> <input type=mouse bus=ps2/> <input type=keyboard bus=ps2/> <graphics type=spice autoport=yes> <listen type=address/> <image compression=off/> </graphics> <sound model=ich6> <address type=pci domain=0x0000 bus=0x00 slot=0x04 function=0x0/> </sound> <video> <model type=qxl ram=65536 vram=65536 vgamem=16384 heads=1 primary=yes/> <address type=pci domain=0x0000 bus=0x00 slot=0x02 function=0x0/> </video> <redirdev bus=usb type=spicevmc> <address type=usb bus=0 port=2/> </redirdev> <redirdev bus=usb type=spicevmc> <address type=usb bus=0 port=3/>"""
#xmlconfig6 = """</redirdev> <memballoon model=virtio> <address type=pci domain=0x0000 bus=0x00 slot=0x08 function=0x0/> </memballoon> <rng model=virtio> <backend model=random>/dev/urandom</backend> <address type=pci domain=0x0000 bus=0x00 slot=0x09 function=0x0/> </rng> </devices> </domain>"""
#xmlconfig = xmlconfig0 + xmlconfig1 + xmlconfig2 + xmlconfig3 + xmlconfig4 + xmlconfig5 + xmlconfig6
#xmlconfig = "'%s'" % xmlconfig
#print(xmlconfig)

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

dom = conn.createXML(xmlconfig, 0)
if dom == None:
    print('Failed to create a domain from an XML definition.', file=sys.stderr)
    exit(1)

print('Guest '+dom.name()+' has booted', file=sys.stderr)

conn.close()
exit(0)
