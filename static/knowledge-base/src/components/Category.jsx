import React from 'react';
import { Link } from 'react-router-dom';

export default class Category extends React.Component {
  constructor(props) {
    super(props);
    this.state = {topics: [], title: "(no topics)"};
    fetch(`/api/category/${this.props.match.params.categorySlug}/topics`).then((response) => {
      return response.json();
    }).then((data) => {
      let newState = {
        topics: data.results,
      };
      if (data.results.length > 0) {
        newState.title = data.results[0].category;
      }
      this.setState(newState);
    });
  }

  render() {
    return (
      <div>
        <h2>{this.state.title}</h2>
        <ul>
          {this.state.topics.map((topic) => (
            <li key={topic.slug}>
              <Link
                to={`${this.props.match.url}/topic/${topic.slug}`}>
                {topic.topic}
              </Link>
            </li>
          ))}
        </ul>
      </div>
    );
  }
}
