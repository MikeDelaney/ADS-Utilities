from nose.tools import *
from ADS_Utilities.pec import SpecificCondition, PecRec, PecRecSeq


class TestSpecificCondition():

    def setup(self):
        self.spec = SpecificCondition(' X168')

    def teardown(self):
        self.spec = None

    def test_specific_condition_or_value_init(self):
        assert_equal(self.spec.or_value, ' ')

    def test_specific_condition_x_value_init(self):
        assert_equal(self.spec.x_value, 'X')

    def test_specific_condition_code_init(self):
        assert_equal(self.spec.code, '168')

    def test_specific_condition_str(self):
        assert_equal(str(self.spec), ' X168')


class TestPecRec():

    def setup(self):
        self.record = PecRec('  1 18  0  0  0  0  0  0  0  0  0    0    0'
                             '    0    01996199828 55  2AUN1474-41013    N '
                             '^C:BASE MODEL - ESI - w/FRONT DISC BRAKES')

    def teardown(self):
        self.record = None

    def test_pecrec_make_init(self):
        assert_equal(self.record.make, '1')

    def test_pecrec_model_1_init(self):
        assert_equal(self.record.model_1, '18')

    def test_pecrec_model_2_init(self):
        assert_equal(self.record.model_2, '0')

    def test_pecrec_model_3_init(self):
        assert_equal(self.record.model_3, '0')

    def test_pecrec_model_4_init(self):
        assert_equal(self.record.model_4, '0')

    def test_pecrec_model_5_init(self):
        assert_equal(self.record.model_5, '0')

    def test_pecrec_model_6_init(self):
        assert_equal(self.record.model_6, '0')

    def test_pecrec_engine_1_init(self):
        assert_equal(self.record.engine_1, '0')

    def test_pecrec_engine_2_init(self):
        assert_equal(self.record.engine_2, '0')

    def test_pecrec_engine_3_init(self):
        assert_equal(self.record.engine_3, '0')

    def test_pecrec_engine_4_init(self):
        assert_equal(self.record.engine_4, '0')

    def test_pecrec_spec_1_or_value_init(self):
        assert_equal(self.record.spec_1.or_value, ' ')

    def test_pecrec_spec_1_x_value_init(self):
        assert_equal(self.record.spec_1.x_value, ' ')

    def test_pecrec_spec_1_code_init(self):
        assert_equal(self.record.spec_1.code, '0')

    def test_pecrec_spec_2_or_value_init(self):
        assert_equal(self.record.spec_2.or_value, ' ')

    def test_pecrec_spec_2_x_value_init(self):
        assert_equal(self.record.spec_2.x_value, ' ')

    def test_pecrec_spec_2_code_init(self):
        assert_equal(self.record.spec_2.code, '0')

    def test_pecrec_spec_3_or_value_init(self):
        assert_equal(self.record.spec_3.or_value, ' ')

    def test_pecrec_spec_3_x_value_init(self):
        assert_equal(self.record.spec_3.x_value, ' ')

    def test_pecrec_spec_3_code_init(self):
        assert_equal(self.record.spec_3.code, '0')

    def test_pecrec_spec_4_or_value_init(self):
        assert_equal(self.record.spec_4.or_value, ' ')

    def test_pecrec_spec_4_x_value_init(self):
        assert_equal(self.record.spec_4.x_value, ' ')

    def test_pecrec_spec_4_code_init(self):
        assert_equal(self.record.spec_4.code, '0')

    def test_pecrec_from_year_init(self):
        assert_equal(self.record.from_year, 1996)

    def test_pecrec_to_year_init(self):
        assert_equal(self.record.to_year, 1998)

    def test_pecrec_group_init(self):
        assert_equal(self.record.group, '28')

    def test_pecrec_pd_init(self):
        assert_equal(self.record.pd, '55')

    def test_pecrec_pcq_init(self):
        assert_equal(self.record.pcq, '2')

    def test_pecrec_lc_init(self):
        assert_equal(self.record.lc, 'AUN')

    def test_pecrec_pn_init(self):
        assert_equal(self.record.pn, '1474-41013')

    def test_pecrec_block_flag_init(self):
        assert_equal(self.record.block_flag, 'N')

    def test_pecrec_flag_init(self):
        assert_equal(self.record.flag, ' ')

    def test_pecrec_comment_init(self):
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

    def test_pecrecseq_make_init(self):
        assert_equal(self.record.make, '1')

    def test_pecrecseq_model_1_init(self):
        assert_equal(self.record.model_1, '18')

    def test_pecrecseq_model_2_init(self):
        assert_equal(self.record.model_2, '0')

    def test_pecrecseq_model_3_init(self):
        assert_equal(self.record.model_3, '0')

    def test_pecrecseq_model_4_init(self):
        assert_equal(self.record.model_4, '0')

    def test_pecrecseq_model_5_init(self):
        assert_equal(self.record.model_5, '0')

    def test_pecrecseq_model_6_init(self):
        assert_equal(self.record.model_6, '0')

    def test_pecrecseq_engine_1_init(self):
        assert_equal(self.record.engine_1, '0')

    def test_pecrecseq_engine_2_init(self):
        assert_equal(self.record.engine_2, '0')

    def test_pecrecseq_engine_3_init(self):
        assert_equal(self.record.engine_3, '0')

    def test_pecrecseq_engine_4_init(self):
        assert_equal(self.record.engine_4, '0')

    def test_pecrecseq_spec_1_or_value_init(self):
        assert_equal(self.record.spec_1.or_value, ' ')

    def test_pecrecseq_spec_1_x_value_init(self):
        assert_equal(self.record.spec_1.x_value, ' ')

    def test_pecrecseq_spec_1_code_init(self):
        assert_equal(self.record.spec_1.code, '0')

    def test_pecrecseq_spec_2_or_value_init(self):
        assert_equal(self.record.spec_2.or_value, ' ')

    def test_pecrecseq_spec_2_x_value_init(self):
        assert_equal(self.record.spec_2.x_value, ' ')

    def test_pecrecseq_spec_2_code_init(self):
        assert_equal(self.record.spec_2.code, '0')

    def test_pecrecseq_spec_3_or_value_init(self):
        assert_equal(self.record.spec_3.or_value, ' ')

    def test_pecrecseq_spec_3_x_value_init(self):
        assert_equal(self.record.spec_3.x_value, ' ')

    def test_pecrecseq_spec_3_code_init(self):
        assert_equal(self.record.spec_3.code, '0')

    def test_pecrecseq_spec_4_or_value_init(self):
        assert_equal(self.record.spec_4.or_value, ' ')

    def test_pecrecseq_spec_4_x_value_init(self):
        assert_equal(self.record.spec_4.x_value, ' ')

    def test_pecrecseq_spec_4_code_init(self):
        assert_equal(self.record.spec_4.code, '0')

    def test_pecrecseq_from_year_init(self):
        assert_equal(self.record.from_year, 1996)

    def test_pecrecseq_to_year_init(self):
        assert_equal(self.record.to_year, 1998)

    def test_pecrecseq_group_init(self):
        assert_equal(self.record.group, '28')

    def test_pecrecseq_pd_init(self):
        assert_equal(self.record.pd, '55')

    def test_pecrecseq_pcq_init(self):
        assert_equal(self.record.pcq, '2')

    def test_pecrecseq_lc_init(self):
        assert_equal(self.record.lc, 'AUN')

    def test_pecrecseq_pn_init(self):
        assert_equal(self.record.pn, '1474-41013')

    def test_pecrecseq_block_flag_init(self):
        assert_equal(self.record.block_flag, 'N')

    def test_pecrecseq_flag_init(self):
        assert_equal(self.record.flag, ' ')

    def test_pecrecseq_comment_init(self):
        assert_equal(self.record.comment, '^C:BASE MODEL - ESI - w/FRONT '
                                          'DISC BRAKES')

    def test_pecrecseq_sequence_init(self):
        assert_equal(self.record.sequence, '1/1900')

    def test_format_sequence(self):
        assert_equal(self.record.format_sequence(), '^C:***    1/1900     ***')

    def test_pecrecseq_str(self):
        assert_equal(str(self.record), '  1 18  0  0  0  0  0  0  0  0  0'
                                       '    0    0    0    01996199828 55  2'
                                       'AUN1474-41013    N ^C:BASE MODEL - '
                                       'ESI - w/FRONT DISC BRAKES'
                                       '^C:***    1/1900     ***')
