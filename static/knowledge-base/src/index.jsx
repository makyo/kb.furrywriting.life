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
    <p>The FWLife Knowledge Base stores information about the users and what their expertise is. It is intended as a resource for writers to let them know who to ask about what.</p>
    <p>For now, the data is pulled in by hand via the FWG forums or through personal interaction when asked. If you want to add any data, tell Makyo. In the future, this may become user-editable, and you'll be able to claim your user.</p>
  </div>
);

fetch('/api').then(() => {
  render((
      <Router>
        <div>
          <ul className="router-links">
            <li><Link to="/categories">View Categories</Link></li>
            <li><Link to="/users">View Users</Link></li>
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
