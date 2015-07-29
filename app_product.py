from flask import Flask, jsonify, Response
import ujson as json
app = Flask(__name__)
import os

@app.route('/products', methods = ['GET'])
@app.route('/products', methods = ['POST'])
def products():
    params = {}
    result = []
    data = _get_products_data(params)
    ret = Response(response=data,
                    status=200,
                    mimetype="application/json")
    return ret

def _get_products_data(params):
    fname = os.path.join(os.getcwd(), 'prod.json')
    f = open(fname, 'r')
    data = f.read()
    f.close()
    return data

if __name__ == "__main__":
    app.run()
