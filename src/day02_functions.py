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
    
for i in range (len(home_teams)):
    print(get_match_result(home_goals[i], away_goals[i]))
    