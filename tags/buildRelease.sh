#!/bin/sh

if [ $# -lt 1 ]; then
    echo "Usage: buildRelease.sh DIR"

    exit 1
fi

DIR=`basename $1`

find $DIR | xargs chmod a+r
find $DIR -type d | xargs chmod a+x

tar --exclude=".svn*" -czf $DIR.tar.gz $DIR
