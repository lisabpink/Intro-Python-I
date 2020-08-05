# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# The modulus operator, sometimes also called the remainder operator or integer remainder operator
# works on integers (and integer expressions) and yields the remainder when the first operand is divided by the second.
# In Python, the modulus operator is a percent sign ( % )
def is_even(x):
    if (num % 2) == 0:
        return True
    else:
        return False


# Read a number from the keyboard
# num = input("Enter a number: ")
num = int(input("Enter a number: "))

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
print('Even!' if is_even(num) == True else 'Odd!')
