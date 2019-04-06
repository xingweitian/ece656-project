# @Time    : 3/20/2019 1:22 AM
# @Author  : Weitian Xing
# @FileName: check.py
import os
from urllib.parse import urljoin

from . import base_request


def check_server():
    server_host = os.environ.get("ECE656_PROJECT_SERVER_HOST", "127.0.0.1")
    server_port = os.environ.get("ECE656_PROJECT_SERVER_PORT", "8000")
    if server_host and server_port:
        _url = server_host + ":" + server_port
        if not _url.startswith("http://"):
            _url = "http://" + _url
        if not _url.endswith("/"):
            _url = _url + "/"
            os.environ["server_url"] = _url
        full_url = urljoin(_url, "ping")
        try:
            req = base_request.get(full_url)
            if req.status_code == 200:
                return True
        except:
            return False
    return False
