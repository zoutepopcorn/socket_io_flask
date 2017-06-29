#!/usr/bin/python
# J. Hoeksma 2017 - v 0.1
from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

## WEBSERVER STATIC ##
# make al /static/ folder available
@app.route('/')
def root():
  return app.send_static_file('index.html')
@app.route('/<path:path>')
def static_proxy(path):
  return app.send_static_file(path)

## SOCKET.IO CONNECTION ##
# make al /static/ folder available
@socketio.on('connect')
def connected():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>> connect")
    emit('msg', {'data': 'Conooooooooooooonected'})

# Data in from browser, JSON format
@socketio.on('api')
def api(data):
    print('received api request ' + data)

# Message, info or debug information
@socketio.on('msg')
def message(message):
    print('received message: ' + message)

if __name__ == '__main__':
    app.debug = True
    socketio.run(app, port=5000)
