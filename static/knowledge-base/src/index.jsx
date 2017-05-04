import React from 'react';
import { render } from 'react-dom';
import {
  BrowserRouter as Router,
  Link,
  Route
} from 'react-router-dom';

import Users from './components/Users.jsx';
import User from './components/User.jsx'
import Categories from './components/Categories.jsx';
import Category from './components/Category.jsx';
import Topic from './components/Topic.jsx';

const _Front = () => (
  <div>
    Welcome to the FWLife Knowledge Base! Blah blah blah. <Link to="/users">Users</Link> or <Link to="/categories">Categories</Link>
  </div>
);

const _Categories = () => (
  <div>
    <Categories />
  </div>
);

const _Category = ({categorySlug}) => (
  <div>
    <Topics
      category={categorySlug} />
  </div>
);

const _Topic = ({categorySlug, topicSlug}) => (
  <div>
    <Topic
      category={categorySlug}
      topic={topicSlug} />
  </div>
);

const _Users = () => (
  <div>
    <Users />
  </div>
);

const _User = ({username}) => (
  <div>
    <User
      username={username} />
  </div>
);

const KnowledgeBase = () => (
  <div>
    Welcome knowledge arg
  </div>
);

render((
    <Router>
      <div>
        <ul>
          <li><Link to="/categories">Categories</Link></li>
          <li><Link to="/users">Users</Link></li>
        </ul>
        <Route exact path="/" component={KnowledgeBase} />
        <Route path="/categories" component={_Categories} />
        <Route path="/category/:categorSlug" component={_Category} />
        <Route path="/category/:categorySlug/:topicSlug" component={_Topic} />
        <Route path="/users" component={Users} />
        <Route path="/user/:username" component={User} />
      </div>
    </Router>
  ), document.getElementById('app'));
