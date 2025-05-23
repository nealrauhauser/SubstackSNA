#!/usr/bin/env python3
import argparse
import math
import re
import substsna
import sys
from substack_api import Newsletter

src = re.sub(".substack.com", "", sys.argv[1])
src = re.sub("http://", "", src)
newsletter = Newsletter("http://" + src + ".substack.com/")
recommendations = newsletter.get_recommendations()

for rec in recommendations:
    #print(dir(rec))
    print(src + "," + rec.url)
    try:
        if re.search("substack.com", rec.url):
            src2 = re.sub(".substack.com", "", rec.url)
            recs2 = Newsletter("http://" + rec.url)
            for r2 in recs2.get_recommendations():
                print(src2 + "," + r2.url)
    except:
        pass