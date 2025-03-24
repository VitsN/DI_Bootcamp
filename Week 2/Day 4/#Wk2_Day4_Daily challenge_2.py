#Wk2_Day4_Daily challenge
#Challenge 2

def find_longest_word(sentence):
    words = sentence.split()
    longest_word = ""
    max_length = 0
        
    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    
    return longest_word

sentence = "Forgetfulness is by all means powerless!"
longest = find_longest_word(sentence)
print("The longest word is:", longest)

