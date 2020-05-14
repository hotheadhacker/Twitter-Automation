#!/usr/bin/env python

# -----------------------------------------------------------------------
# twitter-trends
#  - lists the current global trending topics
# -----------------------------------------------------------------------

import config
from twitter import *

# -----------------------------------------------------------------------
# load our API credentials
# -----------------------------------------------------------------------
import sys
sys.path.append(".")

# -----------------------------------------------------------------------
# create twitter API object
# -----------------------------------------------------------------------
twitter = Twitter(auth=OAuth(config.access_key,
                             config.access_secret,
                             config.consumer_key,
                             config.consumer_secret))

# -----------------------------------------------------------------------
# retrieve global trends.
# other localised trends can be specified by looking up WOE IDs:
#   http://developer.yahoo.com/geo/geoplanet/
# twitter API docs: https://dev.twitter.com/rest/reference/get/trends/place
# -----------------------------------------------------------------------
results = twitter.trends.place(_id=2295387)

print("Srinagar - Kashmir Trends")
i = 0
for location in results:
    for trend in location["trends"]:
        i = i+1
        print(i)
        print(" - %s" % trend["name"])
