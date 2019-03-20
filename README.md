# Trac development tools

## Clone repository

    git clone https://svn.edgewall.org/git/trac/devs/rjollos teo-rjollos.git
    git config --local include.path ~/devtools/trac.gitconfig

## Install pyenv and pyenv-virtualenv

    $ brew install pyenv pyenv-virtualenv pyenv-virtualenvwrapper
    $ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\n  eval "$(pyenv virtualenv-init -)"\nfi' >> ~/.bash_profile

## Install some Python versions

    $ pyenv install 2.6.9
    $ pyenv install 2.7.14

## Create and activate a virtualenv

    $ pyenv virtualenv 2.7.14 trac-2.7
    $ pyenv activate trac-2.7

    $ pyenv version
    trac-2.7 (set by PYENV_VERSION environment variable)

## Install old Python on Ubuntu

    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt-get update
    sudo apt-get install python2.6 python2.6-dev
