"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""
#!String objects have one unique built-in operation: the % operator (modulo).
#! This is also known as the string formatting or interpolation operator.
#! Given format % values (where format is a string), % conversion specifications in format are replaced with zero or more elements of values.
#! The effect is similar to using the sprintf() in the C language.

#!If format requires a single argument, values may be a single non-tuple object. 5 Otherwise, values must be a tuple with exactly the number of items specified by the format string, or a single mapping object (for example, a dictionary).
x = 10
y = 2.24552
z = "I like turtles!"

# Using the print operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print('x is', x, ',y is', '%.2f' % y, ',z is', '"'+z+'"')

# Use the 'format' string method to print the same thing
print('x is', x, ',y is', "{0:.2f}".format(y), ',z is', '"'+z+'"')

# Finally, print the same thing using an f-string
print('x is {} ,y is {} ,z is "{}"'.format(x, "{0:.2f}".format(y), z))
