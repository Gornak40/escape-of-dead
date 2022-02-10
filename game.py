from bisect import bisect_left
from random import randint


MAX_LAWN = 6
MAX_BARRICADE = 10
MAX_GARAGE = 10
MAX_KILLS = 10
GARAGE_LEVELS = [-1, 3, 6, 8, 10]
LAWN_SUCCESS = 3
BARRICADE_SUCCESS = 3
GARAGE_SUCCESS = 5


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

# TODO
	def bonus(self):
		print('Bonus')

	def reset(self):	
		self.lawn = 0
		self.barricade = MAX_BARRICADE
		self.garage = 0
		self.kills = 0

	def info(self):
		print(f'Lawn: {self.lawn}')
		print(f'Barricade: {self.barricade}')
		print(f'Garage: {self.garage}')
		print(f'Kills: {self.kills}')

	def win(self):
		print('Victory!')
		exit()

	def lost(self):
		print('You lost!')
		exit()

	def roll_lawn(self):
		pass

	def roll_barricade(self):
		pass

	def roll_garage(self):
		res = self.roll_dice()
		print(f'Garage dice: {res}')
		if res >= GARAGE_SUCCESS:
			self.add_garage(1)

	def roll(self):
		line = list(input('Distribute dices: ').upper())
		for i in range(line.count('L')):
			self.roll_lawn()
		for i in range(line.count('B')):
			self.roll_barricade()
		for i in range(line.count('G')):
			self.roll_garage()

	def add(self, *args):
		tp, dlt = args
		dlt = int(dlt)
		match tp:
			case 'lawn':
				self.add_lawn(dlt)
			case 'barricade':
				self.add_barricade(dlt)
			case 'garage':
				self.add_garage(dlt)
			case 'kills':
				self.add_kills(dlt)

	def __init__(self):
		self.reset()
		while True:
			command = [x.strip().lower() for x in input().split() if x.strip()]
			match command[0]:
				case 'exit':
					exit()
				case 'reset':
					self.reset()
				case 'info':
					self.info()
				case 'go':
					self.add_lawn(bisect_left(GARAGE_LEVELS, self.garage))
					self.roll()
					self.add_barricade(-self.lawn)
				case 'add':
					self.add(*command[1:])