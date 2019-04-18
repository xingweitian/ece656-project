use lahman2016;

update HallOfFame
set playerID = 'drewjd01'
where playerID = 'drewj.01';

update Salaries
set Salaries.playerID = (
  select playerID
  from Master
  where Salaries.playerID = Master.bbrefID)
where Salaries.playerID not in (select playerID from Master);

update Salaries
set Salaries.teamID = (
  select teamID from Teams where Salaries.teamID = Teams.teamIDBR and Salaries.yearID = Teams.yearID)
where Salaries.teamID not in (select teamID from Teams);
