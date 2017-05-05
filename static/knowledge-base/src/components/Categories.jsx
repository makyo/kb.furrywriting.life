import React from 'react';
import { Link } from 'react-router-dom';
import 'whatwg-fetch';

export default class Categories extends React.Component {
  constructor(props) {
    super(props);
    this.state = {categories: []};
    console.log('constructed', new Date())
    fetch(`/api/categories`).then((response) => {
      console.log('fetch', new Date())
      return response.json();
    }, console.log).then((data) => {
      this.setState({
        categories: data.results
      });
      console.log('json', new Date())
    }, console.log);
  }

  render() {
    return (
      <div>
        <h2>Categories</h2>
        <ul>
          {this.state.categories.map((category) => (
            <li key={category.slug}>
              <Link
                to={`/category/${category.slug}`}>
                {category.category}
              </Link>
            </li>
          ))}
        </ul>
      </div>
    );
  }
}
