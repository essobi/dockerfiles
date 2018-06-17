#!/usr/bin/env python

import os
import sys

database = 'data'
if len(sys.argv) > 1:
    database = sys.argv[1]

if not os.path.exists(database):
    print('Cannot find, %s exiting.' %database)
    sys.exit(1)


print('Preparing to count Dockerfiles in %s' % database)
database = os.path.abspath(database)
count = 0
for root, dirs, files in os.walk(database):
    path = root.split(os.sep)
    for file in files:
        if 'Dockerfile' in file:
            count+=1
            sys.stdout.write('\r' + str(count))
            sys.stdout.flush()

print('Found a total of %s Dockerfiles!' %count)
