# Match detail arrays
home_teams = ["America", "Chivas", "Cruz Azul", "Monterrey", "America", "Monterrey"]
away_teams = ["Cruz Azul", "Monterrey", "Chivas", "America", "Chivas", "Cruz Azul"]
home_goals = [0, 0, 3, 1, 2, 2]
away_goals = [1, 0, 1, 1, 0, 2]

total_goals = 0
total_draws = 0

for i in range (len(home_teams)):
    if home_goals[i] > away_goals[i]:
        print(f"Final score: {home_teams[i]} defeated {away_teams[i]}, {home_goals[i]} - {away_goals[i]}")
    elif home_goals[i] < away_goals[i]:
        print(f"Final score: {home_teams[i]} lost to {away_teams[i]}, {home_goals[i]} - {away_goals[i]}")
    else:
        print(f"Final score: {home_teams[i]} draw to {away_teams[i]}, {home_goals[i]} - {away_goals[i]}")
        total_draws +=1
    
    total_goals+= home_goals[i] + away_goals[i]
        
print(f"Total goals: {total_goals}")        
print(f"Total draws {total_draws}")
    
       