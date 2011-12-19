#!/usr/bin/env python
#-*- coding: utf-8 -*-#

from reports import *

if sys.version_info.major < 3:
    from __builtin__ import unicode as str


class BaseSender(object):
    """Base class for senders"""
    pass

__all__= ['BaseSender']
for cls in BaseSender.__subclasses__():
    __all__.append(cls.__name__)
