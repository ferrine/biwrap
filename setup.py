#!/usr/bin/env python
from setuptools import setup, find_packages

DISTNAME = 'biwrap'
AUTHOR = 'Maxim Kochurov'
AUTHOR_EMAIL = 'maxim.v.kochurov@gmail.com'
VERSION = '0.1.2'
LONG_DESCRIPTION = open('README.rst').read()
LICENSE = open('LICENSE').read()

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
        download_url='https://github.com/ferrine/biwrap/archive/v0.1.2.zip'
    )
