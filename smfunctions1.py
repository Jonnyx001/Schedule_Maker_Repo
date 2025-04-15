import math
import copy
from smclassesobjects1 import Matchup
from smclassesobjects1 import Week

# Allows user to build a list of team names. Strings.
def input_teams():
    teamnum = int(input("How many teams are in your league?: "))
    teamlist = []
    for i in range(teamnum):
        team = input(f"Enter team {i + 1}: ")
        teamlist.append(team)
    print("Registration complete.")
    return teamlist

# User inputs number of weeks. This outputs a list of week objects with a name like "Week 1" ready to have matchups appended to it as nested objects.
def generate_weeks(weeknum):
    weeks = []
    for i in range(weeknum):
        newweek = Week(f"Week {i + 1}")
        weeks.append(newweek)
    return weeks

# Takes a list of team objects and generates a list of every possible matchup, home and away. Also assigns it a "uses left" value.
def generate_matchups(teamlist, weeknum):
    matchups = []
    games_in_week = math.floor(len(teamlist) / 2)
    games_in_season = games_in_week * weeknum
    for hometeam in teamlist:
        for awayteam in teamlist:
            if hometeam != awayteam:
                newmatchup = Matchup(hometeam, awayteam, None)
                matchups.append(newmatchup)
    for matchup in matchups:
        matchup.usesleft = (games_in_season / len(matchups))
    return matchups

# This outputs a list of week objects with a name like "Week 1" and full matchup slots. 
def generate_schedule(weeks, matchups, teamlist):
    schedule = []
    games_in_week = math.floor(len(teamlist) / 2) # CAN CREATE ISSUES DOWN THE LINE WITH SCALING OR ODD AMOUNT OF TEAMS! also using this for troubleshooting
    print(f"Each week will have {games_in_week} games.") # Only here for troubleshooting
    for week in weeks:
        print(f"Generating {week.name}")
        matchupcount = 0
        print(f"Matchup count is {matchupcount}")
        matchupscopy = matchups.copy() #deepcopy this? caused issues b4.
        print(f"Made fresh copy of matchups:")
        for matchup in matchupscopy: print(f"{matchup.hometeam} vs {matchup.awayteam} | Uses left = {matchup.usesleft}.") # Only here for troubleshooting
        usedteams = []
        print(f"Reset usedteams: {usedteams}") # Only here for troubleshooting
        currentmatchup = 1
        print(f"current matchup is now {currentmatchup}") # Only here for troubleshooting
        for matchupcopy in matchupscopy:
            for value in week.__dict__.values(): # Only here for troubleshooting vvvvv
                if isinstance(value, Matchup):
                    matchupcount += 1
                    print(f"Matchup count is now {matchupcount}") #
                    if matchupcount >= games_in_week:
                        break
                    else:
                        print(f"Matchup count is {matchupcount}. Hasnt reached {games_in_week}. Continuing...") # Only here for troubleshooting^^^^^
            print(f"looping through matchupscopy. Found {matchupcopy.hometeam} vs {matchupcopy.awayteam} | Uses left = {matchupcopy.usesleft}")
            if matchupcopy.usesleft <= 0:
                matchups.remove(matchupcopy)
                print("Removed. (Been used enough this season)")
            else:
                setattr(week, f"Matchup {currentmatchup}", matchupcopy)
                print(f"Available. Matchup {currentmatchup} was added to {week.name}")
                currentmatchup += 1
                print(f"currentmatchup incremented to: {currentmatchup}")
                matchupcopy.usesleft -= 1
                print(f"usesleft for {matchupcopy.hometeam} vs {matchupcopy.awayteam} was decremented to {matchupcopy.usesleft}")
                team1 = matchupcopy.hometeam
                team2 = matchupcopy.awayteam
                usedteams.extend([team1, team2])
                print(f"Used teams: {usedteams}")
                for matchupcopy in matchupscopy[:]: # when i return to remember to mess with these [:]
                    print(f"looping through matchupscopy AGAIN (trying to remove ones with same teams)... Found {matchupcopy.hometeam} vs {matchupcopy.awayteam}. Uses left = {matchupcopy.usesleft}")
                    if matchupcopy.hometeam in usedteams or matchupcopy.awayteam in usedteams:
                        matchupscopy.remove(matchupcopy)
                        print(f"removed (been used this week)") # try using else statements to see if i catch anything that can help me debug
                    else:
                        print(f"KEPT")
        schedule.append(week)
        print(f"{week.name} was added to schedule")
    return schedule
            

                
# Maybe easier to not do home/away. just flip them later?