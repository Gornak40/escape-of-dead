from os import system
from collections import defaultdict


BOT_NAME = 'random-bot.py'
NUMBER = 1000
result = defaultdict(int)
gamelen = 0

for i in range(NUMBER):
	system(f'python {BOT_NAME} > log.txt')
	with open('log.txt') as file:
		logs = list(map(str.strip, file.readlines()))
	result[logs[-1]] += 1
	gamelen += len(logs)
	print(i)

print(result)
print(gamelen / NUMBER)