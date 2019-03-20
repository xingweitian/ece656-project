# @Time    : 3/20/2019 12:22 AM
# @Author  : Weitian Xing
# @FileName: server.py

# Do NOT change this file

from .app import app


def run_server(host, port):
    import server.views
    app.run(host, port)
