number_of_sticks = 21

print ("Давай поиграем в игру")

while number_of_sticks > 0:
	print (30 * "-")
	print ("Палочек на столе:", number_of_sticks)
	turn = input ("Ваш ход, сколько возьмёте? ")
	if turn.isdigit():
		turn = int(turn)
		if 0 < turn < 4:
			if turn <= number_of_sticks:
				if number_of_sticks > 4:
					number_of_sticks -= turn
					my_turn = 4 - turn
					print ("Я возьму:", my_turn)
					number_of_sticks -= my_turn
				else:
					number_of_sticks -= turn
					print ("Палочек на столе:", number_of_sticks)
					print ("Вы проиграли.")
			else:
				print ("Осталось только:", number_of_sticks)
		else:
			print ("Можно брать 1, 2 или 3 палочки!")
		
	else:
		print ("Нужно ввести цифру!")