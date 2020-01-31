import React, { Component } from "react";
import { connect } from "react-redux";
import Modal from "./Modal";
import {
  deleteContact,
  editContact,
  setContacts
} from "../actions/contactActions";

import ApolloClient from "apollo-boost";
import gql from "graphql-tag";
import { useMutation } from '@apollo/react-hooks';

const client = new ApolloClient({
  uri: "http://127.0.0.1:5000/graphql"
});



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

  onDeleteContact(contact) {
    const [deleteContactMutation, { data }] = useMutation(DELETE_USER_BY_ID);
      deleteContactMutation({ variables: { id: contact.id } }).then(data =>{
        console.log(data);
      })

      //this.props.deleteContact(contact.node)}
  }

  componentDidMount() {
    client.query({
      query: GET_USER_LIST
    })
    .then(data => {
      this.props.setContactList(data.data.userList.edges);
      this.setState({ contacts: data.data.userList.edges });
    })
    .catch(console.log);
    // fetch("http://127.0.0.1:5000/api/user/")
    //   .then(res => res.json())
    //   .then(data => {
    //     this.props.setContactList(data);
    //     this.setState({ contacts: data });
    //   })
    //   .catch(console.log);
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
                  {contact.node.firstName} {contact.node.lastName}
                </h5>
                <h6 className="card-subtitle mb-2 text-muted">
                  {contact.node.email}
                </h6>
                <p className="card-text">Phone: {contact.node.phoneNo}</p>
              </div>
              <div className="col-4">
                <div className="height-100">
                  <button
                    className="btn btn-raised btn-info height-100"
                    data-toggle="modal"
                    data-target="#exampleModal"
                    onClick={() => this.onEditContact(contact.node)}
                  >
                    <i className="material-icons pmd-sm">edit</i>
                  </button>
                  &nbsp;
                  <button
                    style={{ height: "100%" }}
                    className="btn btn-raised btn-warning height-100"
                    title="remove"
                    onClick={() => this.onDeleteContact(contact.node)}
                  >
                    <i className="material-icons pmd-sm">delete</i>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      ))
      } 

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
      

      //dispatch(deleteContact(contact));
    }
  };
};

const GET_USER_LIST = gql`
{
  userList{
    edges{
      node{
        id
        firstName
        lastName
        email
        phoneNo
        dateAdded
        dateEdited
      }
    }
  }
}
`;

const DELETE_USER_BY_ID = gql`
  mutation DeleteUser($id: ID){
    deleteUser(input:{id: $id}){
      user{
        firstName
        lastName
        email
        phoneNo
      }
    }
  }
`;

export default connect(mapStateToProps, mapDispatchToProps)(Contacts);
