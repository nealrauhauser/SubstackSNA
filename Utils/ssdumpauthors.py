#!/usr/bin/env python3
import argparse
import configparser
import math
import re
import substsna
import time
import ujson
from arango import ArangoClient

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", help="enable debugging output")
parser.add_argument("-c", "--collection", help="collection other than allusers")
args = parser.parse_args()

if(args.debug):
    DEBUG = True
else:
    DEBUG = False

if args.collection:
    pass
else:
    args.collection = "nealrsubs"

ardb = substsna.mkarango("substack")

col = ardb.collection(args.collection)

for thing in col:
    peep = thing['handle']
    print("nealr,"+thing['handle'])
    for sub in thing['subscriptions']:
        #print(ujson.dumps(sub))
        print(peep + "," + sub['publication']['subdomain'])
