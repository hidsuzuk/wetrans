#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='wetrans',
    version='0.0.1',
    description='translation tool',
    #long_description=README.md,
    author='Hide Suzuki',
    install_requires=['googletrans'],
    author_email='hidsuzuk@pay2.jp',
    url='https://',
    license=license,
    entry_points={
        'console_scripts': [
            'wetrans=wetrans.wetrans:main',
        ],
    },
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests'
)



