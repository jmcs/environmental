#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

VERSION_MAJOR = 1
VERSION_MINOR = 0
VERSION = '{VERSION_MAJOR}.{VERSION_MINOR}'.format_map(locals())


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
