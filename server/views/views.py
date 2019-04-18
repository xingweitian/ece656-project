# @Time    : 4/18/2019 10:55 AM
# @Author  : Weitian Xing
# @FileName: views.py

from .data import data_blueprint
from ..app import app

app.register_blueprint(blueprint=data_blueprint, url_prefix="/data")
