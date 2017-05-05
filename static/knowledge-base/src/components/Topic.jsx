import React from 'react';
import { Link } from 'react-router-dom';
import Expertise from './Expertise.jsx';
import 'whatwg-fetch';

export default class Topic extends React.Component {
  constructor(props) {
    super(props);
    this.state = {expertise: [], category: '(no topics)', topic: '(no expertise)'};
    fetch(`/api/category/${this.props.match.params.categorySlug}/topic/${this.props.match.params.topicSlug}`).then((response) => {
      return response.json();
    }, console.log).then((data) => {
      let newState = {
        expertise: data.results,
      };
      if (data.results.length > 0) {
        newState.category = data.results[0].category;
        newState.topic = data.results[0].topic;
      }
      this.setState(newState);
    }, console.log);
  }

  render() {
    return (
      <div>
        <h2>
          <Link to={`/category/${this.props.match.params.categorySlug}`}>{this.state.category}</Link> :: {this.state.topic}</h2>
        {this.state.expertise.map((expertise) => (
          <Expertise
            key={expertise.expertise_id.toString()}
            expertise={expertise} />
        ))}
      </div>
    );
  }
}
