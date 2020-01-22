import {
  createStore,
  combineReducers,
  applyMiddleware
} from "redux";
import {
  createLogger
} from "redux-logger";
import thunk from "redux-thunk";

import mathReducer from "./reducers/mathReducer";
import contactReducer from "./reducers/contactsReducer";

export default createStore(
  combineReducers({
    mathReducer,
    contactReducer
  }), {},
  applyMiddleware(createLogger(), thunk)
);