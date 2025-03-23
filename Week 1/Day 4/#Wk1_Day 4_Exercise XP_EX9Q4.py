#Wk1_Day 4_Exercise XP
#Exercise 9 (question 4)

teenagers = ["Alice", "Grace", "Elsa", "Diana", "Anna"]

allowed_teenagers = []

for name in teenagers:
    age = input(f"{name}, how old are you? ")
    try:
        age = int(age)  
        if age < 16:
            print(f"Sorry, {name}, you are too young to watch this movie.")
        elif 16 <= age <= 21:
            print(f"Sorry, {name}, you are not permitted to watch this movie.")
        else:
            allowed_teenagers.append(name)  
    except ValueError:
        print(f"Invalid input for {name}. Please enter a valid number.")

print("\nFinal list of teenagers allowed to watch the movie:")
print(", ".join(allowed_teenagers))
print("You can now proceed with payment!", allowed_teenagers)





