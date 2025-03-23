#Wk1_Day 4_Exercise XP
#Exercise 9

total_cost = 0

print("Enter the age of each family member. Type 'done' when finished.")
while True:
    age = input("Age: ")
    if age.lower() == "done":
        break
    try:
        age = int(age)  # Convert the input to an integer
        if age < 3:
            total_cost += 0  # Free ticket
        elif 3 <= age <= 12:
            total_cost += 10
        else:
            total_cost += 15
    except ValueError:
        print("Please enter a valid number or 'done'.")

print(f"\nTotal cost of family tickets: ${total_cost}")




