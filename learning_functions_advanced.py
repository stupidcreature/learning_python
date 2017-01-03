import random
from functools import reduce


def functions_advanced():
    def get_function_times_num(num):
        def mult_by(value):
            return num * value

        return mult_by

    def execute_via_function_variable(fun, value):
        return fun(value)

    # define a function variable
    listOfFunctions = []
    for i in range(0, 11):
        listOfFunctions.append(get_function_times_num(i))

    print("2 * 8 using function variable: {}".format(execute_via_function_variable(listOfFunctions[2], 8)))
    print("10 * 8 using function variable: {}".format(execute_via_function_variable(listOfFunctions[10], 8)))

    def annotated_function(name: str, age: int, weight: float):
        print("{} is {} years old and weighs {} kg.".format(name, age, weight))

    annotated_function("Peter", 10, 50)
    print(annotated_function.__annotations__)

    sum = lambda var1, var2: var1 + var2
    print("Sum of 2 + 3 using a lambda function:", sum(2, 3))

    canvote = lambda age: True if age >= 18 else False

    # Lambdas in dictionaries
    attack = {'quick': (lambda: print("Quick Attack")),
              'power': (lambda: print("Power Attack")),
              'miss': (lambda: print("The Attack Missed"))}

    # keys() returns an iterable so we convert it into a list
    # choice() picks a random value from that list
    attackKey = random.choice(list(attack.keys()))
    attack[attackKey]()

    # Create a random list filled with the characters H and T
    flipList = []

    # Populate the list with 100 Hs and Ts
    # Trick : random.choice() returns a random value from the list
    for i in range(0, 100):
        flipList += random.choice(['H', 'T'])

    # Output results
    print("Heads : ", flipList.count('H'))
    print("Tails : ", flipList.count('T'))

    # Map allows us to execute a function on each item in a list
    oneTo10 = range(1, 11)

    # The function to pass into map
    def dbl_num(num):
        return num * 2

    # Pass in the function and the list to generate a new list
    print(list(map(dbl_num, oneTo10)))

    # You could do the same thing with a lambda
    print(list(map((lambda x: x * 2), oneTo10)))

    # You can perform calculations against multiple lists
    aList = list(map((lambda x, y: x + y), [1, 2, 3], [10, 20, 30]))
    print(aList)

    # Filter selects items from a list based on a function
    # Print out the even values from a list
    print(list(filter((lambda x: x % 2 == 0), range(1, 11))))

    # problem: get all numbers that are multiples of 9 from a random list of 100 values between 1 and 1000

    # generate the list of random numbers
    # randList = []
    # for i in range(0, 100):
    #     randList.append(random.randrange(1, 1001))

    # alternative method for generating the list in one line:
    randList = list(random.randint(1, 1001) for i in range(100))

    print(list(filter((lambda x: x % 9 == 0), randList)))

    # reduce
    list_of_values = [1, 2, 3, 4, 5]

    # use reduce to add values in that list
    print("The sum of all values in {} is {}".format(list_of_values, reduce((lambda x, y: x + y), list_of_values)))
