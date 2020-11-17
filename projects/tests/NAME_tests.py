# Import nose tools
from nose.tools import *
import NAME

# Define setup() method
def setup():
    print "SETUP!"

# Define teardown() method
def teardown():
    print "TEAR DOWN!"

# Define test_basic() method
def test_basic():
    print "I RAN!"
