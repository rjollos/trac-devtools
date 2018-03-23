#!/usr/bin/env python

import argparse
import sys

import xmlrpclib
import utils


def main(ticket_id, filename):
    passwd = utils.get_lp_password()
    if passwd is None:
        sys.exit(1)
    server = xmlrpclib.ServerProxy(utils.trac_url % passwd)
    with open(filename) as f:
        file = xmlrpclib.Binary(f.read())
        server.ticket.putAttachment(ticket_id, filename, '', file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        "Upload attachment to ticket on trac-hacks.org")
    parser.add_argument('ticket_id', type=int, help="Ticket id")
    parser.add_argument('filename', help="Attachment filename")
    args = parser.parse_args()
    main(args.ticket_id, args.filename)
