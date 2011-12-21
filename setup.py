#!/usr/bin/env python
#-*- coding: utf-8 -*- #

from distutils.core import setup
import sys

setup(
    name = "atcrashes",
    version = "0.1a",
    description = "Like atexit, but for crashes",
    url = "http://github.com/Skami18/atcrashes",
    author = "Mickaël Raybaud-Roig",
    author_email = "skami18.mrr@gmail.com",
    py_modules = ['atcrashes'],
    classifiers = [
        'Programming Language :: Python',
        'Intended Audience :: Developers'
    ]
)

