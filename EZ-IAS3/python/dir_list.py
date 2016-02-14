import os
import json

def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir\
    (path)]
    else:
        d['type'] = "file"
    return d

#print json.dumps(path_to_dict('.'), sort_keys=True, indent=4, separators=(',', ': '))

# generator that lists all files within given directory
def all_files(top):
    for root, dirs, files in os.walk(top, topdown=True):
        for name in files:
            yield os.path.join(root, name)
            

for f in all_files('.'):
    print f
    