# @Time    : 3/20/2019 1:01 AM
# @Author  : Weitian Xing
# @FileName: __init__.py

from flask import request

from ..app import app


@app.route("/ping")
def ping():
    return "pong"


def shutdown_server():
    func = request.environ.get("werkzeug.server.shutdown")
    if func is None:
        raise RuntimeError("Not running with the Werkzeug Server")
    func()


@app.route("/exit")
def exit():
    shutdown_server()
    return "Server shutting down."


from . import views
