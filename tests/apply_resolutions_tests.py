from nose.tools import *
from ADS_Utilities.apply_resolutions import *
from ADS_Utilities.dup_over_rpt import DupOverRecDelete
from ADS_Utilities.pec import PecRecSeq

__author__ = 'miked'


class TestApplyResolutions():

    def setup(self):
        d1 = ['1', '1', 'AMC-EAGLE', '1993', '1994', '18', 'TALON', '0', '',
              '0', '', '4 WHEEL/ALL WHEEL DRIVE', '28', 'F BRK HYDRAULICS',
              '55', 'Front Brake Hose', '1474-40300', '2', 'AUN', 'N', '0',
              '0', '', 'INNER - TSI - AWD', '16', 'miked', '8-Oct-13', '1',
              '1 0001600', '', '']
        d2 = ['2', '1', 'AMC-EAGLE', '1993', '1994', '18', 'TALON', '0', '',
              '0', '', 'EXC 4 WHEEL/ALL WHEEL DRIVE', '28', 'F BRK HYDRAULICS',
              '55', 'Front Brake Hose', '1474-40300', '2', 'AUN', 'N', '0',
              '0', '', 'INNER - DL - ES', '17', 'miked', '8-Oct-13', '1',
              '1 0001700', '', '']
        d3 = ['11', '1', 'AMC-EAGLE', '1996', '1998', '18', 'TALON', '0', '',
              '0', '', '4 WHEEL/ALL WHEEL DRIVE', '31', 'R BRK HYDRAULICS',
              '55', 'Rear Brake Hose', '1474-40093', '2', 'AUN', 'N', '0',
              '0', '', '', '63', 'miked', '8-Oct-13', '4', '1 0006300', '', '']
        d4 = ['12', '1', 'AMC-EAGLE', '1995', '1995', '18', 'TALON', '0', '',
              '0', '', 'w/4 WHEEL DISC; 4 WHEEL/ALL WHEEL DRIVE', '31',
              'R BRK HYDRAULICS', '55', 'Rear Brake Hose', '1474-40093', '2',
              'AUN', 'N', '0', '0', '', '', '64', 'miked', '8-Oct-13', '4',
              '1 0006400', '', '']
        d5 = ['13', '1', 'AMC-EAGLE', '1995', '1998', '18', 'TALON', '0', '',
              '0', '', 'w/4 WHEEL DISC; EXC 4 WHEEL/ALL WHEEL DRIVE', '31',
              'R BRK HYDRAULICS', '55', 'Rear Brake Hose', '1474-40093', '2',
              'AUN', 'N', '0', '0', '', 'ESI', '65', 'miked', '8-Oct-13',
              '4', '1 0006500', '', '']
        d6 = ['425', '13', 'OLDSMOBILE', '1970', '1970', '3', 'CUTLASS/F85',
              '0', '', '0', '', '', '28', 'F BRK HYDRAULICS', '55',
              'Front Brake Hose', '1474-17542', '2', 'AUN', 'N', '0', '0', '',
              '442 - CUTLASS (EXC CUTLASS SUPREME) - F85 - VISTA CRUISER',
              '5163', 'miked', '8-Oct-13', '124', '13 0005200', '', '']
        d7 = ['425', '13', 'OLDSMOBILE', '1971', '1971', '3', 'CUTLASS/F85',
              '0', '', '13', '', '', '28', 'F BRK HYDRAULICS', '55',
              'Front Brake Hose', '1474-17542', '2', 'AUN', 'N', '0', '0', '',
              'CUTLASS (EXC CUTLASS SUPREME) - F85 - VISTA CRUISER',
              '5163', 'miked', '8-Oct-13', '124', '13 0005200', '', '']
        d8 = ['425', '13', 'OLDSMOBILE', '1971', '1971', '3', 'CUTLASS/F85',
              '0', '', '24', '', '', '28', 'F BRK HYDRAULICS', '55',
              'Front Brake Hose', '1474-17542', '2', 'AUN', 'N', '0', '0', '',
              '442 - CUTLASS (EXC CUTLASS SUPREME) - F85 - VISTA CRUISER',
              '5163', 'miked', '8-Oct-13', '124', '13 0005200', '', '']
        d9 = ['425', '13', 'OLDSMOBILE', '1971', '1971', '3', 'CUTLASS/F85',
              '0', '', '38', '', 'w/FT DISC/RR DRUM', '28',
              'F BRK HYDRAULICS', '55', 'Front Brake Hose', '1474-17542', '2',
              'AUN', 'N', '0', '0', '', '442 - CUTLASS (EXC CUTLASS SUPREME)'
                                        ' - F85 - VISTA CRUISER',
              '5163', 'miked', '8-Oct-13', '124', '13 0005200', '', '']
        d10 = ['426', '13', 'OLDSMOBILE', '1971', '1971', '3', 'CUTLASS/F85',
               '0', '', '38', 'V8-455', 'w/4 WHEEL DRUM', '28',
               'F BRK HYDRAULICS', '55', 'Front Brake Hose', '1474-17542', '2',
               'AUN', 'N', '0', '0', '', '442 - CUTLASS (EXC CUTLASS SUPREME)'
                                         ' - CUTLASS SUPREME - F85'
                                         ' - VISTA CRUISER',
               '5170', 'miked', '8-Oct-13', '124', '13 0005900', '', '']
        d11 = ['416', '13', 'OLDSMOBILE', '1968', '1968', '3', 'CUTLASS/F85',
               '0', '', '0', '', 'w/FT DISC/RR DRUM', '28', 'F BRK HYDRAULICS',
               '55', 'Front Brake Hose', '1474-17542', '2', 'AUN', 'N', '0',
               '0', '', 'CUTLASS (EXC CUTLASS SUPREME)', '5159', 'miked',
               '8-Oct-13', '121', '13 0004800', '', 'Y']
        d12 = ['417', '13', 'OLDSMOBILE', '1968', '1968', '3', 'CUTLASS/F85',
               '0', '', '0', '', '', '28', 'F BRK HYDRAULICS', '55',
               'Front Brake Hose', '1474-17542', '2', 'AUN', 'N', '0', '0', '',
               '442 - CUTLASS (EXC CUTLASS SUPREME) - F85 - VISTA CRUISER',
               '5165', 'miked', '8-Oct-13', '121', '13 0005400', '', '']

        r1 = '  1 18  0  0  0  0  0  0  0  0  0  168    0    0    01993199428' \
             ' 55  2AUN1474-40300    N ^C:INNER - TSI - AWD' \
             '^C:***    1/1600     ***'
        r2 = '  1 18  0  0  0  0  0  0  0  0  0    0    0    0    01993199428' \
             ' 55  2AUN1474-40300    N ^C:INNER - DL - ES' \
             '^C:***    1/1700     ***'
        r3 = '  1 25  0  0  0  0  0  0  0  0  0    0    0    0    01991199128' \
             ' 55  2AUN1474-40081    N ^C:OUTER - HATCHBACK - SEDAN' \
             '^C:***    1/2600     ***'
        r4 = '  1 25  0  0  0  0  0  0  0  0  0  138    0    0    01989199028' \
             ' 55  2AUN1474-40086    N ^C:INNER^C:***    1/2700     ***'
        r5 = '  1 18  0  0  0  0  0  0  0  0  0  168    0    0    01996199831' \
             ' 55  2AUN1474-40093    N ^C:***    1/6300     ***'
        r6 = '  1 18  0  0  0  0  0  0  0  0  0  138  168    0    01995199531' \
             ' 55  2AUN1474-40093    N ^C:***    1/6400     ***'
        r7 = '  1 18  0  0  0  0  0  0  0  0  0  138    0    0    01995199831' \
             ' 55  2AUN1474-40093    N ^C:ESI^C:***    1/6500     ***'
        r8 = ' 13  3  0  0  0  0  0  0  0  0  0  137    0    0    01968196828' \
             ' 55  2AUN1474-17542    N ^C:CUTLASS (EXC CUTLASS SUPREME)' \
             '^C:***   13/4800     ***'
        r9 = ' 13  3  0  0  0  0  0  0  0  0  0    0    0    0    01970197128' \
             ' 55  2AUN1474-17542    N ' \
             '^C:442 - CUTLASS (EXC CUTLASS SUPREME) - F85 - VISTA CRUISER' \
             '^C:***   13/5200     ***'
        r10 = ' 13  3  0  0  0  0  0  0  0  0  0    0    0    0    01968196828' \
              ' 55  2AUN1474-17542    N ' \
              '^C:442 - CUTLASS (EXC CUTLASS SUPREME) - F85 - VISTA CRUISER' \
              '^C:***   13/5400     ***'
        r11 = ' 13  3  0  0  0  0  0 38  0  0  0  136    0    0    01971197128' \
              ' 55  2AUN1474-17542    N ^C:CUTLASS SUPREME' \
              '^C:***   13/5900     ***'

        e1 = '  1 18  0  0  0  0  0  0  0  0  0  168    0    0    01993199428' \
             ' 55  2AUN1474-40300    N ^C:INNER - TSI - AWD' \
             '^C:***    1/1600     ***'
        e2 = '  1 18  0  0  0  0  0  0  0  0  0 X168    0    0    01993199428' \
             ' 55  2AUN1474-40300    N ^C:INNER - DL - ES' \
             '^C:***    1/1700     ***'
        e3 = '  1 25  0  0  0  0  0  0  0  0  0    0    0    0    01991199128' \
             ' 55  2AUN1474-40081    N ^C:OUTER - HATCHBACK - SEDAN' \
             '^C:***    1/2600     ***'
        e4 = '  1 25  0  0  0  0  0  0  0  0  0  138    0    0    01989199028' \
             ' 55  2AUN1474-40086    N ^C:INNER^C:***    1/2700     ***'
        e5 = '  1 18  0  0  0  0  0  0  0  0  0  168    0    0    01996199831' \
             ' 55  2AUN1474-40093    N ^C:^C:***    1/6300     ***'
        e6 = '  1 18  0  0  0  0  0  0  0  0  0  138  168    0    01995199531' \
             ' 55  2AUN1474-40093    N ^C:^C:***    1/6400     ***'
        e7 = '  1 18  0  0  0  0  0  0  0  0  0  138 X168    0    01995199831' \
             ' 55  2AUN1474-40093    N ^C:ESI^C:***    1/6500     ***'
        e8 = ' 13  3  0  0  0  0  0  0  0  0  0    0    0    0    01970197028' \
             ' 55  2AUN1474-17542    N ' \
             '^C:442 - CUTLASS (EXC CUTLASS SUPREME) - F85 - VISTA CRUISER' \
             '^C:***   13/5200     ***'
        e9 = ' 13  3  0  0  0  0  0 13  0  0  0    0    0    0    01971197128' \
             ' 55  2AUN1474-17542    N ' \
             '^C:CUTLASS (EXC CUTLASS SUPREME) - F85 - VISTA CRUISER' \
             '^C:***   13/5201     ***'
        e10 = ' 13  3  0  0  0  0  0 24  0  0  0    0    0    0    01971197128' \
              ' 55  2AUN1474-17542    N ' \
              '^C:442 - CUTLASS (EXC CUTLASS SUPREME) - F85 - VISTA CRUISER' \
              '^C:***   13/5202     ***'
        e11 = ' 13  3  0  0  0  0  0 38  0  0  0  137    0    0    01971197128' \
              ' 55  2AUN1474-17542    N ' \
              '^C:442 - CUTLASS (EXC CUTLASS SUPREME) - F85 - VISTA CRUISER' \
              '^C:***   13/5203     ***'
        e12 = ' 13  3  0  0  0  0  0  0  0  0  0    0    0    0    01968196828' \
              ' 55  2AUN1474-17542    N ' \
              '^C:442 - CUTLASS (EXC CUTLASS SUPREME) - F85 - VISTA CRUISER' \
              '^C:***   13/5400     ***'
        e13 = ' 13  3  0  0  0  0  0 38  0  0  0  136    0    0    01971197128' \
              ' 55  2AUN1474-17542    N ' \
              '^C:442 - CUTLASS (EXC CUTLASS SUPREME) - CUTLASS SUPREME - F85' \
              ' - VISTA CRUISER^C:***   13/5900     ***'


        self.dupes = {'1/1600': [DupOverRecDelete(d1)],
                      '1/1700': [DupOverRecDelete(d2)],
                      '1/6300': [DupOverRecDelete(d3)],
                      '1/6400': [DupOverRecDelete(d4)],
                      '1/6500': [DupOverRecDelete(d5)],
                      '13/5200': [DupOverRecDelete(d6), DupOverRecDelete(d7),
                                  DupOverRecDelete(d8), DupOverRecDelete(d9)],
                      '13/5900': [DupOverRecDelete(d10)],
                      '13/4800': [DupOverRecDelete(d11)],
                      '13/5400': [DupOverRecDelete(d12)]}

        self.source = {'1/1600': PecRecSeq(r1), '1/1700': PecRecSeq(r2),
                       '1/2600': PecRecSeq(r3), '1/2700': PecRecSeq(r4),
                       '1/6300': PecRecSeq(r5), '1/6400': PecRecSeq(r6),
                       '1/6500': PecRecSeq(r7), '13/4800': PecRecSeq(r8),
                       '13/5200': PecRecSeq(r9), '13/5400': PecRecSeq(r10),
                       '13/5900': PecRecSeq(r11)}

        self.expected = {'1/1600': PecRecSeq(e1), '1/1700': PecRecSeq(e2),
                         '1/2600': PecRecSeq(e3), '1/2700': PecRecSeq(e4),
                         '1/6300': PecRecSeq(e5), '1/6400': PecRecSeq(e6),
                         '1/6500': PecRecSeq(e7), '13/5200': PecRecSeq(e8),
                         '13/5201': PecRecSeq(e9), '13/5202': PecRecSeq(e10),
                         '13/5203': PecRecSeq(e11), '13/5400': PecRecSeq(e12),
                         '13/5900': PecRecSeq(e13)}

    def teardown(self):
        self.dupes = None
        self.source = None
        self.expected = None

    def test_apply_resolutions(self):
        assert_items_equal(apply_resolutions(self.source, self.dupes),
                           self.expected)


