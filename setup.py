#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import datetime

VERSION_MAJOR = 0
VERSION_MINOR = "{:%Y%m%d%H%M%S}".format(datetime.datetime.utcnow())  # Use timestamp as minor version during beta
VERSION = '{VERSION_MAJOR}.{VERSION_MINOR}'.format_map(locals())


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
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
)
