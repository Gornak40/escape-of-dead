import sys
from subprocess import Popen, PIPE


FULL_LOG = 0


class Bot:
	def get_dices(self):
		return input('Dices: ')

	def get_bonus(self):
		return input('Bonus: ')

	def update(self, lawn, barricade, garage, kills, skip_spawn, result, tp):
		if tp != 1:
			return
		print(f'L[{lawn}] B[{barricade}] G[{garage}] K[{kills}]')
		return

	def __init__(self):
		with Popen([sys.executable, '-u', 'game.py'], stdin=PIPE, stdout=PIPE, universal_newlines=True, bufsize=1) as engine:
			while True:
				lawn, barricade, garage, kills, skip_spawn, result, tp = map(int, engine.stdout.readline().split())
				self.update(lawn, barricade, garage, kills, skip_spawn, result, tp)
				match tp:
					case 0:
						print('Victory!' if result == 1 else 'Defeat!')
						exit(0)
					case 1:
						dices = self.get_dices()
						if not FULL_LOG:
							print(f'Dices: {dices}')
						print(dices, file=engine.stdin, flush=True)
					case 2:
						bonus = self.get_bonus()
						print(f'Bonus: {bonus}')
						print(bonus, file=engine.stdin, flush=True)
					case _:
						if FULL_LOG:
							print(f'Result: {-tp}')


if __name__ == '__main__':
	Bot()