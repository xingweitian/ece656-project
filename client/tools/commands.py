# @Time    : 4/5/2019 11:08 PM
# @Author  : Weitian Xing
# @FileName: commands.py
import os
import sys

from .base_request import get
from urllib.parse import urljoin


def data_clean():
    server_url = os.environ.get("server_url")
    print(get(urljoin(server_url, "data/dirty")))
    user_choice = input("Please type the numbers that you choose, e.g., 1 2 3: ")
    print(get(urljoin(server_url, "data/clean"), user_choice=user_choice))


def data_analysis():
    return "TODO"


def analysis_validate():
    return "TODO"


def data_revert():
    return "TODO"


def exit():
    print("You will logout.")
    server_url = os.environ.get("server_url")
    res = get(server_url + "exit")
    print(res.text)
    sys.exit(0)


def switch(command: str):
    swithcer = {
        "1": data_clean,
        "2": data_analysis,
        "3": analysis_validate,
        "4": data_revert,
        "5": exit
    }

    func = swithcer.get(command, lambda: "Invalid argument, please try again.")
    return func()


def commands():
    print(r"""
    ======================================
    ===========ECE 656 Project============
    ======================================
    
    1. Clean Data
    2. Analysis Data
    3. Validate Analysis
    4. Revert Data(Only After 1.)
    5. Exit
    
    Usage: type the number of the operation
    
    For example:
    
    Please choose operation: 1
        
    ======================================    
    """)
    while 1:
        user_input = input("Please choose operation(the number of the operation):")
        switch(user_input)
