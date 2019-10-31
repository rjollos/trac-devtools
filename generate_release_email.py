#!/usr/bin/env python

import argparse
import sys
import textwrap
import urllib2


files = (
    'Trac-%s.tar.gz',
    'Trac-%s-py2-none-any.whl',
    'Trac-%s.win32.exe',
    'Trac-%s.win-amd64.exe',
)

base_url = 'https://download.edgewall.org/trac'

descriptions = {
    'maintenance': 'latest maintenance release for the older stable branch',
    'stable': 'latest maintenance release for the current stable branch',
    'dev': 'latest development release leading up to Trac 1.4',
}

anchors = {
    'maintenance': 'Trac10StableRelease',
    'stable': 'Trac12StableRelease',
    'dev': 'LatestDevRelease',
}

template = """\
Trac %(version)s Released
====================

%(description)s

You will find this release at the usual places:

https://trac.edgewall.org/wiki/TracDownload#%(anchor)s

You can find the detailed release notes for %(version)s on the following
pages:
https://trac.edgewall.org/wiki/%(prefix)sTracChangeLog
https://trac.edgewall.org/wiki/TracDev/ReleaseNotes/%(mversion)s#MaintenanceReleases

Now to the packages themselves:

URLs:

%(url)s

MD5 sums:

%(md5)s

SHA256 sums:

%(sha)s

Acknowledgements
================

Many thanks to the growing number of people who have, and continue to,
support the project. Also our thanks to all people providing feedback
and bug reports that helps us make Trac better, easier to use and
more effective. Without your invaluable help, Trac would not evolve.
Thank you all.

Finally, we hope that Trac will be useful to like-minded programmers
around the world, and that this release will be an improvement over
the last version.

Please let us know.

/The Trac Team https://trac.edgewall.org/

"""


def main(version, release):

    def try_open(u):
        try:
            resp = urllib2.urlopen(u)
        except urllib2.HTTPError as e:
            print("%s for URL '%s'" % (e, u))
            sys.exit(1)
        return resp

    def get_hashes(h):
        hashes = []
        for f in files:
            resp = try_open('%s/%s.%s' % (base_url, f % version, h))
            hashes.append(resp.read().strip())
        return hashes

    md5_hashes = get_hashes('md5')
    sha_hashes = get_hashes('sha')

    urls = []
    for f in files:
        u = '%s/%s' % (base_url, f % version)
        try_open(u)
        urls.append(u)

    description = '\n'.join(textwrap.wrap(
        "Trac %s, the %s, is available." % (version, descriptions[release]),
        width=72))
    mversion = '.'.join(version.split('.')[0:2])
    print(template % {
        'url': '\n'.join(urls),
        'md5': '\n'.join(md5_hashes),
        'sha': '\n'.join(sha_hashes),
        'version': version,
        'mversion': mversion,
        'description': description,
        'prefix': '' if release == 'stable' else '%s/' % mversion,
        'anchor': anchors[release],
    })


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Generate body for a release email")
    parser.add_argument('version', help="Release version (ex: 1.3.1)")
    parser.add_argument('release', help="Release type",
                        choices=('maintenance', 'stable', 'dev'))
    args = parser.parse_args()
    main(args.version, args.release)
