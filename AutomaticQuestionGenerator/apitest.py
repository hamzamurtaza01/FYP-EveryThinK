from flask import Flask, request, jsonify
# import pandas as pd
import csv
from collections import defaultdict 

from flask.json import jsonify

from QGMAIN import HELLO
app = Flask(__name__)
import json

@app.route('/', methods=['GET','POST'])
def getdata2():
    qg=HELLO()
    return jsonify({"result":qg})
    # return json.dumps({"result":qg})


@app.route('/postData3', methods=['POST'])
def getdata():
    request_data = request.get_json()
    # print()

    name = request_data['data']
    # ab krna done
    print("print name " + str(name))
    return str(name['name'])


# o bhai name same mt rakho


@app.route('/postData', methods=['POST'])
def getdatas():
    request_data = request.get_json()
    # name = request_data["name"]

    name = request_data['data']
    # name = "itching"
    return name


if __name__ == '__main__':
    app.run(port=8888,host='127.0.0.1',debug=True)
