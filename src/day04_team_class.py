matches = [
    {"home_team": "America", "away_team": "Cruz Azul", "home_goals": 0, "away_goals": 1},
    {"home_team": "Chivas", "away_team": "Monterrey", "home_goals": 0, "away_goals": 0},
    {"home_team": "Cruz Azul", "away_team": "Chivas", "home_goals": 3, "away_goals": 1},
    {"home_team": "Monterrey", "away_team": "America", "home_goals": 1, "away_goals": 1},
    {"home_team": "America", "away_team": "Chivas", "home_goals": 2, "away_goals": 0},
    {"home_team": "Monterrey", "away_team": "Cruz Azul", "home_goals": 2, "away_goals": 2},
]

class Team:
    def __init__(self, name):
        self.name = name
        self.played = 0
        self.won = 0
        self.drawn = 0
        self.lost = 0
        self.goals_for = 0
        self.goals_against = 0
        
    def points(self):
        return(self.won*3) + (self.drawn)
        
    
    def goals_diff(self):
        return self.goals_for - self.goals_against
       
    
        

teams = {}

def get_team(teams, name):
    
    if name not in teams:
        teams[name] = Team(name)
        
    return teams[name]


for match in matches:
    home = get_team(teams, match["home_team"])
    away = get_team(teams, match["away_team"])
    home.goals_for+=match["home_goals"]
    home.goals_against+=match["away_goals"]
    away.goals_for+=match["away_goals"]
    away.goals_against+=match["home_goals"]
    home.played+=1
    away.played+=1
    
    if match["home_goals"] > match["away_goals"]:
        home.won+=1
        away.lost+=1
    elif match["home_goals"] < match["away_goals"]:
        home.lost+=1 
        away.won+=1
    else:
        home.drawn+=1
        away.drawn+=1
              
    
#for team in teams.values():
   # print(f"{team.name}| W: {team.won} | D: {team.drawn}| L: {team.lost}|")

tabla = sorted(teams.values(), key=lambda team: (team.points(), team.goals_diff()), reverse=True)

for team in tabla:
    print(f"{team.name} | Pts: {team.points()} | W: {team.won} D: {team.drawn} L: {team.lost} | GD: {team.goals_diff()}")