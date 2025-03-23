#Wk1_Day 4_Exercise XP
#Exercise 4
#A float is a number that has a decimal point; E.g: 1.5. Whereas, an integer is a whole number with no decimal point, e.g: 5, -1

list= [x / 2 for x in range(3, 11)]
print(list)

format_list = [int(x) if x.is_integer() else x for x in list]

print(format_list)

#another way is to use numpy