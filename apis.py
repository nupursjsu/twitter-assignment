from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from functions import get_tweet, post_tweet, delete_tweet, get_tweets
from settings import conf
import json

app = Flask(__name__)

# Supporting Cross Origin requests for all APIs
cors = CORS(app)

# Swagger spec integration with the UI
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Twitter APIs"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

'''
Author: Chetan Kulkarni
API to get a specific tweet
'''
@app.route('/v1/tweets/<tweetId>', methods=['GET'])
def getTweet(tweetId):
	return jsonify(get_tweet(tweetId, conf))

'''
Author: Nupur Yadav
API to post a new tweet
'''
@app.route('/v1/tweets', methods=['POST'])
def postTweet():
	print(request);
	tweet = request.get_json()
	print(tweet);
	return jsonify(post_tweet(tweet, conf))

'''
Author: Lokesh Vadlamudi
API to get all tweets for a user
'''
@app.route('/v1/tweets', methods=['GET'])
def getTweets():
	return jsonify(get_tweets(conf))

'''
Author: Ronak Mehta
API to Delete a specific tweet
'''
@app.route('/v1/tweets/<tweetId>', methods=['DELETE'])
def deleteTweet(tweetId):
	return jsonify(delete_tweet(tweetId, conf))
	
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)