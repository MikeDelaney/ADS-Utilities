import dup_over_rpt
__author__ = 'miked'


def load_dupes_overlaps(report_file):
    """
    FileObj -> Dict
    Produces dictionary mapping pec make/sequence number to the corresponding
    report record
    """
    rec_dict = {}
    header = report_file.readline()[:-1].split('\t')
    if 'DELETE' in header:
        del_flag = True
    else:
        del_flag = False
    col_indexes = get_column_indexes(header, del_flag)
    while True:
        line = report_file.readline()[:-1].split('\t')
        line = [line[i] for i in col_indexes]
        if line[0] == '':
            break
        elif line[1] == '-':
            pass
        else:
            if del_flag:
                record = dup_over_rpt.DupOverRecDelete(line)
            else:
                record = dup_over_rpt.DupOverRecord(line)
            if record.pec_seq_num not in rec_dict:
                rec_dict[record.pec_seq_num] = [record]
            else:
                rec_dict[record.pec_seq_num].append(record)
    return rec_dict


def get_column_indexes(header, delete_flag):
    """
    listof Str Bool -> listof Int
    Produces list containing indexes of report column names from the report
    header.  Used for re-ordering columns.
    """
    default_cols = ['REP_REC_ID', 'MAKE_ID', 'MAKE_TXT', 'FROM_YEAR',
                    'TO_YEAR', 'MODEL_ID', 'MODEL_TXT', 'SUBMODEL_ID',
                    'SUBMODEL_TXT', 'ENGINE_ID', 'ENGINE_TXT', 'ATTRS',
                    'PART_GROUP_ID', 'PART_GROUP_TXT', 'PART_DESCR_ID',
                    'PART_DESCR_TXT', 'PART_NUM', 'PER_CAR_QTY', 'CAT_LINE_CD',
                    'BLOCK_CD', 'BLOCK_NUM', 'BLOCK_SEQ_NUM', 'FLAG',
                    'COMMENT_TXT', 'CDE2_ID', 'MODIFIED_USER', 'MODIFIED_DATE',
                    'GROUPING_ID', 'CDE_PAGE_SEQ_NUM', 'FILTERS_AND_OPTIONS']
    if delete_flag:
        default_cols.append('DELETE')
    column_indexes = []
    for column in default_cols:
        column_indexes.append(header.index(column))
    return column_indexes
