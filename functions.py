from requests_oauthlib import OAuth1
import requests
import json

'''
Author: Chetan Kulkarni
'''
def get_tweet(tweetId, conf):
  oauth = createOAuth1Object(conf)
  twitterResourceUrl = "{}/1.1/statuses/show.json?id={}".format(conf['twitterEndpoint'], tweetId)
  response = requests.get(twitterResourceUrl, auth=oauth)
  return json.loads(response.text)

'''
Author: Nupur Yadav
'''
def post_tweet(tweet, conf):
  oauth = createOAuth1Object(conf)

  # Creating URL params based on the input json
  params = ""
  for key in tweet:
  	params += key + "=" + tweet[key]

  twitterResourceUrl = "{}/1.1/statuses/update.json?{}".format(conf['twitterEndpoint'], params)
  response = requests.post(twitterResourceUrl, auth=oauth)
  return json.loads(response.text)

'''
Author: Lokesh Vadlamudi
'''
def get_tweets(conf):
  oauth = createOAuth1Object(conf)
  twitterResourceUrl = "{}/1.1/statuses/user_timeline.json?trim_user=true".format(conf['twitterEndpoint'])
  response = requests.get(twitterResourceUrl, auth=oauth)
  return json.loads(response.text)

'''
Author: Ronak Mehta
'''
def delete_tweet(tweetId, conf):
  oauth = createOAuth1Object(conf)
  twitterResourceUrl = "{}/1.1/statuses/destroy/{}.json".format(conf['twitterEndpoint'], tweetId)
  response = requests.post(twitterResourceUrl, auth=oauth)
  return json.loads(response.text)

'''
Author: Nupur Yadav

  This method is used to create the OAuth1.0 object which will be passed as a 'auth'
  argument to the requests.{get, post} methods.

'''
def createOAuth1Object(conf):
  return OAuth1(conf['consumerKey'],
                   client_secret=conf['consumerSecret'],
                   resource_owner_key=conf['accessToken'],
                   resource_owner_secret=conf['accessSecret'])