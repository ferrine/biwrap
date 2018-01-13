#!/usr/bin/env python
from setuptools import setup, find_packages

DISTNAME = 'biwrap'
AUTHOR = 'Maxim Kochurov'
AUTHOR_EMAIL = 'maxim.v.kochurov@gmail.com'
VERSION = '0.0.0'


if __name__ == "__main__":
    setup(
        name=DISTNAME,
        version=VERSION,
        packages=find_packages()
    )
