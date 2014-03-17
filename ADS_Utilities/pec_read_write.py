import pec
from Tkinter import Tk
import tkMessageBox
import sys

__author__ = 'miked'


def load_pecfile_dict(pec_file):
    """
    FileObj -> Dict
    Produces a dictionary mapping make/sequence of source record to
    corresponding PecRecSeq object.
    """
    file_dict = {}
    while True:
        record = pec_file.readline()[:-1]
        if record == '':
            break
        else:
            record = pec.PecRecSeq(record)
            if record.sequence in file_dict:
                Tk().withdraw()
                tkMessageBox.showerror('Error', 'Duplicate sequence numbers '
                                                'exist in PEC file.')
                sys.exit()
            else:
                file_dict[record.sequence] = record
    return file_dict


def write_pecfile_dict(output_file, record_dict):
    """
    FileObj Dict -> FileObj
    Writes pec records from dictionary to output_file
    """
    for key in sorted(record_dict.keys()):
        output_file.write('%s\n' % str(record_dict[key]))
    return output_file
