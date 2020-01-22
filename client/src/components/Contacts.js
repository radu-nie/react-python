import React, { Component } from "react";
import { connect } from "react-redux";

import Modal from "./Modal";
import {
  deleteContact,
  editContact,
  setContacts
} from "../actions/contactActions";

class Contacts extends Component {
  constructor(props) {
    super();
    this.state = {
      contact: {}
    };
  }

  onHandleChange(event) {}

  onEditContact(newContact) {
    this.setState({
      contact: newContact
    });
  }

  componentDidMount() {
    fetch("http://127.0.0.1:5000/api/user/")
      .then(res => res.json())
      .then(data => {
        this.props.setContactList(data);
        this.setState({ contacts: data });
      })
      .catch(console.log);
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
          <div className="col-12">
            <center>
              <h1>Contact List</h1>
            </center>
            {this.props.contacts.contacts.map((contact, i) => (
              <div className="card" key={i}>
                <div className="card-body">
                  <div className="row">
                    <div className="col-8">
                      <h5 className="card-title">
                        {contact.first_name} {contact.last_name}
                      </h5>
                      <h6 className="card-subtitle mb-2 text-muted">
                        {contact.email}
                      </h6>
                      <p className="card-text">Phone: {contact.phone_no}</p>
                    </div>
                    <div className="col-4">
                      <div className="height-100">
                        <button
                          className="btn btn-raised btn-info height-100"
                          data-toggle="modal"
                          data-target="#exampleModal"
                          onClick={() => this.onEditContact(contact)}
                        >
                          <i className="material-icons pmd-sm">edit</i>
                        </button>
                        &nbsp;
                        <button
                          style={{ height: "100%" }}
                          className="btn btn-raised btn-warning height-100"
                          title="remove"
                          onClick={() => this.props.deleteContact(contact)}
                        >
                          <i className="material-icons pmd-sm">delete</i>
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            ))}

            <Modal>
              <input type="text" value={this.state.contact.email} />

              <p>
                {this.state.contact.first_name} {this.state.contact.last_name}
              </p>
              <p>{this.state.contact.email}</p>
              <p>{this.state.contact.phone_no}</p>
            </Modal>
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    user: state.user,
    math: state.reducer,
    contacts: state.contactReducer
  };
};

const mapDispatchToProps = dispatch => {
  return {
    setContactList: contactList => {
      dispatch(setContacts(contactList));
    },
    editContact: contact => {
      dispatch(editContact(contact));
    },
    deleteContact: contact => {
      dispatch(deleteContact(contact));
    }
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Contacts);
