#!/usr/bin/env python

import cep

from os.path import exists
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='django-cep',
    version=cep.__version__,
    maintainer='Thiago Carvalho D Avila',
    maintainer_email='thiagocavila@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    scripts=[],
    url='https://github.com/staticdev/django-cep',
    license='LICENSE',
    description='Address fields autofill app for forms using brazilian CEP field.',
    long_description=read('README.rst'),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        'Programming Language :: Python',
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "Django >= 1.2.0"
    ],
)
