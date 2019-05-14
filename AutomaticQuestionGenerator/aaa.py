from flask import Flask, request, jsonify
# import pandas as pd
import csv
from collections import defaultdict
from flask.json import jsonify
from text_similarity_Final import dog
# from QGMAIN import HELLO
app = Flask(__name__)
import json


@app.route('/', methods=['GET'])
def getdata2():
    qg=dog()
    return jsonify({"result":qg})

#
# @app.route('/', methods=['GET'])
# def getdata2():
#     qg=HELLO()
#     return jsonify({"result":qg})
#     # return json.dumps({"result":qg})

if __name__ == '__main__':
    app.run(port=8000,host='localhost',debug=True)