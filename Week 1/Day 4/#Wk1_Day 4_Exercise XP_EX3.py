#Wk1_Day 4_Exercise XP
#Exercise 3
basket=["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)

basket.remove("Blueberries")
print(basket)

basket.append("Kiwi")
print(basket)

basket.append("Apples")
print(basket)

count_apple=basket.count("Apples")
print(f"No. of apples in the basket: {count_apple}")

basket.clear()

print(basket)