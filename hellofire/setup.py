#!/usr/bin/env python
# Copyright Vincent DAGOURY - 2020. BSD 3-Clause license, see LICENSE file.

import os
from setuptools import setup, find_packages

NAME = 'hellofire'
VERSION = '1.0'
URL='https://github.com/eattestations/ea-python-scripts',
SHORT_DESCRIPTION = """
e-Attestations' hello world using fire.""".strip()

def read_file(path):
    with open(os.path.join(os.path.dirname(__file__), path)) as fp:
        return fp.read()

setup(
    name=NAME,
    version=VERSION,
    url=URL,
    description=SHORT_DESCRIPTION,
    long_description=read_file('README.md'),
    
    keywords=
    'e-Attestations command line interface cli python fire interactive bash tool',
    
    author='Vincent DAGOURY',
    author_email='v.dagoury@e-attestations.com',
    license='BSD',
    
    python_requires='!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Terminals',
    ],
    packages=find_packages(),
    install_requires=['fire'],
    entry_points={
        "console_scripts": [
            "hellofire = hellofire.core:hellofire"
        ]
    }
    )
