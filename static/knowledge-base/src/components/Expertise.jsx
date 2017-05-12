import React from 'react';
import { Link } from 'react-router-dom';

export default class Expertise extends React.Component {
  header() {
    if (this.props.forTopic) {
      return (
        <h3>
          <Link to={`/user/${this.props.expertise.user}`}>
            {this.props.expertise.user}
          </Link>
        </h3>
      );
    } else {
      return (
        <h3>Expertise in <Link to={`/category/${this.props.expertise.expertise_topics[0].category_slug}`}>{this.props.expertise.expertise_topics[0].category}</Link></h3>
      );
    }
  }

  contentWarning() {
    if (this.props.expertise.content_warning) {
      return (
        <strong>This post comes with a content warning. Read at your own risk</strong>
      );
    }
  }

  topics() {
    return this.props.expertise.expertise_topics.map((topic) => {
      return (
        <li key={topic.topic_slug + topic.category_slug}>
          <Link to={`/category/${topic.category_slug}/topic/${topic.topic_slug}`}>{topic.category} :: {topic.topic}</Link>
        </li>
      )
    });
  }

  render() {
    return (
      <div className="expertise">
        {this.header()}
        {this.contentWarning()}
        <p>{this.props.expertise.expertise}</p>
        <h4>Topics:</h4>
        <ul className="router-links">{this.topics()}</ul>
      </div>
    );
  }
}
