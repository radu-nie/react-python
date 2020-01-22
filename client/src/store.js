import { createStore, combineReducers, applyMiddleware } from "redux";
import { createLogger } from "redux-logger";

import mathReducer from "./reducers/mathReducer";
import contactReducer from "./reducers/contactsReducer";

export default createStore(
  combineReducers({ mathReducer, contactReducer }),
  {},
  applyMiddleware(createLogger())
);
