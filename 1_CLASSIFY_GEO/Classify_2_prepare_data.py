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

for f in files:
    data = ch._load_and_process_gh_json(f)
    all_data.extend(data)


# TODO: WRITE ALL_DATA TO A FILE OF CHOOSING
print all_data[44]
print len(all_data)
