import os
import random
from options import word_list
from asci_art import logo, stages


print(logo)

chosen_word = random.choice(word_list)
display = ["_"] * len(chosen_word)
lives = 6
stage_num = len(stages) - 1
letters_used = []

while "_" in display:
    guess = input("Please enter a letter: ")

    os.system('cls') #IMPORTANT for clearing the screen each time

    if guess in display:
        print(f"You already tried {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in display:
        print(f"The letter {guess} is not in the word!")
        lives -= 1
        stage_num -= 1
        guess
    if lives == 0:
        print("You lose!")
        print(stages[0])
        break
    elif lives > 0 and "_" not in display:
        print("You win!")
    print(display)
    print(stages[stage_num])


#########################################################
# end_of_game = False
# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# #TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
# #Set 'lives' to equal 6.
# lives = 6

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"

# while not end_of_game:
#     guess = input("Guess a letter: ").lower()

#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter

#     #TODO-2: - If guess is not a letter in the chosen_word,
#     #Then reduce 'lives' by 1. 
#     #If lives goes down to 0 then the game should stop and it should print "You lose."
#     if guess not in chosen_word:
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")

#     #Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")

#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")

#     #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
#     print(stages[lives])