import React from 'react';
import { Link } from 'react-router-dom';

export default class Expertise extends React.Component {
  render() {
    return (
      <div>
        <h3><Link to={`/user/${this.props.expertise.user}`}>{this.props.expertise.user}</Link></h3>
        <p>{this.props.expertise.expertise}</p>
      </div>
    );
  }
}
