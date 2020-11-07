import os
from flask import Flask, jsonify, request, abort


app = Flask(__name__)

counter = {}
namespace = {}

@app.route('/')
def landing():
    """
    default action for localhost:5000
    # https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
    """
    return "hello world!"


@app.route('/api', methods=['PUT'])
def log():
    if not request.json:
        abort(400)
    else:
        print("func_name", request.json['func_name'])
        print("source", request.json['source'])
        print("key", request.json['key'])

        key = request.json['key']
        if key not in counter.keys():
            counter[key] = 1

            func_name = request.json['func_name']
            namespace[func_name] = key
        else:
            counter[key] += 1

        # return jsonify({"success": 1})


@app.route("/api/<func_name>", methods=['GET'])
def query(func_name):
    if func_name in namespace.keys():
        key = namespace[func_name]
        count = counter[key]
        return jsonify({"func_name": func_name, "count": count})
    else:
        return jsonify({"func_name": func_name, "count": 0})


if __name__ == '__main__':
    app.run(host=os.getenv('LISTEN', '0.0.0.0'), port=int(os.getenv('PORT', '5000')))