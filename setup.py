#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import platform
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

VERSION_MAJOR = 1
VERSION_MINOR = 2
VERSION = '{VERSION_MAJOR}.{VERSION_MINOR}'.format_map(locals())

python_version_major, python_version_minor, _ = platform.python_version_tuple()

if python_version_major < 3:
    print("Environmental doesn't support Python 2")

requires = []
if python_version_major == 3 and python_version_minor < 5:  # if version is below 3.5
    requires.append('typing')

class PyTest(TestCommand):

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.cov = None
        self.pytest_args = ['--cov', 'environmental', '--cov-report', 'term-missing']

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='environmental',
    packages=find_packages(),
    version=VERSION,
    description='Map a python configuration from environment variables',
    long_description=open('README.rst').read(),
    author='Zalando SE',
    url='https://github.com/zalando/environmental',
    license='Apache License Version 2.0',
    requires=requires,
    tests_require=['pytest-cov', 'pytest'],
    cmdclass={'test': PyTest},
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
)
