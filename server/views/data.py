# @Time    : 3/20/2019 1:08 AM
# @Author  : Weitian Xing
# @FileName: data.py

from flask import Blueprint, jsonify

from ..app import app
from ..config import DB_CONFIG_PATH
from ..db.db_util import connect_with_db

data_blueprint = Blueprint('data', __name__)

db_connection = connect_with_db(DB_CONFIG_PATH)


@app.route("/clean")
def clean():
    return jsonify("TODO")


@app.route("/analyze")
def analyze():
    return jsonify("TODO")


@app.route("/validate")
def validate():
    return jsonify("TODO")
