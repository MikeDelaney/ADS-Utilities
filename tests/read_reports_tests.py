from nose.tools import *
from ADS_Utilities.read_reports import load_dupes_overlaps, get_column_indexes
from ADS_Utilities.dup_over_rpt import DupOverRecord, DupOverRecDelete
import StringIO

__author__ = 'miked'

class TestLoadDupesOverlaps():

    def setup(self):
        assert_equal.im_class.maxDiff = None
        header = ['REP_REC_ID', 'MAKE_ID', 'MAKE_TXT', 'FROM_YEAR',
                  'TO_YEAR', 'MODEL_ID', 'MODEL_TXT', 'SUBMODEL_ID',
                  'SUBMODEL_TXT', 'ENGINE_ID', 'ENGINE_TXT', 'ATTRS',
                  'PART_GROUP_ID', 'PART_GROUP_TXT', 'PART_DESCR_ID',
                  'PART_DESCR_TXT', 'PART_NUM', 'PER_CAR_QTY', 'CAT_LINE_CD',
                  'BLOCK_CD', 'BLOCK_NUM', 'BLOCK_SEQ_NUM', 'FLAG',
                  'COMMENT_TXT', 'CDE2_ID', 'MODIFIED_USER', 'MODIFIED_DATE',
                  'GROUPING_ID', 'CDE_PAGE_SEQ_NUM', 'FILTERS_AND_OPTIONS']
        self.r1 = ['1', '6', 'CHRYSLER', '2005', '2008', '33', '300 Series',
                   '0', '', '0', '', '', '27',
                   'F BRK PADS/SHOES,ROTORS/DRUMS', '30',
                   'Front Disc Brake Rotor', '100-53023', '2', 'IWE', 'N',
                   '0', '0', '',
                   'ROTOQUIET - C - 5-115MM (HOLE-BOLT CIRCLE) VENTED DISC',
                   '278', 'MIKED', '21-Nov-13', '1', '6 0002000', '']
        self.r2 = ['2', '6', 'CHRYSLER', '2005', '2008', '33', '300 Series',
                   '0', '', '0', '', '4 WHEEL/ALL WHEEL DRIVE', '27',
                   'F BRK PADS/SHOES,ROTORS/DRUMS', '30',
                   'Front Disc Brake Rotor', '100-53023', '2', 'IWE', 'N',
                   '0', '0', '',
                   'ROTOQUIET - LIMITED - TOURING - AWD - 5-115MM (HOLE-BOLT '
                   'CIRCLE) VENTED DISC',
                   '286', 'MIKED', '21-Nov-13', '1', '6 0002200', '']
        self.r3 = ['4', '6', 'CHRYSLER', '2005', '2008', '33', '300 Series',
                   '0', '', '0', '', '', '30',
                   'R BRK PADS/SHOES,ROTORS/DRUMS', '30',
                   'Rear Disc Brake Rotor', '100-53024', '2', 'IWE', 'N',
                   '0', '0', '',
                   'ROTOQUIET - C - 5-115MM (HOLE-BOLT CIRCLE) VENTED DISC',
                   '279', 'MIKED', '21-Nov-13', '2', '6 0005600', '']
        self.r4 = ['5', '6', 'CHRYSLER', '2005', '2008', '33', '300 Series',
                   '0', '', '0', '', '4 WHEEL/ALL WHEEL DRIVE', '30',
                   'R BRK PADS/SHOES,ROTORS/DRUMS', '30',
                   'Rear Disc Brake Rotor', '100-53024', '2', 'IWE', 'N', '0',
                   '0', '',
                   'ROTOQUIET - LIMITED - TOURING - AWD - 5-115MM (HOLE-BOLT '
                   'CIRCLE) VENTED DISC',
                   '287', 'MIKED', '21-Nov-13', '2', '6 0005700', '']
        self.r5 = ['5', '6', 'CHRYSLER', '2005', '2008', '33', '300 Series',
                   '0', '', '0', '', '4 WHEEL/ALL WHEEL DRIVE', '30',
                   'R BRK PADS/SHOES,ROTORS/DRUMS', '30',
                   'Rear Disc Brake Rotor', '100-53024', '2', 'IWE', 'N', '0',
                   '0', '',
                   'ROTOQUIET - EXTRA RECORD',
                   '287', 'MIKED', '21-Nov-13', '2', '6 0005700', '']
        separator = ['6', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                     '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                     '-', '-', '-', '-', '-', '-', '-', '']
        filter_rec = ['', '', '', '', '', '', '', '', '', '', '', '', '', '',
                      '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                      '', 'Makes:  (all)']

        header_reordered = header[:]
        header_reordered.insert(1, header_reordered.pop(28))
        header_delete = header[:]
        header_delete.append('DELETE')
        header_delete_reordered = header_delete[:]
        header_delete_reordered.insert(1, header_delete_reordered.pop(28))
        header_delete_reordered.insert(2, header_delete_reordered.pop())

        r1_reordered = self.r1[:]
        r1_reordered.insert(1, r1_reordered.pop(28))
        self.r1_delete = self.r1[:]
        self.r1_delete.append('Y')
        r1_delete_reordered = self.r1_delete[:]
        r1_delete_reordered.insert(1, r1_delete_reordered.pop(28))
        r1_delete_reordered.insert(2, r1_delete_reordered.pop())

        r2_reordered = self.r2[:]
        r2_reordered.insert(1, r2_reordered.pop(28))
        self.r2_delete = self.r2[:]
        self.r2_delete.append('')
        r2_delete_reordered = self.r2_delete[:]
        r2_delete_reordered.insert(1, r2_delete_reordered.pop(28))
        r2_delete_reordered.insert(2, r2_delete_reordered.pop())

        r3_reordered = self.r3[:]
        r3_reordered.insert(1, r3_reordered.pop(28))
        self.r3_delete = self.r3[:]
        self.r3_delete.append('')
        r3_delete_reordered = self.r3_delete[:]
        r3_delete_reordered.insert(1, r3_delete_reordered.pop(28))
        r3_delete_reordered.insert(2, r3_delete_reordered.pop())

        r4_reordered = self.r4[:]
        r4_reordered.insert(1, r4_reordered.pop(28))
        self.r4_delete = self.r4[:]
        self.r4_delete.append('Y')
        r4_delete_reordered = self.r4_delete[:]
        r4_delete_reordered.insert(1, r4_delete_reordered.pop(28))
        r4_delete_reordered.insert(2, r4_delete_reordered.pop())

        r5_reordered = self.r5[:]
        r5_reordered.insert(1, r5_reordered.pop(28))
        self.r5_delete = self.r5[:]
        self.r5_delete.append('')
        r5_delete_reordered = self.r5_delete[:]
        r5_delete_reordered.insert(1, r5_delete_reordered.pop(28))
        r5_delete_reordered.insert(2, r5_delete_reordered.pop())

        separator_delete = separator[:]
        separator_delete.append('')
        separator_delete_reordered = separator_delete[:]
        separator_delete_reordered.insert(2, separator_delete_reordered.pop())

        filter_rec_delete = filter_rec[:]
        filter_rec_delete.append('')
        filter_rec_delete_reordered = filter_rec_delete[:]
        filter_rec_delete_reordered.insert(2, filter_rec_delete_reordered.pop())

        self.report_1 = StringIO.StringIO('\t'.join(header) + '\n' +
                                          '\t'.join(self.r1) + '\n' +
                                          '\t'.join(self.r2) + '\n' +
                                          '\t'.join(separator) + '\n' +
                                          '\t'.join(self.r3) + '\n' +
                                          '\t'.join(self.r4) + '\n' +
                                          '\t'.join(self.r5) + '\n' +
                                          '\t'.join(filter_rec) + '\n')
        self.report_2 = StringIO.StringIO('\t'.join(header_reordered) + '\n' +
                                          '\t'.join(r1_reordered) + '\n' +
                                          '\t'.join(r2_reordered) + '\n' +
                                          '\t'.join(separator) + '\n' +
                                          '\t'.join(r3_reordered) + '\n' +
                                          '\t'.join(r4_reordered) + '\n' +
                                          '\t'.join(r5_reordered) + '\n' +
                                          '\t'.join(filter_rec) + '\n')
        self.report_3 = StringIO.StringIO('\t'.join(header_delete) + '\n' +
                                          '\t'.join(self.r1_delete) + '\n' +
                                          '\t'.join(self.r2_delete) + '\n' +
                                          '\t'.join(separator_delete) + '\n' +
                                          '\t'.join(self.r3_delete) + '\n' +
                                          '\t'.join(self.r4_delete) + '\n' +
                                          '\t'.join(self.r5_delete) + '\n' +
                                          '\t'.join(filter_rec_delete) + '\n')
        self.report_4 = StringIO.StringIO('\t'.join(header_delete_reordered) +
                                          '\n' +
                                          '\t'.join(r1_delete_reordered) +
                                          '\n' +
                                          '\t'.join(r2_delete_reordered) +
                                          '\n' +
                                          '\t'.join(separator_delete_reordered)
                                          + '\n' +
                                          '\t'.join(r3_delete_reordered) +
                                          '\n' +
                                          '\t'.join(r4_delete_reordered) +
                                          '\n' +
                                          '\t'.join(r5_delete_reordered) +
                                          '\n' +
                                          '\t'.join(filter_rec_delete_reordered)
                                          + '\n')

    def teardown(self):
        self.report_1 = None
        self.report_2 = None
        self.report_3 = None
        self.report_4 = None
        self.r1 = None
        self.r2 = None
        self.r3 = None
        self.r4 = None
        self.r5 = None
        self.r1_delete = None
        self.r2_delete = None
        self.r3_delete = None
        self.r4_delete = None
        self.r5_delete = None

    def test_load_default(self):
        assert_items_equal(load_dupes_overlaps(self.report_1),
                           {'6/2000': DupOverRecord(self.r1),
                            '6/2200': DupOverRecord(self.r2),
                            '6/5600': DupOverRecord(self.r3),
                            '6/5700': [DupOverRecord(self.r4),
                                       DupOverRecord(self.r5)]})

    def test_load_default_reordered(self):
        assert_items_equal(load_dupes_overlaps(self.report_2),
                           {'6/2000': DupOverRecord(self.r1),
                            '6/2200': DupOverRecord(self.r2),
                            '6/5600': DupOverRecord(self.r3),
                            '6/5700': [DupOverRecord(self.r4),
                                       DupOverRecord(self.r5)]})

    def test_load_delete(self):
        assert_items_equal(load_dupes_overlaps(self.report_3),
                           {'6/2000': DupOverRecDelete(self.r1_delete),
                            '6/2200': DupOverRecDelete(self.r2_delete),
                            '6/5600': DupOverRecDelete(self.r3_delete),
                            '6/5700': [DupOverRecDelete(self.r4_delete),
                                       DupOverRecDelete(self.r5_delete)]})

    def test_load_delete_reordered(self):
        assert_items_equal(load_dupes_overlaps(self.report_4),
                           {'6/2000': DupOverRecDelete(self.r1_delete),
                            '6/2200': DupOverRecDelete(self.r2_delete),
                            '6/5600': DupOverRecDelete(self.r3_delete),
                            '6/5700': [DupOverRecDelete(self.r4_delete),
                                       DupOverRecDelete(self.r5_delete)]})


class TestGetColumnIndexes():

    def setup(self):
        self.header_default = ['REP_REC_ID', 'MAKE_ID', 'MAKE_TXT',
                               'FROM_YEAR', 'TO_YEAR', 'MODEL_ID',
                               'MODEL_TXT', 'SUBMODEL_ID', 'SUBMODEL_TXT',
                               'ENGINE_ID', 'ENGINE_TXT', 'ATTRS',
                               'PART_GROUP_ID', 'PART_GROUP_TXT',
                               'PART_DESCR_ID', 'PART_DESCR_TXT', 'PART_NUM',
                               'PER_CAR_QTY', 'CAT_LINE_CD', 'BLOCK_CD',
                               'BLOCK_NUM', 'BLOCK_SEQ_NUM', 'FLAG',
                               'COMMENT_TXT', 'CDE2_ID', 'MODIFIED_USER',
                               'MODIFIED_DATE', 'GROUPING_ID',
                               'CDE_PAGE_SEQ_NUM', 'FILTERS_AND_OPTIONS']
        self.header_default_reordered = ['REP_REC_ID', 'CDE_PAGE_SEQ_NUM',
                                         'MAKE_ID', 'MAKE_TXT', 'FROM_YEAR',
                                         'TO_YEAR', 'MODEL_ID', 'MODEL_TXT',
                                         'SUBMODEL_ID', 'SUBMODEL_TXT',
                                         'ENGINE_ID', 'ENGINE_TXT', 'ATTRS',
                                         'PART_GROUP_ID', 'PART_GROUP_TXT',
                                         'PART_DESCR_ID', 'PART_DESCR_TXT',
                                         'PART_NUM', 'PER_CAR_QTY',
                                         'CAT_LINE_CD', 'BLOCK_CD',
                                         'BLOCK_NUM', 'BLOCK_SEQ_NUM', 'FLAG',
                                         'COMMENT_TXT', 'CDE2_ID',
                                         'MODIFIED_USER', 'MODIFIED_DATE',
                                         'GROUPING_ID', 'FILTERS_AND_OPTIONS']
        self.header_default_delete = ['REP_REC_ID', 'MAKE_ID', 'MAKE_TXT',
                                      'FROM_YEAR', 'TO_YEAR', 'MODEL_ID',
                                      'MODEL_TXT', 'SUBMODEL_ID',
                                      'SUBMODEL_TXT', 'ENGINE_ID',
                                      'ENGINE_TXT', 'ATTRS', 'PART_GROUP_ID',
                                      'PART_GROUP_TXT', 'PART_DESCR_ID',
                                      'PART_DESCR_TXT', 'PART_NUM',
                                      'PER_CAR_QTY', 'CAT_LINE_CD',
                                      'BLOCK_CD', 'BLOCK_NUM', 'BLOCK_SEQ_NUM',
                                      'FLAG', 'COMMENT_TXT', 'CDE2_ID',
                                      'MODIFIED_USER', 'MODIFIED_DATE',
                                      'GROUPING_ID', 'CDE_PAGE_SEQ_NUM',
                                      'FILTERS_AND_OPTIONS', 'DELETE']
        self.header_default_delete_reordered = ['REP_REC_ID',
                                                'CDE_PAGE_SEQ_NUM', 'DELETE',
                                                'MAKE_ID', 'MAKE_TXT',
                                                'FROM_YEAR', 'TO_YEAR',
                                                'MODEL_ID', 'MODEL_TXT',
                                                'SUBMODEL_ID', 'SUBMODEL_TXT',
                                                'ENGINE_ID', 'ENGINE_TXT',
                                                'ATTRS', 'PART_GROUP_ID',
                                                'PART_GROUP_TXT',
                                                'PART_DESCR_ID',
                                                'PART_DESCR_TXT', 'PART_NUM',
                                                'PER_CAR_QTY', 'CAT_LINE_CD',
                                                'BLOCK_CD', 'BLOCK_NUM',
                                                'BLOCK_SEQ_NUM', 'FLAG',
                                                'COMMENT_TXT', 'CDE2_ID',
                                                'MODIFIED_USER',
                                                'MODIFIED_DATE', 'GROUPING_ID',
                                                'FILTERS_AND_OPTIONS']

    def teardown(self):
        self.header_default = None
        self.header_default_delete = None
        self.header_default_reordered = None
        self.header_default_delete_reordered = None

    def test_get_column_indexes_default(self):
        assert_equal(get_column_indexes(self.header_default, False), range(30))

    def test_get_column_indexes_default_reordered(self):
        assert_equal(get_column_indexes(self.header_default_reordered, False),
                     [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                      17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 1, 29])

    def test_get_column_indexes_delete(self):
        assert_equal(get_column_indexes(self.header_default_delete, True),
                     range(31))

    def test_get_column_indexes_del_reordered(self):
        assert_equal(get_column_indexes(self.header_default_delete_reordered,
                                        True),
                     [0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                      17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                      1, 30, 2])


