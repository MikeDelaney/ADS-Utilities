__author__ = 'michael.delaney'

class DupOverRecord(object):
    def __init__(self, record=['', '', '', '', '', '', '', '', '', '', '',
                               '', '', '', '', '', '', '', '', '', '', '',
                               '', '', '', '', '', '', '', '']):
        self.rec_num = record[0]
        self.make_id = record[1]
        self.make_text = record[2]
        self.from_year = record[3]
        self.to_year = record[4]
        self.model_id = record[5]
        self.model_text = record[6]
        self.submodel_id = record[7]
        self.submodel_text = record[8]
        self.engine_id = record[9]
        self.engine_text = record[10]
        self.attrs = record[11]
        self.part_group_id = record[12]
        self.part_group_text = record[13]
        self.part_descr_id = record[14]
        self.part_descr_text = record[15]
        self.part_num = record[16]
        self.per_car_qty = record[17]
        self.cat_line_cd = record[18]
        self.block_cd = record[19]
        self.block_num = record[20]
        self.block_seq_num = record[21]
        self.flag = record[22]
        self.comment_text = record[23]
        self.cde2_id = record[24]
        self.modified_user = record[25]
        self.modified_date = record[26]
        self.grouping_id = record[27]
        self.cde_page_seq_num = record[28]
        self.pec_seq_num = record[28][:record[28].find(' ')] + '/' \
                           + str(int(record[28][record[28].find(' '):]))
        self.filters_and_options = record[29]

class DupOverRecDelete(DupOverRecord):
    def __init__(self, record=['', '', '', '', '', '', '', '', '', '', '',
                               '', '', '', '', '', '', '', '', '', '', '',
                               '', '', '', '', '', '', '', '', '']):
        self.delete = record.pop()
        DupOverRecord.__init__(self, record)