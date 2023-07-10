class Team:
	def __init__(self, name, players, coach):
		self.name = name
		self.players = players
		self.coach = coach
		self.points = 0

	def add_player(self, name):
		self.players.append(name)

	def has_player(self, name):
		return name in self.players

	def play_game(self, outcome):
		if outcome:
			self.points += 3