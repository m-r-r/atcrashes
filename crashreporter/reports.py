#!/usr/bin/env python
#-*- coding: utf-8 -*-#

import os
import sys
import platform
import traceback

from formatters import *

if sys.version_info.major < 3:
    from __builtin__ import unicode as str


class BaseReport(object):
    """Represents a crash report"""

    def __init__(self, title=None, fields=None, formatter=None):
        """Create a new Report instance"""
        self._title = title or sys.argv[0]
        self._fields = fields or dict()
        self._fromatter = formatter or BaseFormatter()

    def setTitle(self, title):
        """Set the title of the report"""
        self._title = str(title).capitalize()

    def getTitle(self):
        """Get the title of the report"""
        return self._title

    def setField(self, field, value):
        """Add or update a field in the report"""
        self._fields[field.title()] = str(value)

    def getField(self, field):
        """Get the content of a field"""
        return self._fields.get(field.title(), None)

    def clearField(self, field):
        """Reset a field"""
        try: self._fields.pop(field.title())
        except: pass

    def getFields(self):
        """Get all fields"""
        return self._fields

    def setFields(self, fields):
        """Overwrite all fields"""
        for key, val in fields.iteritems():
            self.setField(key, val)

    def setTraceback(self, tb):
        """Set the traceback to send"""
        self._traceback = tb

    def getTraceback(self):
        """Fet the traceback"""
        return self._traceback
    
    def setFormatter(self, formatter):
        """Set the formatter to use to render the report"""
        self._formatter = formatter

    def getFormatter(self):
        """Get the current formatter"""
        return self._fromatter

    def tostring(self):
        return self.formatter.format_report(self)
    
    def __add__(self, other):
        self.fields = other.fields
        other.fields = self.fields
        return self

    def __sub__(self, other):
        for field in other.fields.keys():
            self.clearField(fields)
        return self

    title = property(getTitle, setTitle)
    fields = property(getFields, setFields)
    formatter = property(getFormatter, setFormatter)
    traceback = tb = property(getTraceback, setTraceback)
    __str__ = __repr__ = tostring


class Python(BaseReport):
    def __init__(self, *args, **kwargs):
        BaseReport.__init__(self, *args, **kwargs)

        self.setField("python version", sys.version)
        self.setField("python executable", sys.executable)

class Platform(BaseReport):
    def __init__(self, *args, **kwargs):
        BaseReport.__init__(self, *args, **kwargs)

        self.setField("platform", platform.platform())
        self.setField("architechture", platform.machine() + ' ' + ' '.join(platform.architecture()))
        self.setField("python implementation", platform.python_implementation())
        self.setField("path", os.environ.get('PATH'))

__all__= ['BaseReport']
for cls in BaseReport.__subclasses__():
    __all__.append(cls.__name__)
