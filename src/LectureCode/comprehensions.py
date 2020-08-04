# say we want to store all of the even numbers in the range
# 0-100 in a list 
# what are some ways we can do this? 

# evens_1 = []

# # loop through the range 
# for i in range(101):
#     # check if the current number is even
#     if i % 2 == 0:
#         # if it is, add it to the `evens` list 
#         evens_1.append(i)

# # print(evens)

# # comprehensions allow us to write the above logic in a much
# # more terse fashion 
# evens_2 = [i for i in range(101) if i % 2 == 0]
# # print(evens)

# print(evens_1 == evens_2)

# create a list of the square values of numbers in the range 1-10

# squares_1 = []

# for i in range(1, 11):
#     squares_1.append(i**2)

# # print(squares)

# squares_2 = [i**2 for i in range(1, 11)]

# print(squares_1 == squares_2)

names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn"]

# create a new list containing only the names that start with `s`
# and also make sure all of the names are properly capitalized 

s_names = [name.capitalize() for name in names if name[0].lower() == 's']

# for name in names:
#     # check if the name starts with `s`
#     if name[0].lower() == 's':
#         s_names.append(name.capitalize())
    # if it does, add it to `s_names`, making sure the 
    # name is properly capitalized 

# print(s_names)

# comprehensions work just as well with dicts as well 

# populate a dict with all letters of the alphabet with their corresponding 
# place in the alphabet 

letters = "abcdefghijklmnopqrstuvwxyz"

alpha = {letter: i + 1 for i, letter in enumerate(letters)}

# for i, letter in enumerate(letters):
#     alpha[letter] = i + 1

print(alpha)
