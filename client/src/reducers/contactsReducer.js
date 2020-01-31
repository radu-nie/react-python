const contactsReducer = (state = {
    contacts: []
}, action) => {
    switch (action.type) {
        case "SET_CONTACTS_LIST":
            state = {
                ...state,
                contacts: action.payload
            };
            break;
        case "EDIT_CONTACT":
            //var initialContact = state.contacts.find(x => (x.id = action.payload));
            state = {
                ...state
            };
            break;
        case "DELETE_CONTACT":
            state = {
                ...state,
                contacts: state.contacts.filter(contact => contact.node.id !== action.payload.id)
            }
            break;
        default:
            break;
    }
    return state;
};
export default contactsReducer;