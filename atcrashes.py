#!/usr/bin/env python
#-*- coding: utf-8 -*-#
"""
atcrashes.py - allow programmer to define multiple functions to be executed
upon anormal program termination.
"""

import sys, traceback

_crashhandlers = []
__all__ = ["register"]

def _run_crashhandlers(*args):
    """run any registered crash functions

    _crashhandlers is traversed in reverse order so functions are executed
    last in, first out.
    """

    exc_info = None
    while _crashhandlers:
        func, args, kwargs = _crashhandlers.pop()
        try:
            apply(func, args, kwargs)
        except:
            import traceback
            print >> sys.stderr, "Error in atcrash._run_crashhandlers:"
            traceback.print_exc()
            exc_info = sys.exc_info()

    if exc_info is not None:
        raise exc_info[0], exc_info[1], exc_info[2]


def register(func, *args, **kwargs):
    """register a function to be executed upon normal program termination

    func - function to be called if the program crash
    args - optional arguments to pass to func
    kwargs - optional keyword arguments to pass to func

    func is returned to facilitate usage as a decorator.
    """
    if not callable(func): 
        raise TypeError('Argument #1 must be a callable')

    _crashhandlers.append((func, args, kwargs))
    return func

if hasattr(sys, "excepthook"):
    sys.excepthook = _run_crashhandlers

if __name__ == "__main__":
    def x1():
        print "running x1"
    def x2(n):
        print "running x2(%r)" % (n,)
    def x3(n, kwd=None):
        print "running x3(%r, kwd=%r)" % (n, kwd)

    register(x1)
    register(x2, 12)
    register(x3, 5, "bar")
    register(x3, "no kwd args")

    raise Exception()
