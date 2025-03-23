#Wk1_Day 4_Exercise XP
#Exercise 7

favorite_fruits = input("Enter your favorite fruits (separate with single space): ")

formatted_fruits = " ".join(favorite_fruits.split())

favorite_fruits_list = formatted_fruits.split()

fruit_check = input("Enter the name of any fruit: ")

if fruit_check in favorite_fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy.")
