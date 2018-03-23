#!/usr/bin/env python

import argparse
import os
import sys

import xmlrpclib
import utils


def main(ticket_id, output_dir):
    passwd = utils.get_lp_password()
    if passwd is None:
        sys.exit(1)
    server = xmlrpclib.ServerProxy(utils.trac_url % passwd)
    for attrs in server.ticket.listAttachments(ticket_id):
        filename = attrs[0]
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        filepath = os.path.join(output_dir, filename)
        print(filepath)
        with open(filepath, 'wb') as f:
            file = server.ticket.getAttachment(ticket_id, filename)
            f.write(file.data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        "Get attachments from ticket on trac-hacks.org")
    parser.add_argument('ticket_id', type=int, help="Ticket id")
    parser.add_argument('output_dir', nargs='?', default='.',
                        help="Output directory")
    args = parser.parse_args()
    main(args.ticket_id, args.output_dir)
