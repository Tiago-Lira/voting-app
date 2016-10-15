
from .application import app, manager, socketio


@manager.command
def socket():
    socketio.run(app, port=8090)
