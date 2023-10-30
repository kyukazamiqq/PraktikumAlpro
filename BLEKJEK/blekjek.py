import random

def generate_card():
	return random.randint(2,11)

def play():
	print("BLEKJEEKKKKKK\n")

	player_card1 = generate_card()
	player_card2 = generate_card()
	sum_player = player_card1 + player_card2

	print(f"You get a {player_card1} and a {player_card2}")
	print(f"Your total is {sum_player}\n")

	dealer_card1 = generate_card()
	dealer_card2 = generate_card()
	sum_dealer = dealer_card1 + dealer_card2

	print(f"The dealer has a {dealer_card1}, and a hidden card.")
	print(f"His total is hidden too.\n")

	player_choose = input("Would you like to 'hit' or 'stay'? ")
	while (player_choose == 'hit'):
		player_card3 = generate_card()
		sum_player = sum_player + player_card3
		print(f"you drew a {player_card3}")
		print(f"Your total is {sum_player}")
		player_choose = input("Would you like to 'hit' or 'stay'? ")
		print()


	print("Okays dealers turns")
	print(f"His hidden card was {dealer_card2}\n")
	print(f"His total was {sum_dealer}\n")

	print(f"Dealer Choose to hit!\n")
	while (sum_dealer < 17):
		dealer_card3 = generate_card()
		sum_dealer = sum_dealer + dealer_card3
		print(f"He draws a {dealer_card3}")
		print(f"His total is {sum_dealer}\n")

	if sum_player > 21:
		print(f"Your total is {sum_player}, PLAYER BUST, DEALER WINS!")
	elif sum_dealer > 21:
		print(f"Dealer total is {sum_dealer} DEALER BUST, PLAYER WINS!")
	elif sum_player < sum_dealer:
		print(f"Dealer total is {sum_dealer}")
		print(f"Player total is {sum_player}")
		print(f"DEALER WINS!")
	elif sum_player > sum_dealer:
		print(f"Dealer total is {sum_dealer}")
		print(f"Player total is {sum_player}")
		print(f"Player WINS!")
	elif sum_player > 21 and sum_dealer > 21:
		print("DEALER AND PLAYER BUSTED")
	elif sum_player == sum_dealer:
		print(f"Player {sum_player} dealer has {sum_dealer} GAME TIE ")

play()

		

