import React, { Component } from "react";

class Home extends Component {
  constructor(props) {
    super();
    this.state = {};
  }

  render() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-12">
            <button type="button" className="btn btn-primary bmd-btn-fab">
              <i className="material-icons">add</i>
            </button>
          </div>
        </div>
        <div className="row">
          <div className="col-12">EIII</div>
        </div>
      </div>
    );
  }
}

export default Home;
