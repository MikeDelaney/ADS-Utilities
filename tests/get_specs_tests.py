from nose.tools import *
import ADS_Utilities.get_specs
import mock

__author__ = 'michael.delaney'


def test_spec_to_val():
    ADS_Utilities.get_specs.get_rows = mock.Mock(return_value=[(u'1 BBL', 1),
                                                               (u'2 BBL', 2)])
    assert_equal([(u'1 BBL', 1), (u'2 BBL', 2)],
                 ADS_Utilities.get_specs.get_rows())
    assert_equal(ADS_Utilities.get_specs.spec_txt_to_val(),
                 {u'1 BBL': 1, u'2 BBL': 2})
