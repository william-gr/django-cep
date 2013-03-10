#!/usr/bin/env python

from os.path import exists
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from cep import __version__

setup(
    name='django-cep',
    version=__version__,
    packages=['cep'],
    scripts=[],
    url='https://github.com/staticdev/django-cep',
    license='LICENSE.txt',
    description='Address fields autofill app for forms using brazilian CEP field.',
    long_description=open('README.markdown').read() if exists("README.markdown") else "",
    install_requires=[
        "Django >= 1.2.0"
    ],
)
