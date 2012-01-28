#!/usr/bin/env python


# import std
import os
from os import path
import re
import sys
# import third party
try:
    from setuptools import setup, find_packages
except ImportError:
    try:
        from ez_setup import use_setuptools
    except ImportError:
        print "can't find ez_setup"
        print "try: wget http://peak.telecommunity.com/dist/ez_setup.py"
        sys.exit(1)
    use_setuptools()
    from setuptools import setup, find_packages

if sys.version_info < (2, 6):
    print "occupyboard supports Python 2.6 and higher"
    sys.exit(1)

sys.path.append(path.join(path.dirname(__file__), 'src'))

__version__ = '0.1'
__author__  = 'TheOccupyBoard Development Team'
__package_data__ = [
    'README.rst',
    'Changelog',
    'License',
    'Makefile',
    'buildout'
]
__namespace_packages__ = [
    'occupyboard',
    'occupyboard.identity'
]


setup(
    name = 'occupyboard.identity',
    version = __version__,
    author = __author__,
    author_email = 'team-dev@theoccupyboard.com',
    description = 'occupyboard',
    long_description = open('README.rst').read(),
    url = 'http://blog.theoccupyboard.com',
    platforms = ["Python >= 2.6"],
    license = 'Apache Software License',
    namespace_packages = __namespace_packages__,
    package_dir = {'': 'src'},
    packages = find_packages('src'),
    package_data = {'': __package_data__},
    include_package_data = True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points = {
        'console_scripts': [
            'occ-daemon=occupyboard.web.daemon:main'
        ]
    },
    install_requires=[
          'setuptools',
          'bottle',
          'ldapom',
          'PyYAML'
    ]
)

