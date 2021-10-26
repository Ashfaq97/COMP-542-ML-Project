# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='TextCompletion',
    version='0.0.0',
    description='Text Completion Project',
    long_description=readme,
    url='https://github.com/Joekeen03/COMP-542-ML-Project',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
