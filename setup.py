#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for zefram package.

"""

from setuptools import setup, find_packages

# Change these settings according to your needs
MAIN_PACKAGE = "zefram"
DESCRIPTION = "Database of zeolite framework characteristics"
LICENSE = "MIT"
URL = "https://bitbucket.org/lukaszmentel/zefram"
AUTHOR = "Lukasz Mentel"
EMAIL = "lmmentel@gmail.com"
VERSION = '0.1.3'

# Add here all kinds of additional classifiers as defined under
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = ['Development Status :: 4 - Beta',
               'Programming Language :: Python',
               'Topic :: Scientific/Engineering :: Chemistry',
               'Topic :: Scientific/Engineering :: Physics']

def readme():
    '''Return the contents of the README.rst file.'''
    with open('README.rst') as freadme:
        return freadme.read()

def setup_package():

    setup(name=MAIN_PACKAGE,
          version=VERSION,
          url=URL,
          description=DESCRIPTION,
          author=AUTHOR,
          author_email=EMAIL,
          include_package_data=True,
          license=LICENSE,
          long_description=readme(),
          classifiers=CLASSIFIERS,
          packages=find_packages(exclude=['tests', 'tests.*']),
          install_requires=[
              'SQLAlchemy',
              'numpy',
          ],
          entry_points = {
              'console_scripts': [
                  'getcif.py = zefram.zefram:cli_getcif',
                  'printframework.py = zefram.zefram:cli_print_framework',
               ],
          }
    )

if __name__ == "__main__":
    setup_package()