class TestUpdateRecord():

    def setup(self):
        self.d1 = DupOverRecDelete(['1', '1', 'AMC-EAGLE', '1993', '1994',
                                    '18', 'TALON', '0', '', '0', '',
                                    '4 WHEEL/ALL WHEEL DRIVE', '28',
                                    'F BRK HYDRAULICS', '55',
                                    'Front Brake Hose', '1474-40300', '2',
                                    'AUN', 'N', '0', '0', '',
                                    'INNER - TSI - AWD', '16', 'miked',
                                    '8-Oct-13', '1', '1 0001600', '', ''])
        self.d1_result = PecRecSeq('  1 18  0  0  0  0  0  0  0  0  0  168   '
                                   ' 0    0    01993199428 55  2AUN1474-40300'
                                   '    N ^C:INNER - TSI - AWD'
                                   '^C:***    1/1600     ***')
        self.d2 = DupOverRecDelete(['2', '1', 'AMC-EAGLE', '1993', '1994',
                                    '18', 'TALON', '0', '', '0', '',
                                    'EXC 4 WHEEL/ALL WHEEL DRIVE', '28',
                                    'F BRK HYDRAULICS', '68',
                                    'Front Brake Hose', '1474-40300', '2',
                                    'AUN', 'N', '0', '0', '',
                                    'INNER - DL - ES', '17', 'miked',
                                    '8-Oct-13', '1', '1 0001700', '', ''])
        self.d2_result = PecRecSeq('  1 18  0  0  0  0  0  0  0  0  0 X168   '
                                   ' 0    0    01993199428 68  2AUN1474-40300'
                                   '    N ^C:INNER - DL - ES'
                                   '^C:***    1/1700     ***')
        self.models2 = DupOverRecDelete(['1', '1', 'AMC-EAGLE', '1993',
                                         '1994', '18, 22', 'TALON', '0', '',
                                         '0', '', '4 WHEEL/ALL WHEEL DRIVE',
                                         '28', 'F BRK HYDRAULICS', '55',
                                         'Front Brake Hose', '1474-40300',
                                         '2', 'AUN', 'N', '0', '0', '',
                                         'INNER - TSI - AWD', '16', 'miked',
                                         '8-Oct-13', '1', '1 0001600', '', ''])
        self.models2_result = PecRecSeq('  1 18 22  0  0  0  0  0  0  0  0  '
                                        '168    0    0    01993199428 55  2AUN'
                                        '1474-40300    N ^C:INNER - TSI - AWD'
                                        '^C:***    1/1600     ***')
        self.eng3 = DupOverRecDelete(['1', '1', 'AMC-EAGLE', '1993', '1994',
                                      '18', 'TALON', '0', '', '1, 2, 3', '',
                                      '4 WHEEL/ALL WHEEL DRIVE', '28',
                                      'F BRK HYDRAULICS', '55',
                                      'Front Brake Hose', '1474-40300', '2',
                                      'AUN', 'N', '0', '0', '',
                                      'INNER - TSI - AWD', '16', 'miked',
                                      '8-Oct-13', '1', '1 0001600', '', ''])
        self.eng3_result = PecRecSeq('  1 18  0  0  0  0  0  1  2  3  0  168 '
                                     '   0    0    01993199428 55  2AUN'
                                     '1474-40300    N ^C:INNER - TSI - AWD'
                                     '^C:***    1/1600     ***')
        self.spec2 = DupOverRecDelete(['1', '1', 'AMC-EAGLE', '1993', '1994',
                                       '18', 'TALON', '0', '', '0', '',
                                       '4 WHEEL/ALL WHEEL DRIVE; '
                                       'w/4 WHEEL DISC', '28',
                                       'F BRK HYDRAULICS', '55',
                                       'Front Brake Hose', '1474-40300', '2',
                                       'AUN', 'N', '0', '0', '',
                                       'INNER - TSI - AWD', '16', 'miked',
                                       '8-Oct-13', '1', '1 0001600', '', ''])
        self.spec2_result = PecRecSeq('  1 18  0  0  0  0  0  0  0  0  0  168'
                                      '  138    0    01993199428 55  2AUN'
                                      '1474-40300    N ^C:INNER - TSI - AWD'
                                      '^C:***    1/1600     ***')
        self.spec_dict = {u'w/4 WHEEL DRUM': 136, u'w/FT DISC/RR DRUM': 137,
                          u'w/4 WHEEL DISC': 138, u'4 WHEEL/ALL WHEEL DRIVE': 168}

    def teardown(self):
        self.d1 = None
        self.d1_result = None
        self.d2 = None
        self.d2_result = None
        self.models2 = None
        self.models2_result = None
        self.eng3 = None
        self.eng3_result = None
        self.spec2 = None
        self.spec2_result = None
        self.spec_dict = None

    def test_update_record_d1(self):
        assert_equal(str(update_record(self.d1, self.d1.pec_seq_num,
                                   self.spec_dict)),
                     str(self.d1_result))

    def test_update_record_d2(self):
        assert_equal(update_record(self.d2, self.d2.pec_seq_num,
                                   self.spec_dict),
                     self.d2_result)

    def test_update_record_models2(self):
        assert_equal(update_record(self.models2, self.models2.pec_seq_num,
                                   self.spec_dict),
                     self.models2_result)

    def test_update_record_eng3(self):
        assert_equal(update_record(self.eng3, self.eng3.pec_seq_num,
                                   self.spec_dict),
                     self.eng3_result)

    def test_update_record_spec2(self):
        assert_equal(update_record(self.spec2, self.spec2.pec_seq_num,
                                   self.spec_dict),
                     self.spec2_result)


