#!/usr/bin/env python

# -----------------------------------------------------------------------
# twitter-trends
#  - lists the current global trending topics
# -----------------------------------------------------------------------

import config
import smtplib
import emailList
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

mailResult = ""
print("Srinagar - Kashmir Trends")
i = 0
# print(results)
for location in results:
    for trend in location["trends"]:
        i = i+1
        print(i)
        print(" - %s" % trend["name"])
        print(" URL:  %s" % trend["url"])
        mailResult += str(i) + ") " + \
            trend["name"] + "\n" + trend["url"] + "\n \n"

        if i == 10:
            break

# query = twitter.search.tweets(q="salmanually")
# How long did this query take?
# -----------------------------------------------------------------------
# print("Search complete (%.3f seconds)" %
#       (query["search_metadata"]["completed_in"]))

# -----------------------------------------------------------------------
# Loop through each of the results, and print its content.
# -----------------------------------------------------------------------
# for result in query["statuses"]:
#     print("(%s) @%s %s" % (result["created_at"],
#                            result["user"]["screen_name"], result["text"]))

# send Mail
TO = emailList.subscribers
# print(emailList.subscribers)
SUBJECT = 'Trends For Kashmir'
TEXT = 'Here are Top trends from Kashmir: \n'

TEXT += mailResult

TEXT += "\n This is trial based project Feedbacks & Suggestions are Most Welcome @ https://www.twitter.com/salmanually \n _____________ \n Want To add your friend or another account? just DM email to https://www.twitter.com/salmanually \n If you want to unsubscribe \n email to: contact@salmanually.com \n or \n tweet/DM: https://www.twitter.com/salmanually"

# Gmail Sign In
gmail_sender = 'kmrtrends@gmail.com'
gmail_passwd = config.password

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(gmail_sender, TO.split(","), BODY)
    print('email sent')
except:
    print('error sending mail')

server.quit()
