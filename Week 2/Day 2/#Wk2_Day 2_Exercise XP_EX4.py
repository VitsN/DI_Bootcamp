#Exercise XP
#Week 2_Ex4

import random

def compare_numbers():
    try:
        user_number = int(input("Please enter a number between 1 and 100: "))
        
        if not (1 <= user_number <= 100):
            print("Please provide a number between 1 and 100.")
            return

        random_number = random.randint(1, 100)

        if user_number == random_number:
            print(f"Success! Both numbers are {user_number}.")
        else:
            print(f"Fail! Your number: {user_number}, Random number: {random_number}.")

    except ValueError:
        print("Invalid input. Please enter a valid number between 1 and 100.")

compare_numbers()
