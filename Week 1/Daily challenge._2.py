#Daily Challenge 2
user_input = input("Enter a word: ")

result = ""

for i in range(len(user_input)):
    if i == 0 or user_input[i] != user_input[i - 1]:
        result += user_input[i]

print("Final word:", result)
