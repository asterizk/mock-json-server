from flask import Flask, jsonify, request, abort
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

RESPONSES_DIR = './responses'

def route_to_filename(route: str, method: str) -> str:
    route_key = route.lstrip('/').replace('/', '-')
    return os.path.join(RESPONSES_DIR, f"{route_key}_{method.upper()}.json")

def load_response(route: str, method: str):
    filename = route_to_filename(route, method)
    if not os.path.isfile(filename):
        abort(404, description=f"No mock response for {route} [{method}]")
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def catch_all(path):
    route = '/' + path
    response = load_response(route, request.method)
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5050)
