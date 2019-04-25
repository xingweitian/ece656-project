# @Time    : 4/18/2019 1:30 AM
# @Author  : Weitian Xing
# @FileName: data_clean.py


def print_dirty_data():
    return """
    
    Some data need to be cleaned:
    
    [1] Missing data in HallOfFame. Changing playerID from 'drewjd01' to 'drewj.01' in HallOfFame cam solve this problem.
    [2] Missing data in Salaries. Some playerIDs in Salaries come from Master.bbrefID, find all of them and change them 
        to corresponding playerID in Master. 
    [3] Missing data in Salaries. There are some teamIDs in Salaries come from Teams.teamIDBR, find all of them and change 
        them to corresponding teamID in Teams.
    """


def data_clean(choices: list, db_connection):
    add_primary_key(db_connection)
    for each in choices:
        exec_sql(each, db_connection)


def exec_sql(num: str, db_connection):
    with db_connection.cursor() as cursor:
        if num == "1":
            sql = "update HallOfFame set playerID = 'drewjd01' where playerID = 'drewj.01'"
        elif num == "2":
            sql = "update Salaries set Salaries.playerID = ( select playerID from Master where Salaries.playerID = Master.bbrefID) where Salaries.playerID not in (select playerID from Master)"
        else:
            sql = "update Salaries set Salaries.teamID = ( select teamID from Teams where Salaries.teamID = Teams.teamIDBR and Salaries.yearID = Teams.yearID) where Salaries.teamID not in (select teamID from Teams)"
        try:
            cursor.execute(sql)
        except Exception as e:
            print(str(e))


def add_primary_key(db_connection):
    with db_connection.cursor() as cursor:
        sqls = [
            "alter table Master add primary key (playerID)",
            "alter table Salaries add primary key (playerID, teamID, yearID)",
            "alter table Teams add primary key (teamID, yearID);"
        ]
        for sql in sqls:
            cursor.execute(sql)