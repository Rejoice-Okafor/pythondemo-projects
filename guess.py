logo = """"

   __ ___      __          
  / // (_)__ _/ /  ___ ____
 / _  / / _ `/ _ \/ -_) __/
/_//_/_/\_, /_//_/\__/_/   
  / /__/___/ _____ ____    
 / / _ \ |/|/ / -_) __/    
/_/\___/__,__/\__/_/       
"""

verse= """

 ▄               ▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░▌             ▐░▌▐░░░░░░░░░░░▌
 ▐░▌           ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀ 
  ▐░▌         ▐░▌  ▐░▌          
   ▐░▌       ▐░▌   ▐░█▄▄▄▄▄▄▄▄▄ 
    ▐░▌     ▐░▌    ▐░░░░░░░░░░░▌
     ▐░▌   ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌
      ▐░▌ ▐░▌                ▐░▌
       ▐░▐░▌        ▄▄▄▄▄▄▄▄▄█░▌
        ▐░▌        ▐░░░░░░░░░░░▌
         ▀          ▀▀▀▀▀▀▀▀▀▀▀ 

"""
import random

from replit import clear

def get_account_description(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}"

def compare_followers(guess, followers_a, followers_b):
    if followers_a > followers_b:
        return guess == "a"
    else:
        return guess == "b"

def main_game():
    score = 0
    continue_playing = True

    while continue_playing:
        account_a = random.choice(data)
        account_b = random.choice(data)

        while account_a == account_b:
            account_b = random.choice(data)

        print(logo)

        description_a = get_account_description(account_a)
        description_b = get_account_description(account_b)

        print(f"Compare A: {description_a}")
        print(verse)
        print(f"Against B: {description_b}")

        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        followers_a = account_a["follower_count"]
        followers_b = account_b["follower_count"]

        result = compare_followers(user_guess, followers_a, followers_b)
        clear()

        if result:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")

        play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
        if play_again != "yes":
            continue_playing = False

main_game()
