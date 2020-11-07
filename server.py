import os
from flask import Flask, jsonify, request, abort


app = Flask(__name__)

counter = {}

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

        package_name = request.json['package_name']
        func_name = request.json['func_name']

        if package_name not in counter.keys():
            counter[package_name] = {func_name: 1}

        elif package_name in counter.keys() and (func_name not in counter[package_name].keys()):
            counter[package_name][func_name] = 1
        else:
            counter[package_name][func_name] += 1

        # return jsonify({"success": 1})


@app.route("/api", methods=['GET'])
def query():
    """retrieve count for a given package:func.
    """
    package = request.args.get('package')
    func = request.args.get('func')
    identifier = package + ':' + func

    try:
        return jsonify({identifier: counter[package][func]})
    except:
        return "package:method does not exist"


if __name__ == '__main__':
    app.run(host=os.getenv('LISTEN', '0.0.0.0'), port=int(os.getenv('PORT', '5000')))