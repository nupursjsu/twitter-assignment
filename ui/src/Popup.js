import {Component} from "react";
import React from "react";

// Author: Ronak Mehta
// This is a simple class to show popup when a user wants to see
// extra details about a specific tweet.
class Popup extends Component {
  render() {
    return (
      <div className='popup'>
        <div className='popupGroup'>
          <button onClick={this.props.closePopup}>X</button>
          <pre>{JSON.stringify(this.props.text, undefined, 2)}</pre>
        </div>
      </div>
    );
  }
}

export default Popup;