# 🎨 Display art
from operator import is_
import random

from regex import B
from art import logo, vs
from data import data

# 📦 Format the account data into printable format 
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]

    return f"🌟 {account_name}, a {account_descr} from {account_country} 🌍"

# ✅ Check if the user's answer is correct
def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"      # 👍 if user guess is correct, return True
    else:
        return user_guess == "b"      # 👍 if user guess is correct, return True
    
print("🎮 Welcome to the Higher Lower Game! 🎮")
print(logo)

score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    # 🎲 Generate a random account from the game data 

    # 🔁 Making account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"🅰️  Compare A : {format_data(account_a)}")
    print(vs)
    print(f"🅱️  Against B : {format_data(account_b)}")

    # ❓ Ask user for a guess
    guess = input("🤔 Who has more followers? Type 'A' or 'B': ").lower()

    # 🧹 Clear the screen between rounds
    print("\n"*200)
    print(logo)

    # 🔍 Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # 🧠 Give user feedback on their guess
    if is_correct:
        score += 1
        # 🏆 Score keeping
        print(f"🎉 You are right! Current score: {score}")
    else:
        print(f"❌ Sorry, that's wrong. Final score: {score}")
        game_should_continue = False

# 🔄 Make the game repeatable