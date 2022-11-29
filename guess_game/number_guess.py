from random import randint 

print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 50.""")

def random_num ():
  return randint(1,51)

num_to_guess = random_num()

def game_modes():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ").lower() 
  if difficulty == 'easy':
    attempts = 10
    print (f"You have {attempts} attempts remaining to guess the number. ")
    return attempts
  elif difficulty == 'hard':
    attempts = 5  
    print (f"You have {attempts} attempts remaining to guess the number. ")
    return attempts
  else:
    print("that's not a valid difficulty")
    return game_modes() #MAKE it so that player has to enter an specific option

attempts = game_modes() #TAKING A VARIABLE FROM A function to use it in another function

def game(attempts):
  game_continue = True
  guess = int(input("Make a guess: "))
  while game_continue:
    if attempts == 1:
      print ("GAME OVER!")
      game_continue = False
    elif guess not in range (1,51):
      print("You must type a number between 1 and 50")
      return game(attempts) #MAKE it so that player has to enter an specific option
    elif guess > num_to_guess:
      attempts -= 1
      print(f"You have {attempts} attempts remaining to guess the number.")
      print("Too high!")
      guess = int(input("Make a guess: "))
    elif guess < num_to_guess:
      attempts -= 1 
      print(f"You have {attempts} attempts remaining to guess the number.")
      print("Too low!")
      guess = int(input("Make a guess: "))
    else: 
      print(f"You guessed the correct number, which is {num_to_guess}")
      game_continue = False

game(attempts)
