import pygame as pg


class Sound:
	def __init__(self, game):
		self.game = game
		pg.mixer.init()
		self.path = 'resources/sound/'
		self.theme = pg.mixer.music.load(self.path + 'theme.mp3')
		
		self.npc_pain = pg.mixer.Sound(self.path + 'npc_pain.mp3')
		self.npc_death = pg.mixer.Sound(self.path + 'npc_death.mp3')
		self.npc_shot = pg.mixer.Sound(self.path + 'pistol.mp3')
		
		self.player_pain = pg.mixer.Sound(self.path + 'player_pain.mp3')
		self.pistol = pg.mixer.Sound(self.path + 'pistol.mp3')
		