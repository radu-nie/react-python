export function setContacts(contacts) {
  return {
    type: "SET_CONTACTS_LIST",
    payload: contacts
  };  
}

export function editContact(contact) {
  return {
    type: "EDIT_CONTACT",
    payload: contact
  };
}

export function deleteContact(contact) {
  /** delete from db else do not continue with removing from state */
  return {
    type: "DELETE_CONTACT",
    payload: contact
  };
}

