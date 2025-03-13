#!/usr/bin/env python
# coding: utf-8

# # Mini Project 1

# In[1]:


def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}        1 | 2 | 3")
    print("--+---+--") 
    print(f"{board[3]} | {board[4]} | {board[5]}        4 | 5 | 6")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}        7 | 8 | 9")


# In[2]:


def player_input(player):
    while True:
        try:
            position = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if position in range(9):
                return position
            else:
                print("Invalid position. Please choose a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# In[3]:


def check_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # for horizontal win (rows)
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), # for a vertical win (columns)
                      (0, 4, 8), (2, 4, 6)]           # for a diagonal win
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != ' ':
            return True
    return False


# In[4]:


def play():
    board = [' ' for _ in range(9)]
    current_player = 'X'
    
    for _ in range(9):
        display_board(board)
        position = player_input(current_player)
        
        if board[position] == ' ':
            board[position] = current_player
            if check_win(board):
                display_board(board)
                print(f"Player {current_player} wins!")
                return
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Position is already taken. Try again.")
    
    display_board(board)
    print("It is a tie!")


# In[ ]:


play()



# In[ ]:




