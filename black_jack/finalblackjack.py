from random import choice
from art import logo, goodbye
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def black_jack():
  dealing_continue = True
  print(logo)
  black_start = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")
  os.system('cls')

  if black_start == "y":
#INITIAL HAND 
    com_results = []
    player_results = []
    card1 = choice(cards[1::])
    card2 = choice(cards)
    global current_score
    current_score = card1 + card2
    com_card= choice(cards)
    com_results.append(com_card)
    player_results.append(current_score)

    print(f"""Your cards: {[card1, card2]}, current score: {current_score}
Dealer's first card: {com_card}
      """)  
    if current_score == 21:
      print("BlackJack!!!")
      black_jack()

  #DEALING STAGE
    while dealing_continue:
      black_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if black_deal == 'y':
        os.system('cls')
        #PLAYER DEAL
        dealt_card = choice(cards)
        print (f"You deal: {dealt_card}")
        current_score += dealt_card
        player_results.append(dealt_card)
        #COMPUTER DEAL
        print (f"Your score is: {current_score} and dealer's score is:  {com_card}")
        if current_score > 21:
          print("You lose!")
          dealing_continue = False
          black_jack()
        elif dealt_card == 11 and current_score > 21:
          dealt_card = 1 #MAKE IT so 11 changes to 1 if score is larger than 21
        elif current_score == 21:
          print("BLAAAAACKJACKKK!!!")
          dealing_continue = False
          black_jack()
      else: 
        #PASS 
        os.system('cls')
        print(f"Your hand is: {player_results}, your total score is: {current_score}")
        compu_deal = choice(cards)
        com_card += compu_deal
        com_results.append(compu_deal)
        dealing_continue = False


  #RESULTS STAGE     
        while com_card < 17:
          compu_deal = choice(cards)
          com_card += compu_deal
          com_results.append(compu_deal)
        if com_card > current_score and com_card < 22:
          print(f"\nDealer's hand is: {com_results}, dealer's total score is: {com_card}")
          print("\nYou lose!")
        elif com_card == current_score:
          print(f"\nDealer's hand is: {com_results}, dealer's total score is: {com_card}")
          print("\nIt's a draw!")
        elif current_score > com_card or com_card > 21:
          print(f"\nDealer's hand is: {com_results}, dealer's total score is: {com_card}")
          print("\nYou win!")
        black_jack()
  else: 
    print(goodbye)

black_jack()


