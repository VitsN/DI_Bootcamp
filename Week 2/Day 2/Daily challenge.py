
matrix = [
    ['7', 'i', 'i'],
    ['T', 's', 'x'],
    ['h', '%', '?'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!']
]

decoded_message = ""

for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        char = matrix[row][col]
        if char.isalpha():
            decoded_message += char
        elif decoded_message and not decoded_message[-1].isspace():
            decoded_message += " "

decoded_message = decoded_message.strip()

print("Decoded Message:", decoded_message)
