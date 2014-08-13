#!/usr/bin/env python

#
#
#

import boolean2
from setuptools import setup

setup(name='BooleanNet',
      version='1.2.6',
      description='Boolean Network Simulation Toolbox',
      author='Istvan Albert',
      author_email='istvan.albert@gmail.com',
      url='http://code.google.com/p/booleannet/',
      packages=['boolean2', 'boolean2.ply', 'boolean2.plde'],
)
