# @Time    : 4/18/2019 1:30 AM
# @Author  : Weitian Xing
# @FileName: data_clean.py


def print_dirty_data():
    return """
    
    Some data need to be cleaned:
    
    [1] Missing data in HallOfFame. Changing playerID from 'drewjd01' to 'drewj.01' in HallOfFame cam solve this problem.
    [2] Missing data in Salaries. Some playerIDs in Salaries come from Master.bbrefID, find all of them and change them 
        to corresponding playerID in Master. There are also some teamIDs in Salaries come from Teams.teamIDBR, find all of them
        and change them to corresponding teamID in Teams.
    # [3] Missing data in CollegePlaying.
    # [4] Missing data in Fielding.
    
    """


def data_clean(choices: list, db_connection):
    for each in choices:
        exec_sql(each, db_connection)


def exec_sql(num: str, db_connection):
    with db_connection.cursor() as cursor:
        if num == "1":
            sql = "update HallOfFame set playerID = 'drewjd01' where playerID = 'drewj.01'"
        else:
            sql = "update Salaries set Salaries.playerID = ( select playerID from Master where Salaries.playerID = Master.bbrefID) where Salaries.playerID not in (select playerID from Master)"
        cursor.execute(sql)
