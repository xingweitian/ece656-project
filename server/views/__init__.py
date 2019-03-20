# @Time    : 3/20/2019 1:01 AM
# @Author  : Weitian Xing
# @FileName: __init__.py

from .data import data_blueprint
from ..app import app

app.register_blueprint(blueprint=data_blueprint, url_prefix="/data")


@app.route("/ping")
def ping():
    return "pong"
