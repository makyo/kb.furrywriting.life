import React from 'react';
import { render } from 'react-dom';
import {
  BrowserRouter as Router,
  Link,
  Route,
  Switch
} from 'react-router-dom';

import Promise from 'promise-polyfill';
if (!window.Promise) {
  window.Promise = Promise;
}

import Users from './components/Users.jsx';
import User from './components/User.jsx'
import Categories from './components/Categories.jsx';
import Category from './components/Category.jsx';
import Topic from './components/Topic.jsx';

const KnowledgeBase = () => (
  <div>
    Welcome knowledge arg
  </div>
);

fetch('/api').then(() => {
  render((
      <Router>
        <div>
          <ul className="router-links">
            <li><Link to="/categories">Categories</Link></li>
            <li><Link to="/users">Users</Link></li>
          </ul>
          <Switch>
            <Route exact path="/" component={KnowledgeBase} />
            <Route path="/categories" component={Categories} />
            <Route path="/category/:categorySlug/topic/:topicSlug" component={Topic} />
            <Route path="/category/:categorySlug" component={Category} />
            <Route path="/users" component={Users} />
            <Route path="/user/:username" component={User} />
          </Switch>
        </div>
      </Router>
    ), document.getElementById('app'));
})
