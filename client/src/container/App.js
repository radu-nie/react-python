import React, { Component } from "react";
import { connect } from "react-redux";

import Contacts from "../components/Contacts";
import Home from "../components/Home";
import Header from "../components/Header";
import "./App.css";
import { Route, BrowserRouter as Router, Switch } from "react-router-dom";

class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <Switch>
            <Route exact path="/">
              <Header />
              <Home />
            </Route>
            <Route path="/about">
              <Header />
              <About />
            </Route>
            <Route path="/contacts">
              <Header />
              <Contacts />
            </Route>
          </Switch>
        </div>
      </Router>
    );
  }
}

function About() {
  return (
    <div>
      <h2>ABOUD</h2>
    </div>
  );
}

const mapStateToProps = state => {
  return {
    user: state.user,
    math: state.reducer
  };
};

const mapDispatchToProps = dispatch => {
  return {
    setName: name => {
      dispatch({
        type: "SET_NAME",
        payload: name
      });
    }
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(App);
