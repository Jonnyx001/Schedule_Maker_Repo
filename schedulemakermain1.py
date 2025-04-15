from smclassesobjects1 import Matchup
from smclassesobjects1 import Week

from smfunctions1 import input_teams
from smfunctions1 import generate_weeks
from smfunctions1 import generate_matchups
from smfunctions1 import generate_schedule

weeknum = int(input("How many weeks are in your regular season?: "))
teamlist = input_teams()

weeks = generate_weeks(weeknum)
matchups = generate_matchups(teamlist, weeknum)

schedule = generate_schedule(weeks, matchups, teamlist)

for week in schedule:
    print(week.name)
    for value in week.__dict__.values():
        if isinstance(value, Matchup):
            print(f"{value.hometeam} vs {value.awayteam}")
        

#shuffle team list so that the last teams dont guarantee to miss out playing each other.