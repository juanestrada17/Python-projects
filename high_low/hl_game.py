from random import choice
from art import logo, vs
from game_data import data
import os

person1 = choice(data)
person2 = choice(data)

def game_on():
    total_score = 0
    game_continue = True 

    while game_continue:
        
        person1 = choice(data)
        person2 = choice(data)
        
        print(logo)
        print(f"Your current score is: {total_score}")
        print (f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}")
        print (vs)
        print (f"Against B: {person2['name']}, a {person2['description']}, from {person2['country']}")
        choices = input("Who has more followers? Enter A or B: ").lower()

        if choices == 'a' and person1['follower_count'] > person2['follower_count']:
            total_score += 1
            print (f"That's right! that person has {person1['follower_count']} followers\n\n")
            print(f"Your total score is {total_score}")     
            os.system('cls')                   
        elif choices == 'b' and person1['follower_count'] < person2['follower_count']:
            total_score += 1
            print(f"That's right! that person has {person2['follower_count']} followers\n\n")
            print(f"Your total score is {total_score}")
            os.system('cls')                    
        else:
            os.system('cls')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {total_score}")
            game_continue = False

game_on()