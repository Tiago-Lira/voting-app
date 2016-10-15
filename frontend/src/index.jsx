
import React from 'react';
import ReactDOM from 'react-dom';
import {Router, Route, hashHistory} from 'react-router';
import {createStore, applyMiddleware} from 'redux';
import {Provider} from 'react-redux';
import io from 'socket.io-client';
import Reducer from './Reducer';
import {setState} from './ActionCreators';
import remoteActionMiddleware from './RemoteActionMiddleware';
import App from './components/App';
import {VotingContainer} from './components/Voting';
import {ResultsContainer} from './components/Results';


const socket = io(`${location.protocol}//${location.hostname}:8090`);
socket.on('state', state => {
    console.log(state);
    store.dispatch(setState(state));
});

const createStoreWithMiddleware = applyMiddleware(
  remoteActionMiddleware(socket)
)(createStore);

const store = createStoreWithMiddleware(Reducer);

ReactDOM.render(
    <Provider store={store}>
        <Router history={hashHistory}>
            <Route component={App}>
                <Route path='/' component={VotingContainer} />
                <Route path='/results' component={ResultsContainer} />
            </Route>
        </Router>
    </Provider>,
    document.getElementById('app')
);
