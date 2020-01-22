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
  return {
    type: "DELETE_CONTACT",
    payload: contact
  };
}
