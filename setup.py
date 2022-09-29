# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     setup.py
   Description :
   Author :       liaozhaoyan
   date：          2022/9/28
-------------------------------------------------
   Change Activity:
                   2022/9/28:
-------------------------------------------------
"""
__author__ = 'liaozhaoyan'

VERSION = '0.1.2'

import sys
from setuptools import setup

if sys.version_info.major == 2:
    reqLists = ["pip==20.3.4", "requests", "protobuf==3.15.0", "python-snappy==0.6.1"]
else:
    reqLists = ["protobuf==3.15.0", "python-snappy==0.6.1"]

setup(name='prometheus-writer',
      version=VERSION,
      description="prometheus remote writer.",
      long_description='prometheus remote writer.',
      classifiers=["Topic :: System :: Operating System Kernels :: Linux",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.5",
                   "Programming Language :: Python :: 3.6",
                   "Programming Language :: Python :: 3.7",
                   "Programming Language :: Python :: 3.8",
                   "Programming Language :: Python :: 3.9",
                   "Programming Language :: Python :: 3.10",
                   "Programming Language :: Python :: Implementation :: PyPy",
                   ],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='prometheus remote writer',
      author='liaozhaoyan',
      author_email='zhaoyan.liao@linux.alibaba.com',
      url="https://github.com/liaozhaoyan/prometheus-writer",
      license='Apache',
      packages=["prometheus"],
      include_package_data=True,
      zip_safe=True,
      install_requires=reqLists,
      entry_points={
      }
      )

if __name__ == "__main__":
    pass
