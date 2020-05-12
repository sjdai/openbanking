import flask
from flask import jsonify, request


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/test/oauth', methods=['GET'])
def oauth():
    return jsonify("http://127.0.0.1:5000/oauth/authorization")

@app.route('/oauth/authorization', methods=['GET'])
def authorization():
    return jsonify("http://127.0.0.1:5000/login")


@app.route('/login', methods=['GET'])
def login():
    if 'username' in request.args and 'password' in request.args:
        username = request.args['username']
        password = request.args['password']
        return jsonify("success")
    return jsonify("fail")


app.run()