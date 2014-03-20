from distutils.core import setup

setup(
    name='ADS Utilities',
    version='1.0',
    packages=['tests', 'ADS_Utilities'],
    scripts=['bin/apply_resolutions.py'],
    url='',
    license='',
    author='Mike Delaney',
    author_email='mdelaney@utexas.edu',
    description='Applies corrections in duplicates/overlaps report to source data'
)
