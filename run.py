# @Time    : 3/20/2019 12:17 AM
# @Author  : Weitian Xing
# @FileName: run.py


import argparse

from client.client import run_client
from server.server import run_server

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-c", "--client", dest="client", help="run client", action="store_true")
group.add_argument("-s", "--server", dest="server", help="run server", action="store")

args = parser.parse_args()

if args.server:
    host, port = args.server.split(":")
    run_server(host, port)

if args.client:
    run_client()
