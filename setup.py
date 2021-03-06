# -*- coding: utf-8 -*-
# $Id$
from setuptools import setup, find_packages
import os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read().strip()


name = 'openxmllib-py3'

long_description = "\n\n".join((
    read('README.rst'),
    read('doc', 'source', 'TODO.txt'),
    read('doc', 'source', 'HISTORY.txt')))

setup(
    name=name,
    version=read('openxmllib', 'version.txt'),
    description='Provides resources to handle OpenXML documents.',
    long_description=long_description,
    author='Wilberto Morales',
    author_email='wilbertomorales777@gmail.com',
    url='https://github.com/wilbertom/openxmllib-py3',
    license="GPLv2",
    keywords='Python OpenXML lxml Office2007 ECMA376',
    classifiers=[
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Topic :: Office/Business :: Office Suites",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Indexing",
        "Programming Language :: Python"
    ],
    packages=['openxmllib'],
    include_package_data=True,
    exclude_package_data={
        '': ['tests']
    },
    install_requires=['lxml>=3.4.0'],
    zip_safe=False,
    entry_points={
        'console_scripts': ['openxmlinfo = openxmllib.shell:openxmlinfo']
    },
)
