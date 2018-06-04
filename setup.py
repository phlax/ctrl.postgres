#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python ctrl.postgres
"""

from setuptools import setup


install_requires = [
    'ctrl.core',
    'ctrl.command',
    'asyncpg']

extras_require = {}
extras_require['test'] = [
    "pytest",
    "pytest-mock",
    "coverage",
    "pytest-coverage",
    "codecov",
    "flake8"],

setup(
    name='ctrl.postgres',
    version='0.0.1',
    description='ctrl.postgres',
    long_description="ctrl.postgres",
    url='https://github.com/phlax/ctrl.postgres',
    author='Ryan Northey',
    author_email='ryan@synca.io',
    license='GPL3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        ('License :: OSI Approved :: '
         'GNU General Public License v3 or later (GPLv3+)'),
        'Programming Language :: Python :: 3.5',
    ],
    keywords='python ctrl',
    install_requires=install_requires,
    extras_require=extras_require,
    packages=['ctrl.postgres'],
    include_package_data=True)
