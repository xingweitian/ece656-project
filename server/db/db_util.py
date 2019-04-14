# @Time    : 4/13/2019 3:07 PM
# @Author  : Weitian Xing
# @FileName: db_util.py

import json

import pymysql.cursors


def connect_with_db(config_path: str):
    with open(config_path, "r") as f:
        _config = json.load(f)
    return pymysql.connect(host=_config["host"],
                           port=_config["port"],
                           user=_config["user"],
                           password=_config["password"],
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor
                           )


if __name__ == "__main__":
    from ..config import DB_CONFIG_PATH

    con = connect_with_db(DB_CONFIG_PATH)
    print(con.server_status)
