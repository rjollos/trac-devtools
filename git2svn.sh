#!/usr/bin/env sh

branch=$1

rm -rf .svn
svn up ../trac-$branch
cp -R ../trac-$branch/.svn .

