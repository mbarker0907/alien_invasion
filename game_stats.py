class GameStats():
	"""Track statistics for Alien Invasion."""

	def __init__(self, ai_settings):
		"""Initialize statistics."""
		self.ai_settings = ai_settings
		self.reset_stats()
<<<<<<< HEAD
		# Start game in an inactive state.
		self.game_active = False
=======
>>>>>>> parent of 9f604d1 (Game freezes when all of player's ships have been destroyed.)

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.ai_settings.ship_limit