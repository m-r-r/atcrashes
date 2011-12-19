#!/usr/bin/env python
#-*- coding: utf-8 -*- #

from distutils.core import setup
import sys

setup(
    name = "crashreporter",
    version = "0.1a",
    description = "Send a crash report when an application crash",
    url = "http://github.com/Skami18/CrashReporter",
    author = "Mickaël Raybaud-Roig",
    author_email = "skami18.mrr@gmail.com",
    packages = ['crashreporter'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Intended Audience :: Developers'
    ]
)

