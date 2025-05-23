#!/usr/bin/env python
from substack_api import Newsletter
import sys
import ujson

# Initialize a newsletter by its URL
newsletter = Newsletter(sys.argv[1])

#recent_posts = newsletter.get_posts(limit=5)
#top_posts = newsletter.get_posts(sorting="top", limit=10)
#search_results = newsletter.search_posts("machine learning", limit=3)
#podcasts = newsletter.get_podcasts(limit=5)
#recommendations = newsletter.get_recommendations()
#authors = newsletter.get_authors()

# 'endpoint', 'get_raw_data', 'get_subscriptions', 'id', 'name', 'profile_set_up_at', 'username']

for author in newsletter.get_authors():
    print(sys.argv[1] + " " +ujson.dumps(author.username))
