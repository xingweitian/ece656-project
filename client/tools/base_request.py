# @Time    : 3/20/2019 1:23 AM
# @Author  : Weitian Xing
# @FileName: base_request.py
import requests


def get(url, **kwargs):
    return requests.get(url, kwargs)


def post(url, data):
    return requests.post(url, data)
