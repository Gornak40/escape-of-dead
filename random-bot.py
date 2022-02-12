from bot import Bot
from random import choice, randint


class Random_Bot(Bot):
	def get_dices(self):
		return ''.join(choice(['L', 'B', 'G']) for _ in range(4))

	def get_bonus(self):
		return randint(1, 4)


if __name__ == '__main__':
	Random_Bot()