#!/usr/bin/env python
from substack_api import User
import sys
import ujson

# Initialize a user by their username
user = User(sys.argv[1])

# Get user profile information
profile_data = user.get_raw_data()
print(ujson.dumps(profile_data))