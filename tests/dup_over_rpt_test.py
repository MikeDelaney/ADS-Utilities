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

    def test_rec_num_init(self):
        assert_equal(self.record.rec_num, '1')

    def test_make_id_init(self):
        assert_equal(self.record.make_id, '1')

    def test_make_text_init(self):
        assert_equal(self.record.make_text, 'AMC-EAGLE')

    def test_from_year_init(self):
        assert_equal(self.record.from_year, '1993')

    def test_to_year_init(self):
        assert_equal(self.record.to_year, '1994')

    def test_model_id_init(self):
        assert_equal(self.record.model_id, '18')

    def test_model_text_init(self):
        assert_equal(self.record.model_text, 'TALON')

    def test_submodel_id_init(self):
        assert_equal(self.record.submodel_id, '0')

    def test_submodel_text_init(self):
        assert_equal(self.record.submodel_text, '')

    def test_engine_id_init(self):
        assert_equal(self.record.engine_id, '0')

    def test_engine_text_init(self):
        assert_equal(self.record.engine_text, '')

    def test_attrs_init(self):
        assert_equal(self.record.attrs, '4 WHEEL/ALL WHEEL DRIVE')

    def test_part_group_id_init(self):
        assert_equal(self.record.part_group_id, '28')

    def test_part_group_text_init(self):
        assert_equal(self.record.part_group_text, 'F BRK HYDRAULICS')

    def test_part_descr_id_init(self):
        assert_equal(self.record.part_descr_id, '55')

    def test_part_descr_text_init(self):
        assert_equal(self.record.part_descr_text, 'Front Brake Hose')

    def test_part_num_init(self):
        assert_equal(self.record.part_num, '1474-40300')

    def test_per_car_qty_init(self):
        assert_equal(self.record.per_car_qty, '2')

    def test_cat_line_cd_init(self):
        assert_equal(self.record.cat_line_cd, 'AUN')

    def test_block_cd_init(self):
        assert_equal(self.record.block_cd, 'N')

    def test_block_num_init(self):
        assert_equal(self.record.block_num, '0')

    def test_block_seq_num_init(self):
        assert_equal(self.record.block_seq_num, '0')

    def test_flag_init(self):
        assert_equal(self.record.flag, '')

    def test_comment_text_init(self):
        assert_equal(self.record.comment_text, 'INNER - TSI - AWD')

    def test_cde2_id_init(self):
        assert_equal(self.record.cde2_id, '16')

    def test_modified_user_init(self):
        assert_equal(self.record.modified_user, 'miked')

    def test_modified_date_init(self):
        assert_equal(self.record.modified_date, '08-OCT-13')

    def test_grouping_id_init(self):
        assert_equal(self.record.grouping_id, '1')

    def test_cde_page_seq_num_init(self):
        assert_equal(self.record.cde_page_seq_num, '1 0001600')

    def test_pec_seq_num_init(self):
        assert_equal(self.record.pec_seq_num, '1/1600')

    def test_filters_and_options_init(self):
        assert_equal(self.record.filters_and_options, '')

    def test_dupoverrecord_str(self):
        assert_equal(str(self.record), '1, 1, AMC-EAGLE, 1993, 1994, 18, '
                                       'TALON, 0, , 0, , 4 WHEEL/ALL WHEEL '
                                       'DRIVE, 28, F BRK HYDRAULICS, 55, '
                                       'Front Brake Hose, 1474-40300, 2, AUN, '
                                       'N, 0, 0, , INNER - TSI - AWD, 16, '
                                       'miked, 08-OCT-13, 1, 1 0001600, ')


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

    def test_rec_num_init(self):
        assert_equal(self.record.rec_num, '1')

    def test_make_id_init(self):
        assert_equal(self.record.make_id, '1')

    def test_make_text_init(self):
        assert_equal(self.record.make_text, 'AMC-EAGLE')

    def test_from_year_init(self):
        assert_equal(self.record.from_year, '1993')

    def test_to_year_init(self):
        assert_equal(self.record.to_year, '1994')

    def test_model_id_init(self):
        assert_equal(self.record.model_id, '18')

    def test_model_text_init(self):
        assert_equal(self.record.model_text, 'TALON')

    def test_submodel_id_init(self):
        assert_equal(self.record.submodel_id, '0')

    def test_submodel_text_init(self):
        assert_equal(self.record.submodel_text, '')

    def test_engine_id_init(self):
        assert_equal(self.record.engine_id, '0')

    def test_engine_text_init(self):
        assert_equal(self.record.engine_text, '')

    def test_attrs_init(self):
        assert_equal(self.record.attrs, '4 WHEEL/ALL WHEEL DRIVE')

    def test_part_group_id_init(self):
        assert_equal(self.record.part_group_id, '28')

    def test_part_group_text_init(self):
        assert_equal(self.record.part_group_text, 'F BRK HYDRAULICS')

    def test_part_descr_id_init(self):
        assert_equal(self.record.part_descr_id, '55')

    def test_part_descr_text_init(self):
        assert_equal(self.record.part_descr_text, 'Front Brake Hose')

    def test_part_num_init(self):
        assert_equal(self.record.part_num, '1474-40300')

    def test_per_car_qty_init(self):
        assert_equal(self.record.per_car_qty, '2')

    def test_cat_line_cd_init(self):
        assert_equal(self.record.cat_line_cd, 'AUN')

    def test_block_cd_init(self):
        assert_equal(self.record.block_cd, 'N')

    def test_block_num_init(self):
        assert_equal(self.record.block_num, '0')

    def test_block_seq_num_init(self):
        assert_equal(self.record.block_seq_num, '0')

    def test_flag_init(self):
        assert_equal(self.record.flag, '')

    def test_comment_text_init(self):
        assert_equal(self.record.comment_text, 'INNER - TSI - AWD')

    def test_cde2_id_init(self):
        assert_equal(self.record.cde2_id, '16')

    def test_modified_user_init(self):
        assert_equal(self.record.modified_user, 'miked')

    def test_modified_date_init(self):
        assert_equal(self.record.modified_date, '08-OCT-13')

    def test_grouping_id_init(self):
        assert_equal(self.record.grouping_id, '1')

    def test_cde_page_seq_num_init(self):
        assert_equal(self.record.cde_page_seq_num, '1 0001600')

    def test_pec_seq_num_init(self):
        assert_equal(self.record.pec_seq_num, '1/1600')

    def test_filters_and_options_init(self):
        assert_equal(self.record.filters_and_options, '')

    def test_delete_init(self):
        assert_equal(self.record.delete, 'Y')

    def test_dupoverrecdelete_str(self):
        assert_equal(str(self.record), '1, 1, AMC-EAGLE, 1993, 1994, 18, '
                                       'TALON, 0, , 0, , 4 WHEEL/ALL WHEEL '
                                       'DRIVE, 28, F BRK HYDRAULICS, 55, '
                                       'Front Brake Hose, 1474-40300, 2, AUN, '
                                       'N, 0, 0, , INNER - TSI - AWD, 16, '
                                       'miked, 08-OCT-13, 1, 1 0001600, , Y')
