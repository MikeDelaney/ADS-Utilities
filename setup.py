try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Applies corrections in duplicates/overlaps report to source data',
    'author': 'Mike Delaney',
    'url': '',
    'download_url': '',
    'author_email': 'mdelaney@utexas.edu',
    'version': '1.0',
    'install_requires': ['nose', 'mock', 'Tkinter']
    'packages': ['tests', 'ADS_Utilities'],
    'scripts': [],
    'name': 'ADS Utilities',
    'license': ''
}

setup(**config)
