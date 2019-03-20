#!/usr/bin/env sh

BRANCH=$1
REV=${2#r}  # Strip leading "r" from rev string
echo "The following revisions are eligible for merge:"
ELIGIBLE=$(svn mergeinfo --show-revs eligible ^/branches/$1)
echo "\t"$ELIGIBLE
if [[ ! $ELIGIBLE =~ (^|[[:space:]])r$REV($|[[:space:]]) ]]; then
	echo "Changeset r$REV is not eligible for merge"
	exit 0
fi
svn merge -c $REV ^/branches/$BRANCH .
if [[ $? = 0 ]]; then
	echo "\nCommit checklist:"
	echo " 1. Check correct version prefix (e.g. 1.2.4dev)"
	echo " 2. Add \"[skip ci]\" to skip build"
	echo " 3. Check correct issue references"
fi

