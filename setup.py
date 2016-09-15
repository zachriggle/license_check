#!/usr/bin/env python2
import glob
import os
import platform
import sys
from distutils.command.install import INSTALL_SCHEMES
from distutils.sysconfig import get_python_inc
from distutils.util import convert_path

from setuptools import find_packages
from setuptools import setup

setup(
    name                 = 'license-check',
    packages             = find_packages(),
    version              = '0.1',
    package_data         = {
        'license_check': [
            'check.sh',
        ],
    },
    entry_points         = {'console_scripts': ['license_check=license_check:main']},
    description          = "Recursive license checker.",
    author               = "Zach Riggle",
    url                  = 'https://github.com/zachriggle/license-check',
    install_requires     = ['virtualenv'],
    license              = "MIT",
    keywords             = 'license check mit gpl bsd gplv2 gplv3 legal',
    classifiers          = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ]
)
