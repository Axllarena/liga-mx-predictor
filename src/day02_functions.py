home_teams = ["America", "Chivas", "Cruz Azul", "Monterrey", "America", "Monterrey"]
away_teams = ["Cruz Azul", "Monterrey", "Chivas", "America", "Chivas", "Cruz Azul"]
home_goals = [0, 0, 3, 1, 2, 2]
away_goals = [1, 0, 1, 1, 0, 2]

def get_match_result(home_goals, away_goals):
    if (home_goals > away_goals):
        return "home_win"
    elif home_goals < away_goals:
        return "away_win"
    else:
        return "draw"

    
#for i in range (len(home_teams)):
 #   print(get_match_result(home_goals[i], away_goals[i]))

def describe_match(home_team, away_team, home_goals, away_goals):

    if (get_match_result(home_goals, away_goals) == "home_win"):
        return (f"{home_team} defeated {away_team} {home_goals} - {away_goals}")
    elif (get_match_result(home_goals, away_goals) == "away_win"):
        return (f"{away_team} defeated {home_team} {away_goals} - {home_goals}")
    else:
        return (f"{away_team} drew with {home_team} {away_goals} - {home_goals}")

for i in range(len(home_teams)):
    print(describe_match(home_teams[i], away_teams[i], home_goals[i], away_goals[i]))


def calculate_totals(home_goals, away_goals):
    goals = 0
    draws = 0
    for i in range(len(home_goals)):
        if home_goals[i] == away_goals[i]:
            draws += 1
        goals += home_goals[i] + away_goals[i]
    return goals, draws

print("\n")
totals = calculate_totals(home_goals, away_goals)
print(f"Total goals scored: {totals[0]}")
print(f"Total draws: {totals[1]}")