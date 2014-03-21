ADS-Utilities
=============

Allows resolving duplicates/overlaps directly in reports and applying changes to source data without
use of PET for editing.

Requires:
=========
1. Updated copy of svt.mdb in C:\Wip\_VALID_TABLES folder
2. Python 2.7

To Use:
=======
1. Open report in MS Excel
2. Add a column with a heading of DELETE
3. Resolve duplicates/overlaps in the report. Changes made to report fields will be applied to the PEC data.
4. Save completed resolutions as a .tab file
5. Retrieve PEC source data with sequence numbers
6. Run apply_resolutions.py to apply the changes.

