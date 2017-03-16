import tweepy
import json

#prints list of trending topics in India 
def main():
    #consumer key, consumer secret, access token, access secret.
    ckey="v2jwaSVt27THEOzANj8xi8lvO"
    csecret="1Cxd4B6lylQuY3TsOJCpSzrWImjfeZXDrD0hGHgo3vgZPFZVLt"
    atoken="3973064473-HXjQzLJAevVFxcULXJQncG8LsLXs0BbGTqnhADC"
    asecret="vZrpw5UKtqiH3TCEmN6jXhOj4HZbHaKoRrv2mnRMcYT9M"

    auth=tweepy.OAuthHandler(ckey,csecret)
    auth.set_access_token(atoken,asecret)

    api=tweepy.API(auth)

    bla=api.trends_place(2295411)
    json.dumps(bla)
    for blas in bla:
	   for pa in blas[u'trends']:
		 print pa[u'name']