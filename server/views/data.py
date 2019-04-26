# @Time    : 3/20/2019 1:08 AM
# @Author  : Weitian Xing
# @FileName: data.py

from flask import Blueprint, jsonify, request

from ..config import DB_CONFIG_PATH
from ..db.data_clean import print_dirty_data, data_clean
from ..db.data_revert import data_revert
from ..db.data_analysis import analysis
from ..db.data_validate import validate
from ..db.db_util import connect_with_db

data_blueprint = Blueprint("data", __name__)

db_connection = connect_with_db(DB_CONFIG_PATH)


@data_blueprint.route("/dirty")
def dirty():
    return print_dirty_data()


@data_blueprint.route("/clean")
def clean():
    user_choice = request.args.get("user_choice")
    user_choice_list = user_choice.split()
    data_clean(user_choice_list, db_connection)
    return "Cleaning data complete."


@data_blueprint.route("/analyze")
def analyze():
    analysis()
    return "TODO"


@data_blueprint.route("/validate")
def validate():
    validate()
    return "TODO"


@data_blueprint.route("/revert")
def revert():
    with db_connection.cursor() as cursor:
        data_revert(cursor)
    return "Data revert complete."
