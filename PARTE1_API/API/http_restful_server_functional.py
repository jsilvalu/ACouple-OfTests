#!/usr/bin/env python

# Telefonica CDO QA Team
# qacdo@telefonica.com

# The following script is based on these examples:
#   > https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
#   > https://gist.github.com/miguelgrinberg/5614326
import json

from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_httpauth import HTTPBasicAuth

from multiprocessing import Pool
from multiprocessing import cpu_count

app = Flask(__name__, static_url_path = "")
auth = HTTPBasicAuth()
LOCATORS_VALUE = "locators"
SPORTS_VALUE = "sports"
cms_file = "cms.json"
rse_file = "rse.json"
sports_file = "sports.json"
rse_sports_file = "rse_sports.json"
api_version = "2.0.0"

def load_file_json(file):
    with open(file,"r") as f:
        return json.loads(f.read())

def load_jsons(type, response_type):
    """
    :param response_type: full|selenium|appium
    :return:
    """
    base = {"version":api_version, "type": response_type}
    if type == SPORTS_VALUE:
        body = load_file_json(sports_file)
        if response_type == "full":
            base["football"] = body["football"]
            base["cycling"] = body["cycling"]
        elif response_type == "football":
            base["football"] = body["football"]
        elif response_type == "cycling":
            base["cycling"] = body["cycling"]
    elif type == LOCATORS_VALUE:
        body = load_file_json(cms_file)
        if response_type == "full":
            base["appium"] = body["appium"]
            base["selenium"] = body["selenium"]
        elif response_type == "selenium":
            base["selenium"] = body["selenium"]
        elif response_type == "appium":
            base["appium"] = body["appium"]

    return base

@auth.get_password
def get_password(username):
    if username == '3ntr3v1st4':
        return 't3cn1c4'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)
    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)


@app.route('/')
def index():
    msg = """
    This is a HTTP RESTful web service developed for being used as part of QA CDO Interviews.
    Version: 2.0
    """
    return msg

@app.route('/api/{api_version}/cms'.format(api_version=api_version), methods = ['GET'])
@auth.login_required
def get_locators():
    return jsonify(load_jsons(LOCATORS_VALUE, "full"))

@app.route('/api/{api_version}/sports'.format(api_version=api_version), methods = ['GET'])
@auth.login_required
def get_sports():
    return jsonify(load_jsons(SPORTS_VALUE, "full"))

@app.route('/api/{api_version}/cms/<string:type_id>'.format(api_version=api_version), methods = ['GET'])
@auth.login_required
def get_locators_by_id(type_id):
    if type_id not in ["full","selenium","appium"]:
        abort(404)
    return jsonify(load_jsons(LOCATORS_VALUE, type_id))

@app.route('/api/{api_version}/sports/<string:type_id>'.format(api_version=api_version), methods = ['GET'])
@auth.login_required
def get_sports_by_id(type_id):
    if type_id not in ["full","cycling","football"]:
        abort(404)
    return jsonify(load_jsons(SPORTS_VALUE, type_id))

@app.route('/api/{api_version}/rse'.format(api_version=api_version), methods = ['GET'])
@auth.login_required
def get_rse():
    result = load_file_json(rse_file)
    return jsonify(result)

@app.route('/api/{api_version}/rsesports'.format(api_version=api_version), methods = ['GET'])
@auth.login_required
def get_rse_sports():
    result = load_file_json(rse_sports_file)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', threaded=True)

