#!/usr/bin/env python
#-*- coding: utf-8 -*-#

import sys

if sys.version_info.major < 3:
    from __builtin__ import unicode as str

class BaseFormatter(object):
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

__all__= ['BaseFormatter']
for cls in BaseFormatter.__subclasses__():
    __all__.append(cls.__name__)

