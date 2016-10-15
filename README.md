# voting-app

Voting application using Flask and React with Redux. This code was created following the tutorial of [Tero Parviainen](http://teropa.info/blog/2015/09/10/full-stack-redux-tutorial.html).  


The only difference from the tutorial is that I'm using the backend with `Flask` and `Flask-SocketIO`. It was interesting to learn Redux and try to apply in a python application.


## Running this project

### Clone this project
```bash
$ git clone git@github.com:Tiago-Lira/voting-app.git
```

### Getting started with the backend application with Flask
```bash
$ cd backend/
$ pip install -r requirements.txt
$ python manage.py socket
"
WebSocket transport not available. Install eventlet or gevent and gevent-websocket  
for improved performance.
 * Running on http://127.0.0.1:8090/ (Press CTRL+C to quit)
"
```

### Getting started with the frontend application with React
```bash
$ cd frontend/
$ npm install
$ npm install -g webpack webpack-dev-server
$ npm start
"
> webpack-dev-server --port 5000
http://localhost:5000/webpack-dev-server/
"
```
