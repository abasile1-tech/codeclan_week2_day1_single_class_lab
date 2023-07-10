from src.team import Team

team1 = Team("Patriots",["Tom Brady","Cory Dillon"],"Bill Belichick")

team1.add_player("Jean-Ralphio Saperstein")

print(team1.has_player("Tom Brady"))
print(team1.has_player("Mario"))

print(f"Team Points Before Winning: {team1.points}")
team1.play_game(True)
print(f"Team Points After Winning: {team1.points}")