# @Time    : 3/20/2019 1:02 AM
# @Author  : Weitian Xing
# @FileName: client.py
from .tools.check import check_server
from .tools.welcome import welcome_ascii_art
from .tools.commands import commands


def run_client():
    server_status = check_server()
    if not server_status:
        print("Please run server first. You can find tutorial in the README.md.")
        exit(-1)
    welcome_ascii_art()
    commands()
