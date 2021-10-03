#!/usr/bin/env python3

import urllib.request, json
import sys

# Configure API request
try:
    API_key = sys.argv[1]
except IndexError:
    API_key = '-1'
    print(f'No API key specified', file=sys.stderr)
print("key entered:\n" + API_key)
endpoint = "https://developer.nps.gov/api/v1/alerts?parkCode=acad"
HEADERS = {"Authorization":API_key}
req = urllib.request.Request(endpoint,headers=HEADERS)
try:
   response = urllib.request.urlopen(req)

except urllib.error.HTTPError as e:
    print(e)  #getting a 403 error 
