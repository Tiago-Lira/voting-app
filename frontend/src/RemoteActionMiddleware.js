
export default socket => store => next => action => {
    if (action.meta && action.meta.remote) {
        delete action.meta;
        socket.emit('action', action);
    }
    return next(action);
}
