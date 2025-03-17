#Challenge 1
Input_user_number=int(input("Enter a number:"))
Input_user_length=int(input("Enter a length:"))

list_multiples = []  

for i in range(1, Input_user_length + 1):
    list_multiples.append(Input_user_number * i)

print(list_multiples)
