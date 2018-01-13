#!/usr/bin/env python
from os.path import realpath, dirname, join
from setuptools import setup, find_packages

DISTNAME = 'biwrap'
AUTHOR = 'Maxim Kochurov'
AUTHOR_EMAIL = 'maxim.v.kochurov@gmail.com'
VERSION = '0.1.6'
PROJECT_ROOT = dirname(realpath(__file__))
try:
    LONG_DESCRIPTION = open(join(PROJECT_ROOT, 'README.rst')).read()
except IOError:
    LONG_DESCRIPTION = ''
LICENSE = 'MIT License'

if __name__ == "__main__":
    setup(
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        description='Yet simple util to make wrapper with optional arguments',
        long_description=LONG_DESCRIPTION,
        name=DISTNAME,
        version=VERSION,
        license=LICENSE,
        packages=find_packages(),
        url='https://github.com/ferrine/biwrap',
        download_url='https://github.com/ferrine/biwrap/archive/v0.1.6.zip'
    )
