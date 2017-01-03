# import is used to make specialty functions available
# These are called modules


# main function simply for calling all the demo functions (one for each topic)
# that way we can have everything in one file
from learning_functions_advanced import functions_advanced


def main():
    # # the basics
    # simple_data_types()
    # conditionals()
    # loops()
    # functions()
    # user_input()
    # file_io()
    # object_oriented_programming_basic()
    # object_oriented_programming_intermediate()
    # exceptions()
    functions_advanced()

    # # problems
    # primes()

    pass


if __name__ == "__main__":
    main()
