import math


def simple_data_types():
    # Hello world is just one line of code
    # print() outputs data to the screen
    print("Hello World")

    '''
    This is a multi-line comment
    '''

    # A variable is a place to store values
    # Its name is like a label for that value
    name = "Derek"
    print(name)

    # A variable name can contain letters, numbers, or _
    # but can't start with a number

    # There are 5 data types Numbers, Strings, List, Tuple, Dictionary
    # You can store any of them in the same variable

    name = 15
    print(name)

    # The arithmetic operators +, -, *, /, %, **, //
    # ** Exponential calculation
    # // Floor Division
    print("5 + 2 =", 5 + 2)
    print("5 - 2 =", 5 - 2)
    print("5 * 2 =", 5 * 2)
    print("5 / 2 =", 5 / 2)
    print("5 % 2 =", 5 % 2)
    print("5 ** 2 =", 5 ** 2)
    print("5 // 2 =", 5 // 2)

    # Order of Operation states * and / is performed before + and -

    print("1 + 2 - 3 * 2 =", 1 + 2 - 3 * 2)
    print("(1 + 2 - 3) * 2 =", (1 + 2 - 3) * 2)

    # A string is a string of characters surrounded by " or '
    # If you must use a " or ' between the same quote escape it with \
    quote = "\"Always remember your unique,"

    # A multi-line quote
    multi_line_quote = ''' just
    like everyone else" '''

    print(quote + multi_line_quote)

    # To embed a string in output use %s
    print("%s %s %s" % ('I like the quote', quote, multi_line_quote))

    # To keep from printing newlines use end=""
    print("I don't like ", end="")
    print("newlines")

    # You can print a string multiple times with *
    print('\n' * 5)

    # LISTS -------------
    # A list allows you to create a list of values and manipulate them
    # Each value has an index with the first one starting at 0

    grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
    print('The first item is', grocery_list[1])

    # You can change the value stored in a list box
    grocery_list[0] = "Green Juice"
    print(grocery_list)

    # You can get a subset of the list with [min:up to but not including max]

    print(grocery_list[1:3])

    # You can put any data type in a a list including a list
    other_events = ['Wash Car', 'Pick up Kids', 'Cash Check']
    to_do_list = [other_events, grocery_list]

    print(to_do_list)

    # Get the second item in the second list (Boxes inside of boxes)
    print(to_do_list[1][1])

    # You add values using append
    grocery_list.append('onions')
    print(to_do_list)

    # Insert item at given index
    grocery_list.insert(1, "Pickle")

    # Remove item from list
    grocery_list.remove("Pickle")

    # Sorts items in list
    grocery_list.sort()

    # Reverse sort items in list
    grocery_list.reverse()

    # del deletes an item at specified index
    del grocery_list[4]
    print(to_do_list)

    # We can combine lists with a +
    to_do_list = other_events + grocery_list
    print(to_do_list)

    # Get length of list
    print(len(to_do_list))

    # Get the max item in list
    print(max(to_do_list))

    # Get the minimum item in list
    print(min(to_do_list))

    # TUPLES -------------
    # Values in a tuple can't change like lists

    pi_tuple = (3, 1, 4, 1, 5, 9)

    # Convert tuple into a list
    new_tuple = list(pi_tuple)

    # Convert a list into a tuple
    # new_list = tuple(grocery_list)

    # tuples also have len(tuple), min(tuple) and max(tuple)

    # DICTIONARY or MAP -------------
    # Made up of values with a unique key for each value
    # Similar to lists, but you can't join dicts with a +

    super_villains = {'Fiddler': 'Isaac Bowin',
                      'Captain Cold': 'Leonard Snart',
                      'Weather Wizard': 'Mark Mardon',
                      'Mirror Master': 'Sam Scudder',
                      'Pied Piper': 'Thomas Peterson'}

    print(super_villains['Captain Cold'])

    # Delete an entry
    del super_villains['Fiddler']
    print(super_villains)

    # Replace a value
    super_villains['Pied Piper'] = 'Hartley Rathaway'

    # Print the number of items in the dictionary
    print(len(super_villains))

    # Get the value for the passed key
    print(super_villains.get("Pied Piper"))
    print(super_villains.get("Villain NotInList", "default value if Villain is not in list"))

    # Get a list of dictionary keys
    print(super_villains.keys())

    # Get a list of dictionary values
    print(super_villains.values())

    # extract key/value pairs
    for villain_k, villain_v in super_villains.items():
        print(villain_k, villain_v)

    # extract key/value pairs (the same as above)
    for villain in super_villains.items():
        print(villain[0], villain[1])

    list_of_numbers = range(1, 11)
    list_of_lists_of_powers = [[math.pow(num, 2), math.pow(num, 3), math.pow(num, 4)]
                               for num in list_of_numbers]

    num = 1
    for plist in list_of_lists_of_powers:
        print("{} : {}".format(num, plist))
        num += 1