class TestBuildSpecList():

    def setup(self):
        self.specs = {u'w/POWER STEERING': 164,
                      u'4 WHEEL/ALL WHEEL DRIVE': 168}

    def teardown(self):
        self.specs = None

    def test_build_spec_list_1(self):
        assert_equal(build_spec_list('EXC w/POWER STEERING', self.specs),
                     [' X164', '    0', '    0', '    0'])

    def test_build_spec_list_2(self):
        assert_equal(build_spec_list('w/POWER STEERING; '
                                     '4 WHEEL/ALL WHEEL DRIVE', self.specs),
                     ['  164', '  168', '    0', '    0'])


def test_increment_seq_1():
    assert_equal(increment_seq('1/1600'), '1/1601')


def test_increment_seq_2():
    assert_equal(increment_seq('31/5305'), '31/5306')


def test_build_mdl_eng_list_1():
    assert_equal(build_mdl_eng_list('1', 'model'), ['1', '0', '0', '0', '0', '0'])


def test_build_mdl_eng_list_2():
    assert_equal(build_mdl_eng_list('1, 2', 'model'), ['1', '2', '0', '0', '0', '0'])


def test_build_mdl_eng_list_all():
    assert_equal(build_mdl_eng_list('1, 2, 3, 4, 5, 6', 'model'), ['1', '2', '3', '4', '5', '6'])


