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
          <Route path='/' element = {<Home/>} />
        </Routes>
    </Router>
  </Provider>
  );
}

export default App;
