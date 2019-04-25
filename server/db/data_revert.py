# @Time    : 4/24/2019 10:58 PM
# @Author  : Weitian Xing
# @FileName: data_revert.py
import re
import time
import tqdm

from server.config import LAHMAN2016_PATH, DB_CONFIG_PATH


def exec_sql_file(cursor, sql_file):
    print("\n[INFO] Executing SQL script file: '%s'" % (sql_file))
    statement = ""

    with open(sql_file) as f:
        for line in tqdm.tqdm(f.readlines()):
            if re.match(r'--', line):
                continue
            if line == "\n":
                continue
            line = line.rstrip("\n")
            if not re.search(r'[^-;]+;', line):
                statement = statement + line
            else:
                statement = statement + line
                try:
                    time.sleep(0.1)
                    cursor.execute(statement)
                except Exception as e:
                    print(str(e))
                statement = ""


def data_revert(cursor):
    exec_sql_file(cursor, LAHMAN2016_PATH)


if __name__ == "__main__":
    from server.db.db_util import connect_with_db

    db_connection = connect_with_db(DB_CONFIG_PATH)
    with db_connection.cursor() as cursor:
        data_revert(cursor)
