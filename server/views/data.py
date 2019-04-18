# @Time    : 3/20/2019 1:08 AM
# @Author  : Weitian Xing
# @FileName: data.py

from flask import Blueprint, jsonify

from ..config import DB_CONFIG_PATH
from ..db.data_clean import print_dirty_data
from ..db.db_util import connect_with_db

data_blueprint = Blueprint("data", __name__)

db_connection = connect_with_db(DB_CONFIG_PATH)


@data_blueprint.route("/dirty")
def dirty():
    return print_dirty_data()


@data_blueprint.route("/clean")
def clean():
    return jsonify("TODO")


@data_blueprint.route("/analyze")
def analyze():
    return jsonify("TODO")


@data_blueprint.route("/validate")
def validate():
    return jsonify("TODO")
