#Wk1_Day 4_Exercise XP
#Exercise 8

toppings = []

base_price = 10
topping_price = 2.5

while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    else:
        toppings.append(topping)
        print(f"Adding {topping} to your pizza!")

total_price = base_price + len(toppings) * topping_price

print("\nYour pizza includes the following toppings:")
print(", ".join(toppings))
print(f"Total price: Rs{total_price:.2f}")

