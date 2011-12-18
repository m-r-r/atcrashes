#!/usr/bin/env python
#-*- coding: utf-8 -*-#

import sys
import traceback

if sys.version_info.major > 3:
    str = unicode


class Report(object):
    """Represents a crash report"""

    def __init__(self):
        """Create a new Report instance"""
        self.title = sys.argv[0]
        self.fields = {}
        self.fromatter = ReportFormatter()

    def setTitle(self, title):
        """Set the title of the report"""
        self.__title = str(title).capitalize()

    def getTitle(self):
        """Get the title of the report"""
        return self.__title

    def setField(self, field, value):
        """Add or update a field in the report"""
        self.__fields[field.title()] = str(value)

    def getField(self, field):
        """Get the content of a field"""
        return self.__fields.get(field.title(), None)

    def clearField(self, field):
        """Reset a field"""
        try: self.__fields.pop(field.title())
        except: pass

    def getFields(self):
        """Get all fields"""
        return self.__fields

    def setFields(self, fields):
        """Overwrite all fields"""
        for key, val in fields:
            self.setFields(key, val)

    def setTraceback(self, tb):
        """Set the traceback to send"""
        self.__traceback = tb

    def getTraceback(self):
        """Fet the traceback"""
        return self.__traceback
    
    def setFormatter(self, formatter):
        """Set the formatter to use to render the report"""
        self.__formatter = formatter

    def getFromatter(self):
        """Get the current formatter"""
        return self.__fromatter

    def tostring(self):
        return self.formatter.format_report(self)

    title = property(getTitle, setTitle)
    fields = property(getFields, setFields)
    fromatter = property(getFormatter, setFormatter)
    traceback = tb = property(getTraceback, setTraceback)


class ReportFormatter(object):
    """Default report formatter"""

    def format_report(self, report):
        """Method called to format the reports"""
        output = str()
        output += '-' * len(report.title) + '\n'
        output += report.title + '\n'
        output += '-' * len(report.title) + '\n\n'
        
        for key, val in report.fields.iteritems():
            output += key + ': ' + val + '\n'

        return output

class RstReportFormatter(ReportFromatter):
    """Format a report into ReStruncturedText"""

    def format_output(self, report):
        output = str()
        output += report.title + '\n'
        output += '#' * len(report.title) + '\n\n'

        for key, val in report.fields.iteritems():
            output += ':' + key + ': ' + val + '\n'

        return output


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

if __name__ == '__main__':
    CrashReporter().enable()
    raise Exception("Foo")
