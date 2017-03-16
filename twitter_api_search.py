#!/usr/bin/env python



"""Documentation

The keyword to execute this code in the text converted is "Search twitter for'.
Here is the menu of what wil happen after it is recognized.
'Search twitter for..'
 1. 'tweets related to _____'- Searches for _____
 2. '_____' Searches for ______
 3. 'tweets sent from ________ '-Searches for tweets sent from ____ account
 4. 'at the rate _____'- @_____
 5. 'tweets containing hash tag _______'-#________
 6. 'videos of _____' Displays tweets containing media and _____

"""

import tweepy



#consumer key, consumer secret, access token, access secret.
ckey="v2jwaSVt27THEOzANj8xi8lvO"
csecret="1Cxd4B6lylQuY3TsOJCpSzrWImjfeZXDrD0hGHgo3vgZPFZVLt"
atoken="3973064473-HXjQzLJAevVFxcULXJQncG8LsLXs0BbGTqnhADC"
asecret="vZrpw5UKtqiH3TCEmN6jXhOj4HZbHaKoRrv2mnRMcYT9M"

auth =tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
api=tweepy.API(auth) 




def query_maker(q):
   
   q=q.replace('at the rate','@',1)
   q=q.replace('hashtag','#',1)
   q=q.replace('hash tag','#',1)
   q=q.replace('sent from','from:',1)
   q=q.replace('videos of','filter:media',1)
   q=q.replace('tweets','',1)
   q=q.replace('related to','',1)
   q=q.replace('containing','',1)
   q=q.replace('  ',' ')
   return q


def main(query):

    query=query_maker(query)
    search_api(query)


def search_api(q):
     tweets = api.search(q)
     for tweet in tweets:
         print tweet.text
         print '\n'

