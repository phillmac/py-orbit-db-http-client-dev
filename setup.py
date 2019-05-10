#!/usr/bin/env python

from orbitdbapi import __version__
from setuptools import setup, find_packages

setup(
    name='orbitdbapi',
    version=__version__,
    description='A Python HTTP Orbitdb API Client',
    author='Phillip Mackintosh',
    url='https://github.com/phillmac/py-orbit-db-http-client',
    packages=find_packages(),
    install_requires=[
        'requests >= 2.11'
        ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)