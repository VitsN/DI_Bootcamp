#Exercise XP
#Week 2_Ex7_Q2 and Q3

import random
def get_random_temp():
    return random.randint(-10, 40)

def main():
    temperature = get_random_temp()
    print(f"The temperature right now is {temperature} degrees Celsius.")

    if temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temperature <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 17 <= temperature <= 23:
        print("The weather is pleasant. A light jacket should suffice!")
    elif 24 <= temperature <= 32:
        print("Warm and sunny! Stay hydrated and enjoy your day.")
    elif 33 <= temperature <= 40:
        print("It’s quite hot! Wear light clothing and stay cool.")

main()


