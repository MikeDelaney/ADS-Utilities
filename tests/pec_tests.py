from nose.tools import *
from ADS_Utilities.pec import SpecificCondition


def setup():
    print "SETUP!"


def teardown():
    print "TEAR DOWN!"


def test_specific_condition_init():
    spec1 = SpecificCondition()
    spec2 = SpecificCondition(' X168')
    assert_equal(spec1.or_value, ' ')
    assert_equal(spec1.x_value, ' ')
    assert_equal(spec1.code, '0')
    assert_equal(spec2.or_value, ' ')
    assert_equal(spec2.x_value, 'X')
    assert_equal(spec2.code, '168')


def test_specific_condition_str():
    spec = SpecificCondition(' X168')
    assert_equal(str(spec), ' X168')