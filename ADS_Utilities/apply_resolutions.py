from Tkinter import Tk
from tkFileDialog import askopenfilename
import tkMessageBox
import ADS_Utilities.pec as pec
import ADS_Utilities.get_specs as get_specs
import ADS_Utilities.pec_read_write as pec_read_write
import ADS_Utilities.read_reports as read_reports
import string
import sys

__author__ = 'miked'


def build_mdl_eng_list(mdl_eng_string, list_type):
    """
    Str Str -> listof Str
    Produces list of model/engine numbers of appropriate length from given
    string
    """
    if list_type == 'model':
        new_list = ['0', '0', '0', '0', '0', '0']
    else:
        new_list = ['0', '0', '0', '0']
    if mdl_eng_string.find(',') == -1:
        new_list[0] = mdl_eng_string
    else:
        new_mdl_eng = mdl_eng_string.split(',')
        for i in range(0, len(new_mdl_eng)):
            new_list[i] = new_mdl_eng[i].strip()
    return new_list


def normalize_spec_text(spec_string):
    """
    Str -> Str
    Produces string with corrected punctuation and with text values matched
    to spec table
    """
    spec_string = spec_string.replace(':', ';')
    spec_string = spec_string.replace('w/o POWER STEERING',
                                      'EXC w/POWER STEERING')
    spec_string = spec_string.replace('w/MAN TRANS', 'EXC w/AUTO TRANS')
    spec_string = spec_string.replace('w/o AUTO TRANS', 'EXC w/AUTO TRANS')
    return spec_string


def format_comment(comment):
    """
    Str -> Str
    Produces string with '^C:' as leading text delimiter and as new line
    indicator.
    """
    if len(comment) == 0:
        return comment
    return '^C:' + comment.replace('~', '^C:')


def build_spec_list(attrs_string, spec_dict):
    """
    Str Dict -> listof Str
    Produces list of specs with text translated to coded values
    """
    spec_list = ['    0', '    0', '    0', '    0']
    if len(attrs_string) == 0:
        return spec_list
    new_specs = attrs_string.split(';')
    for i in range(0, len(new_specs)):
        spec_text = new_specs[i].strip()
        if spec_text[:3] == 'EXC':
            spec_list[i] = ' X' + ('  ' + str(spec_dict[spec_text[4:]]))[-3:]
        else:
            spec_list[i] = ('     ' + str(spec_dict[spec_text]))[-5:]
    return spec_list


def increment_seq(sequence):
    """
    Str -> Str
    Produces new make/sequence number with sequence incremented by 1
    """
    slash_loc = sequence.find('/')
    mk = sequence[:slash_loc]
    seq = int(sequence[slash_loc + 1:]) + 1
    return mk + '/' + str(seq)


def update_record(report_record, sequence, spec_dict):
    """
    DupOverRecDelete Str -> PecRecSeq
    Produces new PecRecSeq object containing information from report record.
    """
    models = build_mdl_eng_list(report_record.model_id, 'model')
    engines = build_mdl_eng_list(report_record.engine_id, 'engine')
    specs = build_spec_list(normalize_spec_text(report_record.attrs), spec_dict)
    comment = format_comment(report_record.comment_text)
    new_record = pec.PecRecSeq()
    new_record.make = report_record.make_id
    new_record.model_1 = models[0]
    new_record.model_2 = models[1]
    new_record.model_3 = models[2]
    new_record.model_4 = models[3]
    new_record.model_5 = models[4]
    new_record.model_6 = models[5]
    new_record.engine_1 = engines[0]
    new_record.engine_2 = engines[1]
    new_record.engine_3 = engines[2]
    new_record.engine_4 = engines[3]
    new_record.spec_1 = pec.SpecificCondition(specs[0])
    new_record.spec_2 = pec.SpecificCondition(specs[1])
    new_record.spec_3 = pec.SpecificCondition(specs[2])
    new_record.spec_4 = pec.SpecificCondition(specs[3])
    new_record.from_year = report_record.from_year
    new_record.to_year = report_record.to_year
    new_record.group = report_record.part_group_id
    new_record.pd = report_record.part_descr_id
    new_record.pcq = report_record.per_car_qty
    new_record.lc = report_record.cat_line_cd
    new_record.pn = report_record.part_num
    new_record.block_flag = report_record.block_cd
    if report_record.flag == '':
        new_record.flag = ' '
    else:
        new_record.flag = report_record.flag
    new_record.comment = comment
    new_record.sequence = sequence
    return new_record


def apply_resolutions(src_dict, report_dict, spec_dict):
    """
    Dict Dict -> Dict
    Produces dict of pec records with changes from dupes report applied
    """
    results_dict = {}
    for key in src_dict:
        if key not in report_dict:
            results_dict[key] = src_dict[key]
        else:
            mkseq = key
            for i in range(0, len(report_dict[key])):
                if report_dict[key][i].delete == 'Y':
                    pass
                else:
                    results_dict[mkseq] = update_record(report_dict[key][i], mkseq, spec_dict)
                    mkseq = increment_seq(mkseq)
    return results_dict


if __name__ == '__main__':
    Tk().withdraw()
    source_filename = askopenfilename(initialdir='C:\Wip',
                                      title='Select Source File')
    source_path = source_filename[:string.rfind(source_filename, '/')]
    report_filename = askopenfilename(initialdir=source_path,
                                      title='Select Dupes Rpt')
    dest_filename = source_filename[:-4] + '_out.txt'

    report_file = open(report_filename)
    dupes_dict = read_reports.load_dupes_overlaps(report_file)
    report_file.close()

    spec_dict = get_specs.spec_txt_to_val()

    source_file = open(source_filename)
    source_dict = pec_read_write.load_pecfile_dict(source_file)
    if source_dict == 1:
        tkMessageBox.showerror('Error', 'Duplicate sequence numbers '
                                                'exist in PEC file.')
        sys.exit()
    source_file.close()

    output_dict = apply_resolutions(source_dict, dupes_dict, spec_dict)

    dest_file = open(dest_filename, 'w')
    dest_file = pec_read_write.write_pecfile_dict(dest_file, output_dict)
    dest_file.close()


