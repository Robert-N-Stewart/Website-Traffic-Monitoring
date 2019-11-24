#! /usr/bin/python

import threading
import sys

__copyright__ = 'Copyright 2014 Systems Deployment, LLC'
__author__ = 'Morris Bernstein'
__email__ = 'morris@systems-deployment.com'


class Stats(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.stats = {'200s': 0.0,
                      '404s': 0.0,
                      '500s': 0.0}
        self.verbose = False

    def __enter__(self):
        self.lock.acquire()

    def __exit__(self, type, value, traceback):
        self.lock.release()
        return False

    def increment(self, var, count=1):
        if self.verbose:
            sys.stderr.write('stats: incrementing {}: {}\n'.format(var, count))
        with self:
            self.stats[var] += count


