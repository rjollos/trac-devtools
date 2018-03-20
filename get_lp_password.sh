#!/usr/bin/env python

from subprocess import Popen, PIPE


if __name__ == '__main__':
    proc = Popen(['lpass', 'show', '--sync', 'no', '--password',
                  'Edgewall/trac-hacks.org'],
                 stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = proc.communicate()
    if proc.returncode == 0:
        print(stdout)
    else:
        print('ERROR: ', stderr)
    proc.stdout.close()
    proc.stderr.close()
