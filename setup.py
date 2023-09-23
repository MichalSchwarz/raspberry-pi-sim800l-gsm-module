#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='Sim800l',
      version='1.0.6',
      description='SIM 800l',
      author='https://github.com/jakhax',
      author_email='jackogina60@gmail.com',
      url='https://github.com/MichalSchwarz/raspberry-pi-sim800l-gsm-module',
      packages=find_packages(exclude=['tests', 'tests.*']),
      install_requires=[
          'pyserial',
      ],
     )
