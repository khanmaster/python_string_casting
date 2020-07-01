#
# x = 12
# y = 11
#
# print(x == y) # checking the values as Boolean resulting True or False
# print(x != y) # checking the values as Boolean resulting True or False
#
# print(x > y)
#
# print(x < y)
#
# print(x <= y)
#
# print(x >= y)

# Let's check a real life example now to understand it better
#
# age = 18
#
# print(age < 19)

# print(3 % 9) # Modular gives the left over value of the equation

# double quotes VS single in python

# print(" hello World")

# print('hello world')

# the best practice and why
# using Double quotes is better -
# Why- let's see an example

# print('Ugne\'s class is eng 67 ') # single quotes


# print("Ugne's class is eng 67") # double quotes

# stings - indexing - casting - slicing - concatenation

#greeting_welcome = "Hell world"
# H E L L O W O R L D
# 0 1 2 3 4 5 6 7 8 9
#
#print(len(greeting_welcome))

# welcome_user = input("Please enter your name ")
# print(" Dear " + welcome_user + " welcome on board") # Concatenation



# Let's move onto STRING slicing

# hi = "hello world"

# print(hi[0])

# print(len(hi)) # finding out the length of the string
# print(hi[-1]) # last index of the string

# print(hi[0:6]) # slicing an index starting from 0 to 6 - will print hello
# print(hi[-6:-11]) # slicing an index starting from -6 to 11 - will print hello

# remove_white_space = "remove the space the end of a string                      "
# print(len(remove_white_space))
#
# print(len(remove_white_space.strip()))

# Boolean value within DATA types


#use_text = "here's SOME text with lot's of text"

# count() counts the substring within the string
# print(use_text.count("text"))
#
# # brings everything to lower case
# print(use_text.lower())
#
# # brings everything to upper case
# print(use_text.upper())
#
# # capitalise first letter of the sentence
# print(use_text.capitalize()) # used to interact with User a lot

use_text = "here's SOME text with lot's of text"
# replacing text in the string
print(use_text.replace("with", ","))

print(use_text.startswith("h"))








