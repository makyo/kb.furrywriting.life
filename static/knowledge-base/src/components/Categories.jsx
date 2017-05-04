import React from 'react';
import { Link } from 'react-router-dom';

export default class Categories extends React.Component {
  constructor(props) {
    super(props);
    this.state = {categories: []};
    fetch(`/api/categories`).then((response) => {
      return response.json();
    }).then((data) => {
      this.setState({
        categories: data.results
      });
    });
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
