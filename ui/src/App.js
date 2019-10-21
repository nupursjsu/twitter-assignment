import React, { Component } from 'react';
import './App.css';
import TweetWindow from "./TweetWindow";
import TweetForm from "./TweetForm";
import Popup from "./Popup";

// This is the main Component which:
// 1. Shows all the Tweets for the current user (GET /v1/tweets)
// 2. Provide an ability to delete a specific tweet (DELETE /v1/tweets/id)
// 3. Get details about a specific tweet (GET /v1/tweets/id)
// 4. Post new Tweets on the Twitter feed (POST /v1/tweets)
class App extends Component {
  state = {
    tweets: [],
    details: {},
    showPopup: false,
  }

  constructor() {
    super();
    this.twitterServiceEndPoint = "http://localhost"
  }
  // Author: Lokesh Vadlamudi
  // This function gets all User Tweets and update the state
  getTweets = () => {
    fetch(this.twitterServiceEndPoint.concat('/v1/tweets'))
      .then(res => res.json())
      .then((data) => {
        console.log(data)
        this.setState({ tweets: data.reverse() })
      })
      .catch(console.log)
  }

  // Author: Ronak Mehta
  // This function deletes the current Tweet and update the state
  deleteTweet = (id) => {
    fetch(this.twitterServiceEndPoint.concat('/v1/tweets/', id), {
      method: 'DELETE'  
    })
      .then(res => res.json())
      .then((data) => {
        console.log(data)
        this.getTweets();
      })
      .catch(console.log)
  }

  // Author: Chetan Kulkarni
  // This function gets the current Tweet and update the state
  getTweet = (id) => {
    fetch(this.twitterServiceEndPoint.concat('/v1/tweets/', id))
      .then(res => res.json())
      .then((data) => {
        console.log(data)
        const info = {
          tweet: data.text,
          id: data.id_str,
          created_at: data.created_at,
          retweet_count: data.retweet_count,
          language: data.lang
        }
        this.setState({ 
          details: info,
          showPopup: true
         })
      })
      .catch(console.log)
  }

  // Author: Nupur Yadav
  // This function post a new Tweets and also update the state
  // to ensure that it is rendered on the UI
  postTweet = (tweet) => {
    fetch(this.twitterServiceEndPoint.concat('/v1/tweets'), {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        status: tweet
      })
    })
      .then(res => res.json())
      .then(data => {
        const joined = this.state.tweets.concat(data);
        this.setState({tweets: joined})
      })
      .catch(console.log)
  }

  // Author: Nupur Yadav
  // As soon as the App component gets mounted,
  // we should show the current Tweets
  componentDidMount() {
    this.getTweets();
  }

  // Author: Nupur Yadav
  // This method is used to close the popup by updating
  // the state (showPopup)
  closePopup() {
    this.setState({
      showPopup: !this.state.showPopup
    });
  }

  // Author: Nupur Yadav
  // This will render the main screen which simulates 
  // the feed as a timeline than anything else... 
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h1>#fourreal Twitter Homework</h1>
        </div>
          {this.state.showPopup ? 
            <Popup
              text={this.state.details}
              closePopup={this.closePopup.bind(this)}
            />
            : null
          }
        <TweetWindow
          tweets={this.state.tweets} 
          onDeleteClick={this.deleteTweet}
          onDetailsClick={this.getTweet}
        />
        <TweetForm
          onSend={this.postTweet}
        />
      </div>
    );
  }
}

export default App;