import React from 'react';
import { Link } from 'react-router-dom';
import 'whatwg-fetch';

export default class Users extends React.Component {
  constructor(props) {
    super(props);
    this.state = {users: []};
    fetch('/api/users').then((response) => {
      return response.json();
    }, console.log).then((data) => {
      this.setState({
        users: data.results
      });
    }, console.log);
  }

  render() {
    return (
      <div>
        <h2>Users</h2>
        <ul>
          {this.state.users.map((user) =>
            <li key={user.username}>
              <Link to={`/user/${user.username}`}>{user.username}</Link>
            </li>)}
        </ul>
      </div>
    );
  }
}
