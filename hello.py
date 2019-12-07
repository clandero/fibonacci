from cloudant import Cloudant
from flask import Flask, render_template, request, jsonify
import atexit
import os
import json

app = Flask(__name__, static_url_path='')
port = int(os.getenv('PORT', 8000))

@app.route('/<int:n>')
def index(n):
    if n > 2222:
        n = 2222
    n_menos_2 = 0
    n_menos_1 = 0
    actual = 1
    for i in range(1,n):
        n_menos_2 = n_menos_1
        n_menos_1 = actual
        actual = n_menos_1 + n_menos_2
    return str(actual)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
