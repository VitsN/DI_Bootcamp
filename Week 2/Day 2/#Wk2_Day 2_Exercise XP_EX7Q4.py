#Exercise XP
#Week 2_Ex7_Q4

import random

def get_random_temp(season):

    if season == 'winter':
        return random.randint(-10, 16)
    elif season == 'spring':
        return random.randint(0, 23)
    elif season == 'summer':
        return random.randint(24, 40)
    elif season == 'autumn' or season == 'fall':
        return random.randint(10, 26)
    else:
        print("Invalid season. Defaulting to 'spring'.")
        return random.randint(0, 23)

def main():
    season = input("Enter a season (winter, spring, summer, autumn/fall): ").strip().lower()

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

main()
