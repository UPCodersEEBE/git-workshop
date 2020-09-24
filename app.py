# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:35:36 2020

@author: crull
"""


# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_name():
    return "hello"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)