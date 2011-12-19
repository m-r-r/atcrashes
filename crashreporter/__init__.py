#!/usr/bin/env python
#-*- coding: utf-8 -*-#

import sys
import traceback

from reports import *
from fromatters import *

__all__ = reports.__all__ + formatters.__all__ + ["enable", "disable", "crashreporter"]

if sys.version_info.major < 3:
    from __builtin__ import unicode as str



class CrashReporter(object):
    """The main class of the module"""

    def __init__(self, *args, **kwargs):
        """Creates a new crash reporter"""
        pass
    
    def __excepthook__(self, exc_type, value, traceback):
        print("Pwned")
        pass

    def enable(self):
        """Install the crash reporter in sys.excepthook"""
        sys.excepthook = self.__excepthook__
 
    def disable(*args, **kwargs):
        """Deactivate the crash reporter"""
        sys.excepthook = sys.__excepthook__


def enable(*args, **kwargs):
    CrashReporter().enable()

def disable(*args, **kwargs):
    CrashReporter().disable()
    
if __name__ == '__main__':
    enable()
    raise Exception("Foo")
