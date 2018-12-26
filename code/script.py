##Number Guessing Game
import random

guess=[]

#getting random number between 1 to 100
cpu_num = random.randint(1, 100)

#ask to user manual input
player_num=int(input("Enter a number 1 To 100 : "))

guess.append(player_num)


while player_num!=cpu_num:
	if player_num>cpu_num:
		print("Too high !!!")
	else:
		print("Too low !!!")
	player_num=int(input("Enter a number 1 To 100 : "))
	guess.append(player_num)
else:
	print("well done...")
	print("You have taken {} guesses".format(len(guess)))
	print("here are you guesses")
	print(guess)