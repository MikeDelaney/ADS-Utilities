from Tkinter import Tk
from tkFileDialog import askopenfilename
import pec
import dup_over_rpt
import get_specs
import pec_read_write
import read_reports
import string

__author__ = 'miked'


def update_record(src_record, report_record):
    return pec.PecRecSeq()


def apply_resolutions(src_dict, report_dict):
    """
    Dict Dict -> Dict
    Produces dict of pec records with changes from dupes report applied
    """
    return {}

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
    source_file.close()

    output_dict = apply_resolutions(source_dict, dupes_dict)

    dest_file = open(dest_filename, 'w')
    dest_file = pec_read_write.write_pecfile_dict(dest_file, output_dict)
    dest_file.close()


