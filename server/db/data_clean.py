# @Time    : 4/18/2019 1:30 AM
# @Author  : Weitian Xing
# @FileName: data_clean.py


def print_dirty_data():
    return """
    [1] Missing data in HallOfFame. Changing playerID from 'drewjd01' to 'drewj.01' in HallOfFame cam solve this problem.
    [2] Missing data in Salaries. Some playerIDs in Salaries come from Master.bbrefID, find all of them and change them 
        to corresponding playerID in Master. There are also some teamIDs in Salaries come from Teams.teamIDBR, find all of them
        and change them to corresponding teamID in Teams.
    [3] Missing data in CollegePlaying.
    [4] Missing data in Fielding.
    """
