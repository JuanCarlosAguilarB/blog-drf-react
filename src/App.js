import React from 'react';
import logo from './logo.svg';
import { Counter } from './features/counter/Counter';
import './App.css';
import Home from 'containers/pages/Home';
import Error404 from 'containers/errors/Error404';

import { Provider } from 'react-redux';
import {BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { store } from 'app/store';
 

function App() {
  return (
    <Provider store={store}>
      <Router>
        <Routes> 
          <Route path='*' element = {<Error404/>} />
          <Route path='?' element = {<Home/>} />
        </Routes>
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <Counter />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <span>
          <span>Learn </span>
          <a
            className="App-link"
            href="https://reactjs.org/"
            target="_blank"
            rel="noopener noreferrer"
          >
            React
          </a>
          <span>, </span>
          <a
            className="App-link"
            href="https://redux.js.org/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Redux
          </a>
          <span>, </span>
          <a
            className="App-link"
            href="https://redux-toolkit.js.org/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Redux Toolkit
          </a>
          ,<span> and </span>
          <a
            className="App-link"
            href="https://react-redux.js.org/"
            target="_blank"
            rel="noopener noreferrer"
          >
            React Redux
          </a>
        </span>
      </header>
    </div>
    </Router>
  </Provider>
  );
}

export default App;
