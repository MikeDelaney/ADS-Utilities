from nose.tools import *
from ADS_Utilities.pec import SpecificCondition, PecRec


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


def test_pecrec_init():
    record = PecRec('  1 18  0  0  0  0  0  0  0  0  0    0    0    0    0'
                    '1996199828 55  2AUN1474-41013    N ^C:BASE MODEL - ESI'
                    ' - w/FRONT DISC BRAKES')
    assert_equal(record.make, '1')
    assert_equal(record.model_1, '18')
    assert_equal(record.model_2, '0')
    assert_equal(record.model_3, '0')
    assert_equal(record.model_4, '0')
    assert_equal(record.model_5, '0')
    assert_equal(record.model_6, '0')
    assert_equal(record.engine_1, '0')
    assert_equal(record.engine_2, '0')
    assert_equal(record.engine_3, '0')
    assert_equal(record.engine_4, '0')
    assert_equal(record.spec_1.or_value, ' ')
    assert_equal(record.spec_1.x_value, ' ')
    assert_equal(record.spec_1.code, '0')
    assert_equal(record.spec_2.or_value, ' ')
    assert_equal(record.spec_2.x_value, ' ')
    assert_equal(record.spec_2.code, '0')
    assert_equal(record.spec_3.or_value, ' ')
    assert_equal(record.spec_3.x_value, ' ')
    assert_equal(record.spec_3.code, '0')
    assert_equal(record.spec_4.or_value, ' ')
    assert_equal(record.spec_4.x_value, ' ')
    assert_equal(record.spec_4.code, '0')
    assert_equal(record.from_year, 1996)
    assert_equal(record.to_year, 1998)
    assert_equal(record.group, '28')
    assert_equal(record.pd, '55')
    assert_equal(record.pcq, '2')
    assert_equal(record.lc, 'AUN')
    assert_equal(record.pn, '1474-41013')
    assert_equal(record.block_flag, 'N')
    assert_equal(record.flag, ' ')
    assert_equal(record.comment, '^C:BASE MODEL - ESI - w/FRONT DISC BRAKES')

def test_pecrec_str():
    record = PecRec('  1 18  0  0  0  0  0  0  0  0  0    0    0    0    0'
                    '1996199828 55  2AUN1474-41013    N ^C:BASE MODEL - ESI'
                    ' - w/FRONT DISC BRAKES')
    assert_equal(str(record), '  1 18  0  0  0  0  0  0  0  0  0    0    0   '
                              ' 0    01996199828 55  2AUN1474-41013    N '
                              '^C:BASE MODEL - ESI - w/FRONT DISC BRAKES')
