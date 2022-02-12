import sys
from subprocess import Popen, PIPE

with Popen([sys.executable, '-u', 'game.py'], stdin=PIPE, stdout=PIPE, universal_newlines=True, bufsize=1) as engine:
	while True:
		lawn, barricade, garage, kills, skip_spawn, result, tp = map(int, engine.stdout.readline().split())
		match tp:
			case 0:
				print('Victory!' if result == 1 else 'Lost!')
				exit(0)
			case 1:
				print(f'Lawn: {lawn}')
				print(f'Barricade: {barricade}')
				print(f'Garage: {garage}')
				print(f'Kills: {kills}')
				dices = input('Dices: ')
				print(dices, file=engine.stdin, flush=True)
			case 2:
				bonus = input('Bonus: ')
				print(bonus, file=engine.stdin, flush=True)
			case _:
				print(f'Result: {-tp}')
