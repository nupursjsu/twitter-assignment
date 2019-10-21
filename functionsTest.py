import unittest
import mock
from functions import get_tweet, post_tweet, delete_tweet, get_tweets
import requests

class functionsTest(unittest.TestCase):

    def setUp(self):
        self.testConf = {
            "consumerKey": "testConsumerKey",
            "consumerSecret": "testConsumerSecret",
            "twitterEndpoint": "http://testEndpointUrl",
            "accessToken": "testAccessToken",
            "accessSecret": "testAccessSecret"
        }

    '''
    Author: Chetan Kulkarni

    '''
    @mock.patch('functions.requests')
    def test_get_tweet(self, mock_requests):

        # Mocking the requests' GET method to send an appropriate response
        tweetId = "myId"
        mock_requests.get.return_value.text = '{"created_at":"Sun Oct 13 20:55:08 +0000 2019","id":1183486349204230145,"id_str":"1183486349204230145","text":"hello","truncated":false,"entities":{"hashtags":[],"symbols":[],"user_mentions":[],"urls":[]},"source":"","in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":1180686389827923969,"id_str":"1180686389827923969"},"geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"retweet_count":0,"favorite_count":0,"favorited":false,"retweeted":false,"lang":"en"}'
        tweet = get_tweet(tweetId, self.testConf)

        # Asserting that Twitter URL was correctly constructed
        expectedUrl = "{}/1.1/statuses/show.json?id={}".format(self.testConf['twitterEndpoint'], tweetId)
        self.assertApiCallsWithMockedInstance(mock_requests.get, "GET", expectedUrl)


    '''
    Author: Nupur Yadav
    '''
    @mock.patch('functions.requests')
    def test_post_tweet(self, mock_requests):

        # Mocking the requests' POST method to send an appropriate response
        tweetJson = {"status" : "hello"}
        mock_requests.post.return_value.text = '{"contributors":null,"coordinates":null,"created_at":"Sat Oct 19 17:43:56 +0000 2019","entities":{"hashtags":[],"symbols":[],"urls":[],"user_mentions":[]},"favorite_count":0,"favorited":false,"geo":null,"id":1185612559220478000,"id_str":"1185612559220477952","in_reply_to_screen_name":null,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"is_quote_status":false,"lang":"en","place":null,"retweet_count":0,"retweeted":false,"source":"","text":"hello","truncated":false,"user":{"contributors_enabled":false,"created_at":"Sun Oct 06 03:29:23 +0000 2019","default_profile":true,"default_profile_image":true,"description":"","entities":{"description":{"urls":[]}},"favourites_count":0,"follow_request_sent":false,"followers_count":0,"following":false,"friends_count":0,"geo_enabled":false,"has_extended_profile":true,"id":1180686389827924000,"id_str":"1180686389827923969","is_translation_enabled":false,"is_translator":false,"lang":null,"listed_count":0,"location":"","name":"Nupur","notifications":false,"profile_background_color":"F5F8FA","profile_background_image_url":null,"profile_background_image_url_https":null,"profile_background_tile":false,"profile_image_url":"http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png","profile_image_url_https":"https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png","profile_link_color":"1DA1F2","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"protected":false,"screen_name":"Nupur11159291","statuses_count":2,"time_zone":null,"translator_type":"none","url":null,"utc_offset":null,"verified":false}}'
        tweet = post_tweet(tweetJson, self.testConf)

        # Asserting that Twitter URL was correctly constructed
        expectedUrl = "{}/1.1/statuses/update.json?status=hello".format(self.testConf['twitterEndpoint'])
        self.assertApiCallsWithMockedInstance(mock_requests.post, "POST", expectedUrl)


    '''
    Author: Lokesh
    '''
    @mock.patch('functions.requests')
    def test_get_tweets(self, mock_requests):

        # Mocking the requests' GET method to send an appropriate response
        mock_requests.get.return_value.text = '{"created_at":"Sun Oct 13 20:55:08 +0000 2019","id":1183486349204230145,"id_str":"1183486349204230145","text":"hello","truncated":false,"entities":{"hashtags":[],"symbols":[],"user_mentions":[],"urls":[]},"source":"","in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":1180686389827923969,"id_str":"1180686389827923969"},"geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"retweet_count":0,"favorite_count":0,"favorited":false,"retweeted":false,"lang":"en"}'
        tweet = get_tweets(self.testConf)

        expectedUrl = "{}/1.1/statuses/user_timeline.json?trim_user=true".format(self.testConf['twitterEndpoint'])
        self.assertApiCallsWithMockedInstance(mock_requests.get, "GET", expectedUrl)


    '''
    Author: Rounak
    '''
    @mock.patch('functions.requests')
    def test_delete_tweet(self, mock_requests):

        # Mocking the requests' POST method to send an appropriate response
        tweetId = "myId"
        mock_requests.post.return_value.text = '{"created_at":"Sun Oct 13 20:55:08 +0000 2019","id":1183486349204230145,"id_str":"1183486349204230145","text":"hello","truncated":false,"entities":{"hashtags":[],"symbols":[],"user_mentions":[],"urls":[]},"source":"","in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":1180686389827923969,"id_str":"1180686389827923969"},"geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"retweet_count":0,"favorite_count":0,"favorited":false,"retweeted":false,"lang":"en"}'
        tweet = delete_tweet(tweetId, self.testConf)

        expectedUrl = "{}/1.1/statuses/destroy/{}.json".format(self.testConf['twitterEndpoint'], tweetId)
        self.assertApiCallsWithMockedInstance(mock_requests.post, "POST", expectedUrl)


    '''
    Author: Nupur Yadav

        We verify that the mocked API call was made with appropriate parameters:
        1. Assert that an API call was made
        2. Assert that the url matches expectation
        3. Assert that the request was initiated with appropriate OAuth1 object
    '''
    def assertApiCallsWithMockedInstance(self, mocked_request_method, requestType, expectedUrl):

        # Assert that the API call was made
        self.assertTrue(mocked_request_method.called, 
            "Failed to make a {} call to twitter API".format(requestType))

        # Extracting the parameters passed to the mocked function
        (args, kargs) = mocked_request_method.call_args
        actualUrl = args[0]
        oauthObj = kargs['auth']

        # Asserting that Twitter URL was correctly constructed
        self.assertEquals(actualUrl, expectedUrl, "Expected and Actual URLs should match")

        # Asserting the OAuth 1.0 created in the function 
        self.assertOAuthObj(oauthObj)


    '''
    Author: Nupur Yadav

        We verify the auth1 object which is used to populate the request headers with
        Oauth 1.0 Authorization parameters by:
        1. Creating a dummy request object
        2. Preating the request object so that appropriate authorization headers are set.
        3. Getting the Authorization header and asserting it with what we expect.
    '''
    def assertOAuthObj(self, oauth1):
        
        dummyRequest = requests.Request(method='GET', url='http://myDummyUrl', auth=oauth1)
        preparedRequest = dummyRequest.prepare()
        authorizationHeader = preparedRequest.headers['Authorization']

        # Asserting with oauth specific details
        self.assertTrue(authorizationHeader.startswith('OAuth'))
        self.assertTrue("oauth_consumer_key=\"{}\"".format(self.testConf['consumerKey']) in authorizationHeader)
        self.assertTrue("oauth_token=\"{}\"".format(self.testConf['accessToken']) in authorizationHeader)
        # We won't assert the oauth signature as we trust "requests_oauthlib" OAuth1.0 implementation.

if __name__ == '__main__':
    unittest.main()