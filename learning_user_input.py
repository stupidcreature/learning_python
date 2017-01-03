import sys


def user_input():
    # USER INPUT -------------
    print('What is your name?')

    # Stores everything typed up until ENTER
    name = sys.stdin.readline()

    print('Hello', name)

    # STRINGS -------------
    # A string is a series of characters surrounded by ' or "
    long_string = "I'll catch you if you fall - The Floor"

    # Retrieve the first 4 characters
    print(long_string[0:4])

    # Get the last 5 characters
    print(long_string[-5:])

    # Everything up to the last 5 characters
    print(long_string[:-5])

    # Concatenate part of a string to another
    print(long_string[:4] + " be there")

    # String formatting
    print("%c is my %s letter and my number %d number is %.5f" % ('X', 'favorite', 1, .14))

    # Capitalizes the first letter
    print(long_string.capitalize())

    # Returns the index of the start of the string
    # case sensitive
    print(long_string.find("Floor"))

    # Returns true if all characters are letters ' isn't a letter
    print(long_string.isalpha())

    # Returns true if all characters are numbers
    print(long_string.isalnum())

    # Returns the string length
    print(len(long_string))

    # Replace the first word with the second (Add a number to replace more)
    print(long_string.replace("Floor", "Ground"))

    # Remove white space from front and end
    print(long_string.strip())

    # Split a string into a list based on the delimiter you provide
    quote_list = long_string.split(" ")
    print(quote_list)