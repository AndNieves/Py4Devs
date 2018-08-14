from bottle import route, run, template, request, response
import json

@route('/login', method='POST')
def login():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

    name = request.forms.get("username")
    password = request.forms.get("password")
    return json.dumps({ 'response': 'successs'})

run(host='localhost', port=8888, debug=True)