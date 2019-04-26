# @Time    : 4/5/2019 11:08 PM
# @Author  : Weitian Xing
# @FileName: commands.py
import os
import sys
from urllib.parse import urljoin

from .base_request import get

def data_clean():
    server_url = os.environ.get("server_url")
    print(get(urljoin(server_url, "data/dirty")).text)
    user_choice = input("Please type the numbers that you choose, e.g., 1 2 3: ")
    print(get(urljoin(server_url, "data/clean"), **{"user_choice": user_choice}).text)


def data_analysis():
    server_url = os.environ.get("server_url")
    print("""
    
    In this part, we are going to analyze if the rank of all star player will effect
    the player to enter the hall of fame.
    
    """)
    print("Waiting for complete, please be patient...")
    print(get(urljoin(server_url, "data/analyze")).text)


def analysis_validate():
    server_url = os.environ.get("server_url")
    print("Waiting for complete, please be patient...")
    print(get(urljoin(server_url, "data/validate")).text)


def data_revert():
    server_url = os.environ.get("server_url")
    print("Waiting for complete, please be patient...")
    print(get(urljoin(server_url, "data/revert")).text)


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
    4. Revert Data
    5. Exit
    
    Usage: type the number of the operation
    
    For example:
    
    Please choose operation: 1
        
    ======================================    
    """)
    while 1:
        user_input = input("Please choose operation(the number of the operation):")
        switch(user_input)
