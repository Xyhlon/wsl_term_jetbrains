yourpath = '/mnt/c/usr/local/bin'

import os
import re
import stat

for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:
        file = os.path.join(root, name)
        cmd = name.split('.')[0]
        with open(file) as f:
            for line in f:
                for word in line.split():
                    pat = re.compile(r'.:\\.')
                    found = pat.search(word)
                    if found:
                        path = '/mnt/c' + word.replace('\\','/').replace("C:","")
                        print(found.groups())
        with open('/bin/{}'.format(cmd), 'w') as temp_file:
            temp_file.write("#!/bin/bash \n" + path)

        print(stat.ST_UID+stat.ST_GID)
        os.chmod('/bin/{}'.format(cmd), 0o755)




