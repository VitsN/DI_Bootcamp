#Exercise XP
#Week 2_Ex7_Q5 and Q6

import random

def get_random_temp(season):
    if season == 'winter':
        return round(random.uniform(-10, 16), 1)
    elif season == 'spring':
        return round(random.uniform(0, 23), 1)
    elif season == 'summer':
        return round(random.uniform(24, 40), 1)
    elif season == 'autumn' or season == 'fall':
        return round(random.uniform(10, 26), 1)
    else:
        print("Invalid season. Defaulting to 'spring'.")
        return round(random.randint(0, 23), 1)

def main():
    try:
        month = int(input("Enter the number of the month (1 = Januarry, 12 = December): "))
        if month in [6, 7, 8]:
            season = 'winter'
        elif month in [4, 5]:
            season = 'spring'
        elif month in [1, 2, 11, 12]:
            season = 'summer'
        elif month in [9, 10]:
            season = 'autumn'
        else:
            print("Invalid month. Defaulting to 'spring'.")
            season = 'spring'

        temperature = get_random_temp(season)

        print(f"The temperature right now is {temperature} degrees Celsius during {season.capitalize()}.")

        if temperature < 0:
            print("Brrr, that’s freezing! Wear some extra layers today.")
        elif temperature <= 16:
            print("Quite chilly! Don’t forget your coat.")
        elif temperature <= 23:
            print("The weather is pleasant. A light jacket should suffice!")
        elif temperature <= 32:
            print("Warm and sunny! Stay hydrated and enjoy your day.")
        else:
            print("It’s quite hot! Wear light clothing and stay cool.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the month (1-12).")

main()