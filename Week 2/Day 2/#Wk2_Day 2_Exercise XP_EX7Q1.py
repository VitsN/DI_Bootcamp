#Exercise XP
#Week 2_Ex7_Q1

import random

def get_random_temp():
    return random.randint(-10, 40)

#Q1
random_temp = get_random_temp()
print(f"Generated temperature: {random_temp} °C")

