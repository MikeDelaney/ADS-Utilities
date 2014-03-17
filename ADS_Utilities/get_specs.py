import pyodbc

__author__ = 'michael.delaney'


def get_rows():
    """
    Returns recordset from svt.mdb for spec translation
    """
    conn = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb)};'
                          'Dbq=C:\Wip\_VALID_TABLES\svt.mdb;Uid=Admin;Pwd=;')
    cursor = conn.cursor()
    cursor.execute('select spec_txt, spec_no from ct_spec')
    rows = cursor.fetchall()
    return rows

def spec_txt_to_val():
    """
    Recordset -> Dict
    Produces dictionary mapping specific condition text to spec number.
    """
    spec_dict = {}
    rows = get_rows()
    for row in rows:
        spec_dict[row[0]] = row[1]
    return spec_dict