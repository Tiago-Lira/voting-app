
export function setState(state) {
    console.log(state);
    return {
      type: 'SET_STATE',
        state
    };
}

export function vote(entry) {
    console.log('vote');
    return {
        meta: {remote: true},
        type: 'VOTE',
        entry
    };
}


export function next() {
    console.log('next');
    return {
        meta: {remote: true},
        type: 'NEXT'
    };
}
