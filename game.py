from bisect import bisect_left
from random import randint


MAX_LAWN = 6
MAX_BARRICADE = 10
MAX_GARAGE = 10
MAX_KILLS = 10
LEVELS_GARAGE = [-1, 3, 6, 8, 10]
SUCCESS_LAWN = 3
SUCCESS_BARRICADE = 3
SUCCESS_GARAGE = 5


class Game:
	def roll_dice(self):
		return randint(1, 6)

	def add_lawn(self, val):
		self.lawn += val
		self.lawn = min(self.lawn, MAX_LAWN)

	def add_barricade(self, val):
		self.barricade += val
		self.barricade = min(self.barricade, MAX_BARRICADE)
		if self.barricade <= 0:
			self.lost()

	def add_garage(self, val):
		self.garage += val
		if self.garage >= MAX_GARAGE:
			self.win()

	def add_kills(self, val):
		self.kills += val
		if self.kills >= MAX_KILLS:
			self.kills -= MAX_KILLS
			self.bonus()

	def bonus(self):
		self.info(2)
		match int(input()):
			case 1:
				self.lawn = 0
			case 2:
				self.add_garage(1)
			case 3:
				self.skip_spawn = 1
			case 4:
				self.add_barricade(3)

	def reset(self):	
		self.lawn = 0
		self.barricade = MAX_BARRICADE
		self.garage = 0
		self.kills = 0
		self.skip_spawn = 0
		self.result = 0

	def info(self, tp):
		print(self.lawn, self.barricade, self.garage, self.kills, self.skip_spawn, self.result, tp)

	def win(self):
		self.result = 1
		self.info(0)
		exit()

	def lost(self):
		self.result = -1
		self.info(0)
		exit()

	def roll_lawn(self):
		res = self.roll_dice()
		if res >= SUCCESS_LAWN and self.lawn:
			self.add_lawn(-1)
			self.add_kills(1)
		self.info(-res)

	def roll_barricade(self):
		res = self.roll_dice()
		if res >= SUCCESS_BARRICADE:
			self.add_barricade(1)
		self.info(-res)

	def roll_garage(self):
		res = self.roll_dice()
		if res >= SUCCESS_GARAGE:
			self.add_garage(1)
		self.info(-res)

	def roll(self, line):
		for i in range(line.count('L')):
			self.roll_lawn()
		for i in range(line.count('B')):
			self.roll_barricade()
		for i in range(line.count('G')):
			self.roll_garage()

	def go(self):
		if not self.skip_spawn:
			self.add_lawn(bisect_left(LEVELS_GARAGE, self.garage))
		self.skip_spawn = 0
		self.info(1)
		self.roll(list(input().upper()))
		self.add_barricade(-self.lawn)

	def __init__(self):
		self.reset()

	def start(self):
		while True:
			self.go()


if __name__ == '__main__':
	Game().start()