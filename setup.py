#!/usr/bin/env python

import boolean2
from setuptools import setup

setup(name='BooleanNet',
      version='1.2.8',
      description='Boolean Network Simulation Toolbox',
      author='Istvan Albert',
      author_email='istvan.albert@gmail.com',
      url='https://github.com/ialbert/booleannet',
      packages=['boolean2', 'boolean2.ply', 'boolean2.plde'],
      install_requires=[
          'networkx', 'numpy'
      ],
)
