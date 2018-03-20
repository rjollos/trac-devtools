#!/usr/bin/env python

import argparse
import subprocess
import sys

import xmlrpclib

trac_url = 'https://rjollos:%s@trac-hacks.org/login/rpc'


def main(ticket_id, filename):
    passwd = get_lp_password()
    if passwd is None:
        sys.exit(1)
    server = xmlrpclib.ServerProxy(trac_url % passwd)
    with open(filename) as f:
        file = xmlrpclib.Binary(f.read())
        server.ticket.putAttachment(ticket_id, filename, '', file)


def get_lp_password():
    proc = subprocess.Popen(['lpass', 'show', '--sync', 'no', '--password',
                             'Edgewall/trac-hacks.org'],
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    proc.stdout.close()
    proc.stderr.close()
    if proc.returncode == 0:
        return stdout.strip()
    else:
        print('ERROR: ', stderr)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        "Upload attachment to ticket on trac-hacks.org")
    parser.add_argument('ticket_id', type=int, help="Ticket id")
    parser.add_argument('filename', help="Attachment filename")
    args = parser.parse_args()
    main(args.ticket_id, args.filename)
