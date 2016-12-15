#!/usr/bin/env python

from os.path import exists
from setuptools import setup, find_packages

setup(
    name='aksorn',
    version=open('VERSION').read().strip(),
    # Your name & email here
    author='Praphan Klairith',
    author_email='p.klairih@gmail.com',
    # If you had aksorn.tests, you would also include that in this list
    packages=find_packages(),
    # Any executable scripts, typically in 'bin'. E.g 'bin/do-something.py'
    scripts=[],
    # REQUIRED: Your project's URL
    url='',
    # Put your license here. See LICENSE.txt for more information
    license='',
    # Put a nice one-liner description here
    description='',
    long_description=open('README.rst').read() if exists("README.rst") else "",
    # Any requirements here, e.g. "Django >= 1.1.1"
    install_requires=[
        
    ],
    # Ensure we include files from the manifest
    include_package_data=True,
)
