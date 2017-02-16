#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: ipreacher
# Mail: ipreacher@hotmail.com
# Created Time:  2017-02-16 09:43:34 AM
#############################################

from setuptools import setup, find_packages

setup(
    name = 'Stock_WeChat',
    version = '0.0.4',
    keywords = ('test', 'stock', 'WeChat'),
    description = 'just a simple test',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
      ],
    license = 'MIT License',
    install_requires = ['tushare', 'itchat'],

    author = 'ipreacher',
    author_email = 'ipreacher@hotmail.com',
    url = "http://ipreacher.github.io",
    packages = find_packages(),
)
