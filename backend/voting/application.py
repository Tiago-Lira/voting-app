
from flask import Flask
from flask_socketio import SocketIO
from flask_script import Manager

from .redux import make_store
from .actions import *  # noqa


app = Flask('voting')
manager = Manager(app)
socketio = SocketIO(app=app)
store = make_store()

# Initial data
store.dispatch({
    'type': 'SET_ENTRIES',
    'entries': [
        "Shallow Grave",
        "Trainspotting",
        "A Life Less Ordinary",
        "The Beach",
        "28 Days Later",
        "Millions",
        "Sunshine",
        "Slumdog Millionaire",
        "127 Hours",
        "Trance",
        "Steve Jobs"
    ]
})


@socketio.on('connect')
def on_connect():
    broadcast_state()


@socketio.on('action')
def handle_action(action):
    store.dispatch(action)
    broadcast_state()


def broadcast_state():
    socketio.emit('state', store.get_state(), broadcast=True)

broadcast_state()
