from nose.tools import *
from ADS_Utilities.dup_over_rpt import DupOverRecord, DupOverRecDelete

__author__ = 'michael.delaney'


class TestDupOverRecord():
    def setup(self):
        self.record = DupOverRecord(['1', '1', 'AMC-EAGLE', '1993', '1994',
                                     '18', 'TALON', '0', '', '0', '',
                                     '4 WHEEL/ALL WHEEL DRIVE', '28',
                                     'F BRK HYDRAULICS', '55',
                                     'Front Brake Hose', '1474-40300', '2',
                                     'AUN', 'N', '0', '0', '',
                                     'INNER - TSI - AWD', '16', 'miked',
                                     '08-OCT-13', '1', '1 0001600', ''])

    def teardown(self):
        self.record = None

    def test_dupoverrecord_init(self):
        assert_equal(self.record.rec_num, '1')
        assert_equal(self.record.make_id, '1')
        assert_equal(self.record.make_text, 'AMC-EAGLE')
        assert_equal(self.record.from_year, '1993')
        assert_equal(self.record.to_year, '1994')
        assert_equal(self.record.model_id, '18')
        assert_equal(self.record.model_text, 'TALON')
        assert_equal(self.record.submodel_id, '0')
        assert_equal(self.record.submodel_text, '')
        assert_equal(self.record.engine_id, '0')
        assert_equal(self.record.engine_text, '')
        assert_equal(self.record.attrs, '4 WHEEL/ALL WHEEL DRIVE')
        assert_equal(self.record.part_group_id, '28')
        assert_equal(self.record.part_group_text, 'F BRK HYDRAULICS')
        assert_equal(self.record.part_descr_id, '55')
        assert_equal(self.record.part_descr_text, 'Front Brake Hose')
        assert_equal(self.record.part_num, '1474-40300')
        assert_equal(self.record.per_car_qty, '2')
        assert_equal(self.record.cat_line_cd, 'AUN')
        assert_equal(self.record.block_cd, 'N')
        assert_equal(self.record.block_num, '0')
        assert_equal(self.record.block_seq_num, '0')
        assert_equal(self.record.flag, '')
        assert_equal(self.record.comment_text, 'INNER - TSI - AWD')
        assert_equal(self.record.cde2_id, '16')
        assert_equal(self.record.modified_user, 'miked')
        assert_equal(self.record.modified_date, '08-OCT-13')
        assert_equal(self.record.grouping_id, '1')
        assert_equal(self.record.cde_page_seq_num, '1 0001600')
        assert_equal(self.record.pec_seq_num, '1/1600')
        assert_equal(self.record.filters_and_options, '')


class TestDupOverRecDelete():
    def setup(self):
        self.record = DupOverRecDelete(['1', '1', 'AMC-EAGLE', '1993', '1994',
                                        '18', 'TALON', '0', '', '0', '',
                                        '4 WHEEL/ALL WHEEL DRIVE', '28',
                                        'F BRK HYDRAULICS', '55',
                                        'Front Brake Hose', '1474-40300', '2',
                                        'AUN', 'N', '0', '0', '',
                                        'INNER - TSI - AWD', '16', 'miked',
                                        '08-OCT-13', '1', '1 0001600', '',
                                        'Y'])

    def teardown(self):
        self.record = None

    def test_dupoverrecdelete_init(self):
        assert_equal(self.record.rec_num, '1')
        assert_equal(self.record.make_id, '1')
        assert_equal(self.record.make_text, 'AMC-EAGLE')
        assert_equal(self.record.from_year, '1993')
        assert_equal(self.record.to_year, '1994')
        assert_equal(self.record.model_id, '18')
        assert_equal(self.record.model_text, 'TALON')
        assert_equal(self.record.submodel_id, '0')
        assert_equal(self.record.submodel_text, '')
        assert_equal(self.record.engine_id, '0')
        assert_equal(self.record.engine_text, '')
        assert_equal(self.record.attrs, '4 WHEEL/ALL WHEEL DRIVE')
        assert_equal(self.record.part_group_id, '28')
        assert_equal(self.record.part_group_text, 'F BRK HYDRAULICS')
        assert_equal(self.record.part_descr_id, '55')
        assert_equal(self.record.part_descr_text, 'Front Brake Hose')
        assert_equal(self.record.part_num, '1474-40300')
        assert_equal(self.record.per_car_qty, '2')
        assert_equal(self.record.cat_line_cd, 'AUN')
        assert_equal(self.record.block_cd, 'N')
        assert_equal(self.record.block_num, '0')
        assert_equal(self.record.block_seq_num, '0')
        assert_equal(self.record.flag, '')
        assert_equal(self.record.comment_text, 'INNER - TSI - AWD')
        assert_equal(self.record.cde2_id, '16')
        assert_equal(self.record.modified_user, 'miked')
        assert_equal(self.record.modified_date, '08-OCT-13')
        assert_equal(self.record.grouping_id, '1')
        assert_equal(self.record.cde_page_seq_num, '1 0001600')
        assert_equal(self.record.pec_seq_num, '1/1600')
        assert_equal(self.record.filters_and_options, '')
        assert_equal(self.record.delete, 'Y')
