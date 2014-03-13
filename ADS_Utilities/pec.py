class SpecificCondition(object):
    def __init__(self, spec='    0'):
        self.or_value = spec[:1]
        self.x_value = spec[1:2]
        self.code = spec[2:].strip()

    def __str__(self):
        return self.or_value + self.x_value + ('  ' + str(self.code))[-3:]

    
class PecRec(object):
    def __init__(self, rec_str=('  0  0  0  0  0  0  0  0  0  0  0    0    0'
                                '    0    019621962 0  0  0XXX              N')):
        self.make = rec_str[0:3].strip()
        self.model_1 = rec_str[3:6].strip()
        self.model_2 = rec_str[6:9].strip()
        self.model_3 = rec_str[9:12].strip()
        self.model_4 = rec_str[12:15].strip()
        self.model_5 = rec_str[15:18].strip()
        self.model_6 = rec_str[18:21].strip()
        self.engine_1 = rec_str[21:24].strip()
        self.engine_2 = rec_str[24:27].strip()
        self.engine_3 = rec_str[27:30].strip()
        self.engine_4 = rec_str[30:33].strip()
        self.spec_1 = SpecificCondition(rec_str[33:38])
        self.spec_2 = SpecificCondition(rec_str[38:43])
        self.spec_3 = SpecificCondition(rec_str[43:48])
        self.spec_4 = SpecificCondition(rec_str[48:53])
        self.from_year = int(rec_str[53:57])
        self.to_year = int(rec_str[57:61])
        self.group = rec_str[61:63].strip()
        self.pd = rec_str[63:66].strip()
        self.pcq = rec_str[66:69].strip()
        self.lc = rec_str[69:72]
        self.pn = rec_str[72:86].strip()
        self.block_flag = rec_str[86:87]
        self.flag = rec_str[87:88]
        self.comment = rec_str[88:]

    def __str__(self):
        return (('   ' + self.make)[-3:] +
                ('   ' + self.model_1)[-3:] +
                ('   ' + self.model_2)[-3:] +
                ('   ' + self.model_3)[-3:] +
                ('   ' + self.model_4)[-3:] +
                ('   ' + self.model_5)[-3:] +
                ('   ' + self.model_6)[-3:] +
                ('   ' + self.engine_1)[-3:] +
                ('   ' + self.engine_2)[-3:] +
                ('   ' + self.engine_3)[-3:] +
                ('   ' + self.engine_4)[-3:] +
                str(self.spec_1) +
                str(self.spec_2) +
                str(self.spec_3) +
                str(self.spec_4) +
                str(self.from_year) +
                str(self.to_year) +
                ('  ' + self.group)[-2:] +
                ('   ' + self.pd)[-3:] +
                ('   ' + self.pcq)[-3:] +
                self.lc +
                (self.pn + '              ')[:14] +
                self.block_flag +
                self.flag +
                self.comment)


class PecRecSeq(object):
    def __init__(self,
                 rec_str=('  0  0  0  0  0  0  0  0  0  0  0    0    0'
                          '    0    019621962 0  0  0XXX              N'
                          ' ^C:***    0/0         ***')):
        self.make = rec_str[0:3].strip()
        self.model_1 = rec_str[3:6].strip()
        self.model_2 = rec_str[6:9].strip()
        self.model_3 = rec_str[9:12].strip()
        self.model_4 = rec_str[12:15].strip()
        self.model_5 = rec_str[15:18].strip()
        self.model_6 = rec_str[18:21].strip()
        self.engine_1 = rec_str[21:24].strip()
        self.engine_2 = rec_str[24:27].strip()
        self.engine_3 = rec_str[27:30].strip()
        self.engine_4 = rec_str[30:33].strip()
        self.spec_1 = SpecificCondition(rec_str[33:38])
        self.spec_2 = SpecificCondition(rec_str[38:43])
        self.spec_3 = SpecificCondition(rec_str[43:48])
        self.spec_4 = SpecificCondition(rec_str[48:53])
        self.from_year = int(rec_str[53:57])
        self.to_year = int(rec_str[57:61])
        self.group = rec_str[61:63].strip()
        self.pd = rec_str[63:66].strip()
        self.pcq = rec_str[66:69].strip()
        self.lc = rec_str[69:72]
        self.pn = rec_str[72:86].strip()
        self.block_flag = rec_str[86:87]
        self.flag = rec_str[87:88]
        self.comment = rec_str[88:len(rec_str)-24]
        self.sequence = rec_str[-18:-3].strip()

    def __str__(self):
        return (('   ' + self.make)[-3:] +
                ('   ' + self.model_1)[-3:] +
                ('   ' + self.model_2)[-3:] +
                ('   ' + self.model_3)[-3:] +
                ('   ' + self.model_4)[-3:] +
                ('   ' + self.model_5)[-3:] +
                ('   ' + self.model_6)[-3:] +
                ('   ' + self.engine_1)[-3:] +
                ('   ' + self.engine_2)[-3:] +
                ('   ' + self.engine_3)[-3:] +
                ('   ' + self.engine_4)[-3:] +
                str(self.spec_1) +
                str(self.spec_2) +
                str(self.spec_3) +
                str(self.spec_4) +
                str(self.from_year) +
                str(self.to_year) +
                ('  ' + self.group)[-2:] +
                ('   ' + self.pd)[-3:] +
                ('   ' + self.pcq)[-3:] +
                self.lc +
                (self.pn + '              ')[:14] +
                self.block_flag +
                self.flag +
                self.comment +
                '^C:***' + ('     ' + self.sequence[:self.sequence.find('/')])[-5:] +
                (self.sequence[self.sequence.find('/'):] + '         ')[:10] + '***')






