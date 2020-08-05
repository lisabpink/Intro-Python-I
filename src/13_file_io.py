"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
print('----FOO.txt -----')
foo = open('foo.txt', 'r')
print(foo.read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

#! %d is used as a placeholder for numeric or decimal values.
#! This line of code will substitute %s with Alice (str) and %d with 42.
#! The %d and %s string formatting "commands" are used to format strings.
# !The %d is for numbers, and %s is for strings.
#! A carriage return means moving the cursor to the beginning of the line. The code is \r .

# YOUR CODE HERE
bar = open("bar.txt", "w+")
for n in range(3):
    bar.write("Thing %d\r\n" % (n+1))
bar.close()

bar = open('bar.txt', 'r')
print('----BAR.txt -----')
print(bar.read())
bar.close()
