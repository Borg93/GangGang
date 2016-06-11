import sys
import Classify_helpers as ch
import json
import os
import collections

from pprint import pprint


if len(sys.argv) < 3:
    print "AS ARGUMENTS: output file & training files to join"

writefiles = sys.argv[1]
files = sys.argv[2:]

all_data = []


def dict_unicode_to_str(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(dict_unicode_to_str, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(dict_unicode_to_str, data))
    else:
        return data

def process_gh_json(data):

    #    data = dict_unicode_to_str(data) #TODO: FIGURE OUT HOW TO REMOVE THIS

    for d in data:
        d.update({'geometry':filebase})

    return data

for f in files:
    filebase = os.path.splitext(f)[0]
    with open(f) as fp:
        data = json.load(fp)

        data = process_gh_json(data)

        all_data.extend(data)


# TODO: WRITE ALL_DATA TO A FILE OF CHOOSING
print all_data[3]
print len(all_data)
