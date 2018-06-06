#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2018 Absolute Performance Inc <csteam@absolute-performance.com>.

from setuptools import setup

with open('README.rst', 'r') as file:
    long_description = file.read()

setup(
    name='req',
    version='0.0.3',
    description='Simple format for serialization, similar to json.  Not useful for most general use.',
    long_description=long_description,
    author='Taylor C. Richberger',
    author_email='tcr@absolute-performance.com',
    url='https://github.com/absperf/python-req',
    license='MIT',
    py_modules=[
        'req',
        ],
    install_requires=[
        'six',
        ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        ],
)
