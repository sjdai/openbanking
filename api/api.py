import flask
from flask import jsonify, request, Response

app = flask.Flask(__name__)
app.config["DEBUG"] = True

bank_codes = open('./util/bank_code.txt')
bank_codes = bank_codes.read()
bank_codes = bank_codes.split('\n')

client_list = []

key_list = []

@app.route('/test/oauth', methods=['GET'])
def oauth():
    x_stan = request.headers['X-STAN']
    x_destination_id = request.headers['X-DestinationId']
    x_client_id = request.headers['X-ClientId']
    x_txn_init_date_time = request.headers['X-TxnInitDateTime']
    x_key_id = request.headers['X-KeyID']
    if len(x_stan) != 7 or len(x_destination_id) != 7 or len(x_client_id) != 16 or len(x_txn_init_date_time) != 14:
        content = {"error":"invalid_request"}
        return Response(content, status=400, mimetype='application/json')
    elif x_client_id not in bank_codes:
        content = {"error":"invalid_destination"}
        return Response(content, status=400, mimetype='application/json')
    elif x_client_id not in client_list:
        content = {"error":"invalid_client"}
        return Response(content, status=400, mimetype='application/json')
    elif x_key_id not in key_list:
        content = {"error": "unauthorixed_client"}
        return Response(content, status=400, mimetype='application/json')
    else:
        content = {"bank":x_destination_id,"redirect_link":"http://127.0.0.1:5000/oauth/authentication"}
        return Response(content, status=200, mimetype='application/json')
    #return jsonify("http://127.0.0.1:5000/oauth/authorization")

@app.route('/oauth/authorization', methods=['POST'])
def authorization():
    user_agent = request.headers['User-Agent']
    content_type = request_headers['Content-Type']

    response_type = request.args.get('response_type')
    client_id = request.args.get('client_id')
    redirect_url = request.args.get('redirect_url')
    scope = request.args.get('scope')
    state = request.args.get('state')

    content = {
        "code": "authorization code",
        "state": "state for client"
    }
    resp = Response(content, status=200, mimetype="application/json")

    return resp

@app.route('/oauth/token', methods=['POST'])
def token():
    content_type = request.headers['Content-Type']

    grant_type = request.args.get('grant_type')
    code = request.args.get('code')
    redirect_url = request.args.get('redirect_url')
    client_id = request.args.get('client_id')
    client_secret = request.args.get('client_secret')
    scope = request.args.get('scope')
    refresh_token = request.args.get('refresh_token')
    
    content = {
        "access_token": "access token here",
        "token_type": "Bearer",
        "expires_in": 300,
        "refresh_token": "value of refresh token",
        "scope": "scope here"
    }
    
    resp = Response(content, status=200, mimetype="application/json")
    resp.headers['Cache-Control'] = 'no-store'
    resp.headers['Pragma'] = 'no-cache'
    
    return resp

@app.route('/oauth/revocation', methods=['POST'])
def revocation():
    content_type = request.headers['Content-Type']

    token = request.args.get('token')
    token_type_hint = request.args.get('token_type_hint')
    client_id = request.args.get('client_id')
    client_secret = request.args.get('client_secret')

    content = {
        "code": "revoke success code"
        "message": "description about revoke success code"
    }

    resp = Response(content, status=200, mimetype="application/json")

    return resp

@app.route('/oauth/introspection', methods=['POST'])
def introspection():
    content_type = request.headers['Content-Type']

    token = request.args.get('token')
    token_type_hint = request.args.get('token_type_hint')
    client_id = request.args.get('client_id')
    client_secret = request.args.get('client_secret')

    content = {
        "active": True,
        "scope": "range",
        "client_id": "client id here",
        "username": "user",
        "token_type": "access_token",
        "exp": "2020-05-13T00:00:00z",
        "iat": "2020-05-13T00:00:00z",
        "nbf": "2020-05-13T00:00:00z",
        "sub": "uuid",
        "aud": "someone",
        "iss": "authorization server",
        "jti": "unique id"
    }

    resp = Response(content, status=200, mimetype="application/json")

    return resp

@app.route('/test/userdata', methods=['GET'])
def get_userdata():
    pass

@app.route('/login', methods=['GET'])
def login():
    if 'username' in request.args and 'password' in request.args:
        username = request.args['username']
        password = request.args['password']
        return jsonify("success")
    return jsonify("fail")

@app.errorhandler(404)
def api_not_found(e):
    msg = {'message': 'Not Found: This URL'}
    return Response(msg, status=404, mimetype='application/json')

app.run()