def test_normalize_spec_text_colon():
    assert_equal(normalize_spec_text('w/4 WHEEL DISC: '
                                     '4 WHEEL/ALL WHEEL DRIVE'),
                 'w/4 WHEEL DISC; 4 WHEEL/ALL WHEEL DRIVE')


def test_normalize_spec_text_pwr_stg():
    assert_equal(normalize_spec_text('w/o POWER STEERING'),
                 'EXC w/POWER STEERING')


def test_normalize_spec_text_mt():
    assert_equal(normalize_spec_text('w/MAN TRANS'), 'EXC w/AUTO TRANS')


def test_normalize_spec_text_at():
    assert_equal(normalize_spec_text('w/o AUTO TRANS'), 'EXC w/AUTO TRANS')


def test_format_comment_blank():
    assert_equal(format_comment(''), '')


def test_format_comment_single_line():
    assert_equal(format_comment('BENDIX FRONT CALIPERS'),
                 '^C:BENDIX FRONT CALIPERS')


def test_format_comment_multiline():
    assert_equal(format_comment('INNER - 10MM X 155MM - GL - GLS - GT - JAZZ'
                                '~TDI - OLD BODY STYLE'),
                 '^C:INNER - 10MM X 155MM - GL - GLS - GT - JAZZ'
                 '^C:TDI - OLD BODY STYLE')


