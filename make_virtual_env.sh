#!/usr/bin/env sh

if [[ -L "$0" ]]; then
    DIR=$(dirname "$(readlink "$0")")
else
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
fi

if [[ $(pyenv version-name) == 'system' ]]; then
    echo "No pyenv activated"
    exit 1
fi
#pve=${1:-pve}
#if [[ ! -d $pve ]]; then
#    python2.7 -m virtualenv pve
#    source pve/bin/activate
#fi

pip install -U -r $DIR/trac-requirements-dev.txt
pip install -U -r teo-rjollos.git/requirements-release.txt

svn_python=$(locate -l 1 svn-python) > /dev/null
site_packages=$(python -c "import os; print(os.path.dirname(os.__file__) + '/site-packages')")
echo $site_packages

# Create new symbolic links
ln -sf "$svn_python/svn" "$site_packages/"
ln -sf "$svn_python/libsvn" "$site_packages/"
echo "$svn_python/libsvn" > "$site_packages/svn.pth"
