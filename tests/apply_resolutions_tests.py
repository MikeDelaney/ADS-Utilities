from nose.tools import *
from ADS_Utilities.apply_resolutions import apply_resolutions, update_record
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


        self.dupes = {'1/1600': DupOverRecDelete(d1),
                      '1/1700': DupOverRecDelete(d2),
                      '1/6300': DupOverRecDelete(d3),
                      '1/6400': DupOverRecDelete(d4),
                      '1/6500': DupOverRecDelete(d5),
                      '13/5200': [DupOverRecDelete(d6), DupOverRecDelete(d7),
                                  DupOverRecDelete(d8), DupOverRecDelete(d9)],
                      '13/5900': DupOverRecDelete(d10),
                      '13/4800': DupOverRecDelete(d11),
                      '13/5400': DupOverRecDelete(d12)}

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

    def test_update_record(self):
        pass