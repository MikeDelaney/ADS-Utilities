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

        self.r1_reordered = self.r1[:]
        self.r1_reordered.insert(1, self.r1_reordered.pop(28))
        self.r1_delete = self.r1[:]
        self.r1_delete.append('Y')
        self.r1_delete_reordered = self.r1_delete[:]
        self.r1_delete_reordered.insert(1, self.r1_delete_reordered.pop(28))
        self.r1_delete_reordered.insert(2, self.r1_delete_reordered.pop())

        self.r2_reordered = self.r2[:]
        self.r2_reordered.insert(1, self.r2_reordered.pop(28))
        self.r2_delete = self.r2[:]
        self.r2_delete.append('')
        self.r2_delete_reordered = self.r2_delete[:]
        self.r2_delete_reordered.insert(1, self.r2_delete_reordered.pop(28))
        self.r2_delete_reordered.insert(2, self.r2_delete_reordered.pop())

        self.r3_reordered = self.r3[:]
        self.r3_reordered.insert(1, self.r3_reordered.pop(28))
        self.r3_delete = self.r3[:]
        self.r3_delete.append('')
        self.r3_delete_reordered = self.r3_delete[:]
        self.r3_delete_reordered.insert(1, self.r3_delete_reordered.pop(28))
        self.r3_delete_reordered.insert(2, self.r3_delete_reordered.pop())

        self.r4_reordered = self.r4[:]
        self.r4_reordered.insert(1, self.r4_reordered.pop(28))
        self.r4_delete = self.r4[:]
        self.r4_delete.append('Y')
        self.r4_delete_reordered = self.r4_delete[:]
        self.r4_delete_reordered.insert(1, self.r4_delete_reordered.pop(28))
        self.r4_delete_reordered.insert(2, self.r4_delete_reordered.pop())

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
                                          '\t'.join(filter_rec) + '\n')
        self.report_2 = StringIO.StringIO('\t'.join(header_reordered) + '\n' +
                                          '\t'.join(self.r1_reordered) + '\n' +
                                          '\t'.join(self.r2_reordered) + '\n' +
                                          '\t'.join(separator) + '\n' +
                                          '\t'.join(self.r3_reordered) + '\n' +
                                          '\t'.join(self.r4_reordered) + '\n' +
                                          '\t'.join(filter_rec) + '\n')
        self.report_3 = StringIO.StringIO('\t'.join(header_delete) + '\n' +
                                          '\t'.join(self.r1_delete) + '\n' +
                                          '\t'.join(self.r2_delete) + '\n' +
                                          '\t'.join(separator_delete) + '\n' +
                                          '\t'.join(self.r3_delete) + '\n' +
                                          '\t'.join(self.r4_delete) + '\n' +
                                          '\t'.join(filter_rec_delete) + '\n')
        self.report_4 = StringIO.StringIO('\t'.join(header_delete_reordered) +
                                          '\n' +
                                          '\t'.join(self.r1_delete_reordered) +
                                          '\n' +
                                          '\t'.join(self.r2_delete_reordered) +
                                          '\n' +
                                          '\t'.join(separator_delete_reordered)
                                          + '\n' +
                                          '\t'.join(self.r3_delete_reordered) +
                                          '\n' +
                                          '\t'.join(self.r4_delete_reordered) +
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
        self.r1_reordered = None
        self.r2_reordered = None
        self.r3_reordered = None
        self.r4_reordered = None
        self.r1_delete = None
        self.r2_delete = None
        self.r3_delete = None
        self.r4_delete = None
        self.r1_delete_reordered = None
        self.r2_delete_reordered = None
        self.r3_delete_reordered = None
        self.r4_delete_reordered = None

    def test_load_dupes_overlaps_size(self):
        assert_equal(len(load_dupes_overlaps(self.report_1)), 4)
        assert_equal(len(load_dupes_overlaps(self.report_2)), 4)
        assert_equal(len(load_dupes_overlaps(self.report_3)), 4)
        assert_equal(len(load_dupes_overlaps(self.report_4)), 4)

    def test_should_fail(self):
        assert_equal(str(DupOverRecord(self.r1)), str(DupOverRecord(self.r2)))

    def test_load_dupes_overlaps_values(self):
        assert_equal(str(load_dupes_overlaps(self.report_1)['6/2000'][0]), str(DupOverRecord(self.r1)))





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

    def test_get_column_indexes(self):
        assert_equal(get_column_indexes(self.header_default, False), range(30))
        assert_equal(get_column_indexes(self.header_default_reordered, False),
                     [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                      17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 1, 29])
        assert_equal(get_column_indexes(self.header_default_delete, True),
                     range(31))
        assert_equal(get_column_indexes(self.header_default_delete_reordered,
                                        True),
                     [0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                      17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                      1, 30, 2])


