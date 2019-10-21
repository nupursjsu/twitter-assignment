import {Component} from "react";
import React from "react";

// Author: Nupur Yadav
// This is a form created to post new Tweets
// for a user
class TweetForm extends Component {
  state = {
    text: ""
  }

  onChange(e) {
    this.setState({text: e.target.value});
  }

  // This method will call the send() method (initiatized with postTweet() in App.js) 
  // which will post the tweet using the POST
  // tweets API exposed by our Twitter service
  onSubmit(e) {
    e.preventDefault();
    this.props.onSend(this.state.text);
    // Update the text box to get ready for the next tweet
    this.setState({text: ""});
  }

  render() {
    return (
      <div className="TweetForm">
        <form onSubmit={e => this.onSubmit(e)}>
          <input
            type="text"
            placeholder="Write your tweet and press ENTER"
            onChange={e => this.onChange(e)}
            value={this.state.text}
            autoFocus={true}
          />
          <button>Send</button>
        </form>
      </div>
    );
  }
}

export default TweetForm;