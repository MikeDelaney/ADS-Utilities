from nose.tools import *
from ADS_Utilities.pec_read_write import load_pecfile_dict, write_pecfile_dict
from ADS_Utilities.pec import PecRecSeq
import StringIO

__author__ = 'miked'

class TestPecReadWrite():

    def setup(self):
        self.r1 = '  1  1  0  0  0  0  0  0  0  0  0    0    0    0    01962' \
                  '196528 55  2AUN1474-17593    N ^C:***    1/100      ***'
        self.r2 = '  1  1  0  0  0  0  0  0  0  0  0    0    0    0    01966' \
                  '196628 55  2AUN1474-17593    N ^C:ROUND HOLE IN SUPPORT' \
                  '^C:***    1/200      ***'
        self.r3 = '  2  3  0  0  0  0  0  0  0  0  0    0    0    0    01987' \
                  '198933 10  1AUN1475-23519    N ^C:MEDIUM DUTY BRAKES' \
                  '^C:***    2/36500    ***'
        self.r4 = '  2  3  0  0  0  0  0  0  0  0  0    0    0    0    01990' \
                  '199333 10  1AUN1475-23785    N ^C:STATION WAGON' \
                  '^C:***    2/36500    ***'

        self.pec_normal = StringIO.StringIO(self.r1 + '\n' + self.r2 + '\n' +
                                            self.r3 + '\n')
        self.pec_dupseq = StringIO.StringIO(self.r1 + '\n' + self.r2 + '\n' +
                                            self.r3 + '\n' + self.r4 + '\n')

        self.output_dict = {'1/100': PecRecSeq(self.r1),
                            '1/200': PecRecSeq(self.r2),
                            '2/36500': PecRecSeq(self.r3)}


    def teardown(self):
        self.r1 = None
        self.r2 = None
        self.r3 = None
        self.r4 = None
        self.pec_normal = None
        self.pec_dupseq = None
        self.output_dict = None

    def test_load_pecfile_dict(self):
        pec_normal_dict = load_pecfile_dict(self.pec_normal)
        assert_equal(str(pec_normal_dict['1/100']), str(PecRecSeq(self.r1)))
        assert_equal(str(pec_normal_dict['1/200']), str(PecRecSeq(self.r2)))
        assert_equal(str(pec_normal_dict['2/36500']), str(PecRecSeq(self.r3)))

    def test_load_pecfile_dupseq(self):
        assert_equal(1, load_pecfile_dict(self.pec_dupseq))

    def test_write_pecfile_dict(self):
        assert_equal(write_pecfile_dict(StringIO.StringIO(''), self.output_dict).getvalue(), self.pec_normal.getvalue())
