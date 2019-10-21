import {Component} from "react";
import React from "react";


// This Component will display the tweets in a window like
// chat messages, instead of Twitter feed as it looked 
// confusing when looking at only the current user's tweets.
class TweetWindow extends Component {

  // Author: Ronak Mehta
  // This method will delete the tweet by using the DELETE query
  delete(e, id) {
    e.preventDefault();
    console.log("Clicked on delete id: " + id);
    this.props.onDeleteClick(id);
  }

  // Author: Chetan Kulkarni
  // This method will display additional details about a specific tweet like
  // created_at, retweet_count, etc. by making a GET query for that 
  // tweet
  getDetails(e, id) {
    e.preventDefault();
    console.log("Clicked on details for id: " + id);
    this.props.onDetailsClick(id);
  }

  // Author: Lokesh Vadlamudi
  // This method will display a TweetGroup which comprises of the Tweet,
  // a Delete and Details button.
  displayTweet(tweet) {
  	console.log(tweet);
  	const text = tweet.text;
    return (
      <li key = {tweet.id_str} className="TweetGroup">
        <div className="Tweet">
          <div className="text">{text}</div>
          <button className="deleteButton" onClick={e => this.delete(e, tweet.id_str)}>Delete</button>
          <button className="detailsButton" onClick={e => this.getDetails(e, tweet.id_str)}>Details</button>
        </div>
      </li>
    );
  }

  // Rendering the Tweets
  render() {
    const {tweets} = this.props;
    return (
      <ul className="Tweets">
        {tweets.map(t => this.displayTweet(t))}
      </ul>
    );
  }

}

export default TweetWindow;