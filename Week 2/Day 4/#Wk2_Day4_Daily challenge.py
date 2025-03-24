#Wk2_Day4_Daily challenge
#Challenge 1

input_words = input("Enter words followed by commas: ")

sort_words = ','.join([word for word in sorted(input_words.split(','))])

print(sort_words)
