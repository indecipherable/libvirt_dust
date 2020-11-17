from nose.tools import *
import libvirt_smoke

def setup():
  print "SETUP!"

def teardown():
  print "TEAR DOWN!"

def test_basic():
  print "I RAN!"
