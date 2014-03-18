from nose.tools import *
from ADS_Utilities.pec_read_write import load_pecfile_dict, write_pecfile_dict
from ADS_Utilities.pec import PecRecSeq
import StringIO

__author__ = 'miked'

class TestPecReadWrite():

    def setup(self):
        r1 = '  1  1  0  0  0  0  0  0  0  0  0    0    0    0    01962196528' \
             ' 55  2AUN1474-17593    N ^C:***    1/100      ***'
        r2 = '  1  1  0  0  0  0  0  0  0  0  0    0    0    0    01966196628' \
             ' 55  2AUN1474-17593    N ^C:ROUND HOLE IN SUPPORT' \
             '^C:***    1/200      ***'
        r3 = '  2  3  0  0  0  0  0  0  0  0  0    0    0    0    01987198933' \
             ' 10  1AUN1475-23519    N ^C:MEDIUM DUTY BRAKES' \
             '^C:***    2/36500    ***'
        r4 = '  2  3  0  0  0  0  0  0  0  0  0    0    0    0    01990199333' \
             ' 10  1AUN1475-23785    N ^C:STATION WAGON' \
             '^C:***    2/36500    ***'

        self.pec_normal = StringIO.StringIO(r1 + '\n' + r2 + '\n' + r3 + '\n')
        self.pec_dupseq = StringIO.StringIO(r1 + '\n' + r2 + '\n' + r3 + '\n'
                                            + r4 + '\n')
        self.output_dict = {'1/100': PecRecSeq(r1), '1/200': PecRecSeq(r2),
                            '2/36500': PecRecSeq(r3)}

    def teardown(self):
        self.pec_normal = None
        self.pec_dupseq = None
        self.output_dict = None

    def test_load_pecfile_dict(self):
        assert_items_equal(load_pecfile_dict(self.pec_normal), self.output_dict)

    def test_load_pecfile_dupseq(self):
        assert_equal(1, load_pecfile_dict(self.pec_dupseq))

    def test_write_pecfile_dict(self):
        assert_equal(write_pecfile_dict(StringIO.StringIO(''), self.output_dict).getvalue(), self.pec_normal.getvalue())
