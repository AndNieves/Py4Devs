from bottle import route, run, template, request, response
import json

@route('/hello')
def hello():
    return "Hello World!"

@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

run(host='localhost', port=8888, debug=True)