#!/usr/bin/env python
# coding: utf-8

# # Daily Challenge_Week 1 Day 2
# 1.Using the input function, ask the user for a string. The string must be 10 characters long.
If it’s less than 10 characters, print a message which states “string not long enough”.
If it’s more than 10 characters, print a message which states “string too long”.
If it’s 10 characters, print a message which states “perfect string” and continue the exercise.
# In[1]:


user_input_chr=str(input("Enter a string: "))


# In[2]:


if len(user_input_chr) < 10:
    print("string not long enough")
elif len(user_input_chr) > 10:
    print("string too long")
else:
    print("perfect string")

#2.Then, print the first and last characters of the given text.
The user enters "HelloWorld"
Then you have to print 
H
d
# In[3]:


print("First Character:", user_input_chr[0])


# In[4]:


print("Last Character:", user_input_chr[-1])

#3. Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:

The user enters "HelloWorld"
Then, you have to construct the string character by character
H
He
Hel
... etc
HelloWorld
# In[6]:


constructed_string = ""
for char in user_input_chr:
    constructed_string += char
    print(constructed_string)

#4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:
Hlrolelwod
# In[12]:


char_list = list(user_input_chr)
print (char_list)


# In[22]:


import random
random.shuffle(char_list)


# In[23]:


print("newly_jumbled_string: ", char_list)


# In[ ]:




