#!/usr/bin/env python

from sregistry.utils import run_command
import json
import pickle

# Read in list of prefixes

words = json.load(open('search-terms.json','r'))

containers = []
count = 0
start = 0
save_index = 0
for w in range(start, len(words)):
    word = words[w]
    res = run_command(['docker', 'search', '--limit', '100', word])

    # If we hit 50K, save to new file
    if count % 50000 == 0:
        pickle.dump(containers, open('containers_%s.pkl' %save_index, 'wb'))
        containers = []
        save_index+=1

    # If a delimiter of 100, save to index
    elif count % 100 == 0:
        pickle.dump(containers, open('containers_%s.pkl' %save_index, 'wb'))
    if res['return_code'] == 0:
        res = res['message']
        lines = res.split('\n')[1:-1]
        for line in lines:
            container = line.split(' ')[0].strip()
            if container not in containers:
                num = len(containers) + 1
                print("Adding %sth container, %s" %(num, container))
                containers.append(container)
    count+=1

# One final save!
pickle.dump(containers, open('containers.pkl','wb'))
