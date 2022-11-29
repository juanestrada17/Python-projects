import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def black_jack():
  dealing_continue = True
  black_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  os.system('cls')

  if black_start == "y":
#INITIAL HAND 
    card1 = random.choice(cards[1::])
    card2 = random.choice(cards)
    global current_score
    current_score = card1 + card2
    com_card= random.choice(cards)

    print(f"""Your cards: {[card1, card2]}, current score: {current_score}
Computer's first card: {com_card}
      """)  
    if current_score == 21:
      print("BlackJack!!!")

  #DEALING STAGE
    while dealing_continue:
      black_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if black_deal == 'y':
        #PLAYER DEAL
        dealt_card = random.choice(cards)
        print (f"You deal: {dealt_card}")
        current_score += dealt_card
        #COMPUTER DEAL
        print (f"Your score is: {current_score} and computer's score is:  {com_card}")
        if current_score > 21:
          print("You lose!")
          dealing_continue = False
          black_jack()
        elif current_score == 21:
          print("BlackJack!!!")
          dealing_continue = False
          black_jack()
      else: 
        #PASS 
        print(f"Your score is: {current_score}")
        print(f"Computer's score is : {com_card}")
        compu_deal = random.choice(cards)
        print (f"Computer deals: {compu_deal}")
        com_card += compu_deal
        dealing_continue = False


  #RESULTS STAGE     
        while com_card < 17:
          compu_deal = random.choice(cards)
          print (f"Computer deals: {compu_deal}")
          com_card += compu_deal
          print(f"Computers total score is: {com_card}")
        if com_card > current_score and com_card < 22:
          print("You lose!")
        elif com_card == current_score:
          print("It's a draw!")
        elif current_score > com_card or com_card > 21:
          print("You win!")

        black_jack()
  else: 
    print("GoodBye!")

black_jack()






 