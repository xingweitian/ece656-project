# @Time    : 4/13/2019 4:59 PM
# @Author  : Weitian Xing
# @FileName: config.py

import os

from config import ROOT_DIR

DB_CONFIG_PATH = os.path.join(ROOT_DIR, "server", "db.json")

LAHMAN2016_PATH = os.path.join(ROOT_DIR, "server", "db", "lahman2016.sql")
