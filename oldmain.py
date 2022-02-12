from game import Game


if __name__ == '__main__':
	G = Game()
	while True:
		command = [x.strip().lower() for x in input().split() if x.strip()]
		match command[0]:
			case 'exit':
				exit()
			case 'reset':
				G.reset()
			case 'info':
				G.info()
			case 'go':
				G.go()
			case 'add':
				tp, dlt = command[1:]
				dlt = int(dlt)
				match tp:
					case 'lawn':
						G.add_lawn(dlt)
					case 'barricade':
						G.add_barricade(dlt)
					case 'garage':
						G.add_garage(dlt)
					case 'kills':
						G.add_kills(dlt)
