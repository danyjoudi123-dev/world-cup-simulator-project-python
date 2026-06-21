import random 

group = {
    "A": {
    'Argentina': 95,
    'Spain': 95,
    'Iraq': 65,
    'Australia': 74,
    }
}

qualifiers = []

for group:
    teams = play_group()
    qualifiers.append()
    qualifiers.append()

teams = list(group["A"].keys())

def play_group(teams):
    table = {}
    for team in teams: 
        table[team] = {'played': 0, 'points': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'gf': 0, 'ga': 0}

    for i in range(len(teams)):
        for x in range(i+1, len(teams)):
            team1, team2, goal1, goal2 = play_match(teams[i], teams[x], group["A"])
            if goal1 > goal2:
                table[team1]['points'] += 3
                table[team1]['played'] += 1
                table[team1]['wins'] += 1
                table[team1]['gf'] += goal1
                table[team1]['ga'] += goal2
                table[team2]['played'] += 1
                table[team2]['losses'] += 1
                table[team2]['gf'] += goal2
                table[team2]['ga'] += goal1
            elif goal1 == goal2: 
                table[team1]['points'] += 1
                table[team1]['played'] += 1
                table[team1]['draws'] += 1
                table[team1]['gf'] += goal1
                table[team1]['ga'] += goal2
                table[team2]['points'] += 1
                table[team2]['played'] += 1
                table[team2]['draws'] += 1
                table[team2]['gf'] += goal2
                table[team2]['ga'] += goal1
            elif goal1 < goal2: 
                table[team1]['played'] += 1
                table[team1]['losses'] += 1
                table[team1]['gf'] += goal1
                table[team1]['ga'] += goal2
                table[team2]['played'] += 1
                table[team2]['wins'] += 1
                table[team2]['points'] += 3
                table[team2]['gf'] += goal2
                table[team2]['ga'] += goal1
            print("------------------------------")
    sorted_table = print_table(table)
    return sorted_table
    
def print_table(table):
    sorted_table = sorted(
        table.items(),
        key=lambda x: (x[1]["points"], x[1]["gf"] - x[1]["ga"], x[1]["gf"]),
        reverse=True
    )

    print("Team        P  W  D  L  GF  GA  GD  Pts")
    print("-----------------------------------------")

    for team, stats in sorted_table:
        gd = stats["gf"] - stats["ga"]

        print(
            team.ljust(10),
            str(stats["played"]).rjust(1),
            str(stats["wins"]).rjust(2),
            str(stats["draws"]).rjust(2),
            str(stats["losses"]).rjust(2),
            str(stats["gf"]).rjust(3),
            str(stats["ga"]).rjust(3),
            str(gd).rjust(3),
            str(stats["points"]).rjust(4)
        )
    return sorted_table 

def generate_goals(rating):
    goals = 0
    attacking_chance = rating / 20

    for i in range(int(attacking_chance)):
        goal = random.choice(['Goal', 'No Goal'])
        if goal == 'Goal':
            goals = goals + 1
    return(goals)


def play_match(team1, team2, group):

    print(team1 + ' vs ' + team2)
        
    rating1 = group[team1]
    rating2 = group[team2]


    goal1 = generate_goals(rating1)
    goal2 = generate_goals(rating2)
    print(team1 + ' ' + str(goal1) + ' - ' + str(goal2) + ' ' + team2)

    if goal1 > goal2:
        print(team1 + ' wins!')
    elif goal1 < goal2:
        print(team2 + ' wins!')
    elif goal1 == goal2:
        print('Draw!')
    
    result = team1, team2, goal1, goal2
    return result

play_group(teams)


