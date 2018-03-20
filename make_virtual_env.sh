#!/usr/bin/env sh

pve=${1:-pve}
if [[ ! -d $pve ]]; then
    python2.7 -m virtualenv pve
    source pve/bin/activate
fi

pip install -U -r requirements-dev.txt

svn_python=$(locate -l 1 svn-python) > /dev/null
site_packages="$pve/lib/python2.7/site-packages"

# Remove invalid symbolic links.
find "$site_packages/svn" -type l ! -exec test -e {} \; -exec rm {} \;
find "$site_packages/libsvn" -type l ! -exec test -e {} \; -exec rm {} \; -exec rm "$site_packages/svn.pth" \;

# Create new symbolic links
[ ! -h "$site_packages/svn" ] && ln -s "$svn_python/svn" "$site_packages/"
[ ! -h "$site_packages/libsvn" ] && ln -s "$svn_python/libsvn" "$site_packages/"
[ ! -f "$site_packages/svn.pth" ] &&  echo "$svn_python/libsvn" > "$site_packages/svn.pth"
