#!/usr/bin/env python
import os
import sys

if len(sys.argv) == 1:
    files = []
    for f in os.listdir('.'):
        if not f.startswith('.'):
            files.append(f)
    print(' '.join(files))
elif len(sys.argv) == 2:
    if sys.argv[1] == '-a' or sys.argv[1] == '-all':
        print(' '.join(os.listdir('.')))
    else:
        files = []
        path = os.path.join('.', sys.argv[1])
        for f in os.listdir(path):
            if not f.startswith('.'):
                files.append(f)
        files.sort()
        print(' '.join(files))
elif len(sys.argv) == 3:
    path = os.path.join('.', sys.argv[2])
    print(' '.join(os.listdir(path).sort()))
