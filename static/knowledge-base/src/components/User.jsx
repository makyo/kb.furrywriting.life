import React from 'react';
import { Link } from 'react-router-dom';
import Expertise from './Expertise.jsx'
import 'whatwg-fetch';

export default class User extends React.Component {
  constructor(props) {
    super(props);
    this.state = {expertise: []};
    fetch(`/api/user/${this.props.match.params.username}`).then((response) => {
      return response.json();
    }, console.log).then((data) => {
      this.setState({
        expertise: data.results
      });
    }, console.log);
  }

  render() {
    return (
      <div>
        <h2>{this.props.match.params.username}</h2>
          {this.state.expertise.map((expertise) => (
            <Expertise
              expertise={expertise}
              forTopic={false} />
          ))}
      </div>
    );
  }
}
