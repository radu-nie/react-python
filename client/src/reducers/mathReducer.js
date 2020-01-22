const mathReducer = (state = {
    lastValues: {},
    result: null
}, action) => {
    switch (action.type) {
        case "ADD":
            state = {
                ...state,
                lastValues: [...state.lastValues, action.payload],
                result: state.result + action.payload
            };

            break;
        case "SUBTRACT":
            state = {
                ...state,
                lastValues: [...state.lastValues, action.payload],
                result: state.result - action.payload
            };

            break;
        default:
            break;
    }
    return state;
};
export default mathReducer;