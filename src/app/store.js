import { configureStore, applyMiddleware } from '@reduxjs/toolkit';
import thunk from 'redux-thunk';
import rootReducer from 'redux/reducers'
import { composeWithDevTools } from 'redux-devtools-extension';

const initialState = {};

const middleware = [thunk];

export const store = configureStore(
  rootReducer,
  initialState,
  // applyMiddleware(...middleware)
  composeWithDevTools(applyMiddleware(...middleware))
);
