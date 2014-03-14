from nose.tools import *
from ADS_Utilities.pec import SpecificCondition, PecRec, PecRecSeq


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


class TestPecRec():

    def setup(self):
        self.record = PecRec('  1 18  0  0  0  0  0  0  0  0  0    0    0'
                             '    0    01996199828 55  2AUN1474-41013    N '
                             '^C:BASE MODEL - ESI - w/FRONT DISC BRAKES')

    def teardown(self):
        self.record = None

    def test_pecrec_init(self):
        assert_equal(self.record.make, '1')
        assert_equal(self.record.model_1, '18')
        assert_equal(self.record.model_2, '0')
        assert_equal(self.record.model_3, '0')
        assert_equal(self.record.model_4, '0')
        assert_equal(self.record.model_5, '0')
        assert_equal(self.record.model_6, '0')
        assert_equal(self.record.engine_1, '0')
        assert_equal(self.record.engine_2, '0')
        assert_equal(self.record.engine_3, '0')
        assert_equal(self.record.engine_4, '0')
        assert_equal(self.record.spec_1.or_value, ' ')
        assert_equal(self.record.spec_1.x_value, ' ')
        assert_equal(self.record.spec_1.code, '0')
        assert_equal(self.record.spec_2.or_value, ' ')
        assert_equal(self.record.spec_2.x_value, ' ')
        assert_equal(self.record.spec_2.code, '0')
        assert_equal(self.record.spec_3.or_value, ' ')
        assert_equal(self.record.spec_3.x_value, ' ')
        assert_equal(self.record.spec_3.code, '0')
        assert_equal(self.record.spec_4.or_value, ' ')
        assert_equal(self.record.spec_4.x_value, ' ')
        assert_equal(self.record.spec_4.code, '0')
        assert_equal(self.record.from_year, 1996)
        assert_equal(self.record.to_year, 1998)
        assert_equal(self.record.group, '28')
        assert_equal(self.record.pd, '55')
        assert_equal(self.record.pcq, '2')
        assert_equal(self.record.lc, 'AUN')
        assert_equal(self.record.pn, '1474-41013')
        assert_equal(self.record.block_flag, 'N')
        assert_equal(self.record.flag, ' ')
        assert_equal(self.record.comment, '^C:BASE MODEL - ESI - w/FRONT '
                                          'DISC BRAKES')

    def test_pecrec_str(self):
        assert_equal(str(self.record), '  1 18  0  0  0  0  0  0  0  0  0'
                                       '    0    0    0    01996199828 55  2'
                                       'AUN1474-41013    N ^C:BASE MODEL - '
                                       'ESI - w/FRONT DISC BRAKES')


class TestPecRecSeq():

    def setup(self):
        self.record = PecRecSeq('  1 18  0  0  0  0  0  0  0  0  0    0    0'
                                '    0    01996199828 55  2AUN1474-41013    N'
                                ' ^C:BASE MODEL - ESI - w/FRONT DISC BRAKES'
                                '^C:***    1/1900     ***')

    def teardown(self):
        self.record = None

    def test_pecrecseq_init(self):
        assert_equal(self.record.make, '1')
        assert_equal(self.record.model_1, '18')
        assert_equal(self.record.model_2, '0')
        assert_equal(self.record.model_3, '0')
        assert_equal(self.record.model_4, '0')
        assert_equal(self.record.model_5, '0')
        assert_equal(self.record.model_6, '0')
        assert_equal(self.record.engine_1, '0')
        assert_equal(self.record.engine_2, '0')
        assert_equal(self.record.engine_3, '0')
        assert_equal(self.record.engine_4, '0')
        assert_equal(self.record.spec_1.or_value, ' ')
        assert_equal(self.record.spec_1.x_value, ' ')
        assert_equal(self.record.spec_1.code, '0')
        assert_equal(self.record.spec_2.or_value, ' ')
        assert_equal(self.record.spec_2.x_value, ' ')
        assert_equal(self.record.spec_2.code, '0')
        assert_equal(self.record.spec_3.or_value, ' ')
        assert_equal(self.record.spec_3.x_value, ' ')
        assert_equal(self.record.spec_3.code, '0')
        assert_equal(self.record.spec_4.or_value, ' ')
        assert_equal(self.record.spec_4.x_value, ' ')
        assert_equal(self.record.spec_4.code, '0')
        assert_equal(self.record.from_year, 1996)
        assert_equal(self.record.to_year, 1998)
        assert_equal(self.record.group, '28')
        assert_equal(self.record.pd, '55')
        assert_equal(self.record.pcq, '2')
        assert_equal(self.record.lc, 'AUN')
        assert_equal(self.record.pn, '1474-41013')
        assert_equal(self.record.block_flag, 'N')
        assert_equal(self.record.flag, ' ')
        assert_equal(self.record.comment, '^C:BASE MODEL - ESI - w/FRONT '
                                          'DISC BRAKES')
        assert_equal(self.record.sequence, '1/1900')

    def test_format_sequence(self):
        assert_equal(self.record.format_sequence(), '^C:***    1/1900     ***')

    def test_pecrecseq_str(self):
        assert_equal(str(self.record), '  1 18  0  0  0  0  0  0  0  0  0'
                                       '    0    0    0    01996199828 55  2'
                                       'AUN1474-41013    N ^C:BASE MODEL - '
                                       'ESI - w/FRONT DISC BRAKES'
                                       '^C:***    1/1900     ***')
