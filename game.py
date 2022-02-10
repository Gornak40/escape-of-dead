from bisect import bisect_left


MAX_LAWN = 6
MAX_BARRICADE = 10
MAX_GARAGE = 10
MAX_KILLS = 10
GARAGE_LEVELS = [-1, 3, 6, 8, 10]


class Game:
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
		exit(0)

	def lost(self):
		print('You lost!')
		exit(0)

	def spawn(self):
		add = bisect_left(GARAGE_LEVELS, self.garage)
		add = min(MAX_LAWN, self.lawn + add) - self.lawn
		self.lawn += add

	def roll(self):
		pass

	def damage(self):
		self.barricade -= self.lawn
		if self.barricade <= 0:
			self.lost()

	def set(self, *args):
		match args[0]:
			case 'lawn':
				self.lawn = int(args[1])
			case 'barricade':
				self.barricade = int(args[1])
			case 'garage':
				self.garage = int(args[1])
			case 'kills':
				self.kills = int(args[1])

	def __init__(self):
		self.reset()
		while True:
			command = [x.strip().lower() for x in input().split() if x.strip()]
			match command[0]:
				case 'exit':
					exit(0)
				case 'reset':
					self.reset()
				case 'info':
					self.info()
				case 'go':
					self.spawn()
					self.roll()
					self.damage()
				case 'set':
					self.set(*command[1:])