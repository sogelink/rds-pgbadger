#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(name='rdspgbadger',
      version='1.2.3+SGLK.SNAPSHOT',
      description=("Fetch logs from RDS postgres instance and use them with "
                   "pgbadger to generate a report."),
      url='http://github.com/fpietka/rds-pgbadger',
      author='François Pietka',
      author_email='francois@pietka.fr',
      license='MIT',
      packages=['package'],
      install_requires=['boto3>=1.4.0'],
      entry_points={
          'console_scripts': [
              'rds-pgbadger = package.rdspgbadger:main'
          ],
      },
      long_description=open('README.rst').read(),
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Environment :: Console',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6'
      ],
      zip_safe=True)
