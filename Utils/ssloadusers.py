#!/usr/bin/env python3
import argparse
import math
import re
import substsna
import time
from scipy.stats.mstats import gmean

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
    args.collection = "allusers"

#######################################################
ardb = substsna.mkarango("substack")

if(ardb.has_graph(args.collection)):
    myg = ardb.graph(args.collection)
else:
    myg = ardb.create_graph(args.collection)
    print("created " + args.collection)

if(myg.has_vertex_collection(args.collection + "authors")):
    myn = myg.vertex_collection(args.collection + "authors")
else:
    myn = myg.create_vertex_collection(args.collection + "authors")
    print("created " + args.collection + "authors")

# need id_str AND screen_name
myindex = myn.add_hash_index(fields=["id_str"],unique=True)

if not myg.has_edge_definition(args.collection + "follows"):
    myfol = myg.create_edge_definition(
        edge_collection=args.collection + "follows",
        from_vertex_collections=[args.collection + "authors"],
        to_vertex_collections=[args.collection + "authors"])
    print("created graph for " + args.collection)
else:
    myfol = myg.edge_collection(args.collection + "follows")

if not myn.has(resp['id_str']):
    user = {}
    try:
        desc = re.sub(",|\n", "", resp['description'])
    except:
        desc = ""
    user['_key'] = resp['id_str']
    user['id_str'] = resp['id_str']
    user['screen_name'] = resp['screen_name']
    myn.insert(user)
