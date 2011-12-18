#!/usr/bin/env python
#-*- coding: utf-8 -*-#

import sys
import traceback

from reports import Report

__all__ = ['Report', 'CrashReporter']

if sys.version_info.major < 3:
    from __builtin__ import unicode as str


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
