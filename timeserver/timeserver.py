#! /usr/bin/python2.7

import BaseHTTPServer
import argparse
import datetime
import httplib
import sys
import time

import trafficstats

__copyright__ = 'Copyright 2014 Systems Deployment, LLC'
__author__ = 'Morris Bernstein'
__email__ = 'morris@systems-deployment.com'


DEFAULT_PORT = 8080

time_page = """
<html>
<head>
<title>CSS 390 Time Server</title>
</head>
<body>
<p>
Current time: {}
</p>
</body>
</html>
"""


def run(stats, port=DEFAULT_PORT):
    class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
        def do_GET(self):
            {'/': self.do_time,
             '/fail': self.do_fail,
             '/stats': self.do_stats}.get(self.path, self.do_404)()
        def do_404(self):
            stats.increment('404s')
            self.send_error(httplib.NOT_FOUND, "Not found: {}".format(self.path))
        def do_fail(self):
            stats.increment('500s')
            self.send_error(httplib.INTERNAL_SERVER_ERROR, 'Internal error: {}'.format(self.path))
        def do_stats(self):
            self.send_response(httplib.OK)
            self.send_header('content-type', 'text/plain')
            self.end_headers()
            now = int(time.time())
            print 'stats: time', now
            self.wfile.write('time: {}\n'.format(now))
            for k, v in stats.stats.iteritems():
                print 'stats: ', k, v
                self.wfile.write('{}: {}\n'.format(k, int(v)))
        def do_time(self):
            stats.increment('200s')
            self.send_response(httplib.OK)
            self.send_header('content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(time_page.format(datetime.datetime.today().ctime()))

    server_address = ('', port)
    server = BaseHTTPServer.HTTPServer(server_address, Handler)
    sys.stderr.write('started server on port {}\n'. format(port))
    server.serve_forever()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port',
                        dest='port',
                        type=int,
                        default=DEFAULT_PORT)
    args = parser.parse_args()

    stats = trafficstats.Stats()
    run(stats, port=args.port)

