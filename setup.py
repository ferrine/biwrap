#!/usr/bin/env python
from setuptools import setup, find_packages

DISTNAME = 'biwrap'
AUTHOR = 'Maxim Kochurov'
AUTHOR_EMAIL = 'maxim.v.kochurov@gmail.com'
VERSION = '0.1.0'


if __name__ == "__main__":
    setup(
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        name=DISTNAME,
        version=VERSION,
        packages=find_packages(),
        url='https://github.com/ferrine/biwrap',
        download_url='https://github.com/ferrine/biwrap/archive/v0.1.0.zip'
    )
