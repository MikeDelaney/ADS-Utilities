from Tkinter import Tk
from tkFileDialog import askopenfilename
import tkMessageBox
import pec
import dup_over_rpt
import get_specs
import pec_read_write
import read_reports
import string
import sys

__author__ = 'miked'


def build_model_list(model_string):
    model_list = ['0', '0', '0', '0', '0', '0']
    if model_string.find(',') == -1:
        model_list[0] = model_string
    else:
        new_models = model_string.split(',')
        for i in range(0, len(new_models)):
            model_list[i] = new_models[i].strip()
    return model_list


def build_engine_list(engine_string):
    return ['0', '0', '0', '0']


def build_spec_list(attrs_string):
    return ['    0', '    0', '    0', '    0']


def increment_seq(sequence):
    slash_loc = sequence.find('/')
    mk = sequence[:slash_loc]
    seq = int(sequence[slash_loc + 1:]) + 1
    return mk + '/' + str(seq)


def update_record(report_record, sequence):
    models = build_model_list(report_record.model_id)
    engines = build_engine_list(report_record.engine_id)
    specs = build_spec_list(report_record.attrs)
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
    new_record.spec_1 = specs[0]
    new_record.spec_2 = specs[1]
    new_record.spec_3 = specs[2]
    new_record.spec_4 = specs[3]
    new_record.from_year = report_record.from_year
    new_record.to_year = report_record.to_year
    new_record.group = report_record.part_group_id
    new_record.pd = report_record.part_descr_id
    new_record.pcq = report_record.per_car_qty
    new_record.lc = report_record.cat_line_cd
    new_record.pn = report_record.part_num
    new_record.block_flag = report_record.block_cd
    new_record.flag = report_record.flag
    new_record.comment = report_record.comment_text
    new_record.sequence = sequence
    return new_record


def apply_resolutions(src_dict, report_dict):
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
                if report_dict[key][i].delete == '':
                    pass
                else:
                    results_dict[mkseq] = update_record(report_dict[key][i], mkseq)
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

    output_dict = apply_resolutions(source_dict, dupes_dict)

    dest_file = open(dest_filename, 'w')
    dest_file = pec_read_write.write_pecfile_dict(dest_file, output_dict)
    dest_file.close()


