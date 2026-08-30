matches = [
    {"home_team": "America", "away_team": "Cruz Azul", "home_goals": 0, "away_goals": 1},
    {"home_team": "Chivas", "away_team": "Monterrey", "home_goals": 0, "away_goals": 0},
    {"home_team": "Cruz Azul", "away_team": "Chivas", "home_goals": 3, "away_goals": 1},
    {"home_team": "Monterrey", "away_team": "America", "home_goals": 1, "away_goals": 1},
    {"home_team": "America", "away_team": "Chivas", "home_goals": 2, "away_goals": 0},
    {"home_team": "Monterrey", "away_team": "Cruz Azul", "home_goals": 2, "away_goals": 2},
]

for match in matches:
    print(f"{match["home_team"]} vs {match["away_team"]}: {match["home_goals"]} - {match["away_goals"]} ")