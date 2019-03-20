# @Time    : 3/20/2019 1:08 AM
# @Author  : Weitian Xing
# @FileName: data.py

from flask import Blueprint, jsonify

from ..app import app

data_blueprint = Blueprint('data', __name__)


@app.route("/clean")
def clean():
    return jsonify("TODO")


@app.route("/analyze")
def analyze():
    return jsonify("TODO")


@app.route("/validate")
def validate():
    return jsonify("TODO")
