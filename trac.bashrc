#!/bin/bash

dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Grep python
gp () {
  grep -R --include=\*\.py "$1" .
}
# Grep source
gs () {
  grep -R --exclude-dir=./build --exclude-dir=./.svn --exclude-dir=./.git --exclude-dir=./Trac.egg-info --exclude-dir=./trac/locale --exclude=\*\.pyc "$1" .
}

pyenv shell trac-2.7.15
export PATH=$dir/bin:$PATH
export ENVS=$dir/tracenvs
