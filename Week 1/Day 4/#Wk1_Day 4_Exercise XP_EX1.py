#Wk1_Day 4_Exercise XP
#Exercise 1
my_fav_numbers={2, 4, 6, 8}
my_fav_numbers.add(1)
my_fav_numbers.add(3)
my_fav_numbers.remove(max(my_fav_numbers))

print(my_fav_numbers)

friend_fav_numbers={5, 10, 15, 20}
our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)

print(friend_fav_numbers)
print(our_fav_numbers)