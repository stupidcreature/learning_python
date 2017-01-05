# overwrite Widgets with the ttk styled ones
# (looks better, but is less documented and lacks some customization options)


# main function simply for calling all the demo functions (one for each topic)
# that way we can have everything in one file
from learning_tkinter import tkinter


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
    # functions_advanced()
    # iterators_list_comprehension_generators()
    # threads()
    # regular_expressions()
    tkinter()

    # # more comprehensive problems (smaller ones are embedded into the functions above
    # primes()
    # import problem_regex_filesearch
    # problem_regex_filesearch.text_analysis()

    # from not_checked_in import runme
    # runme()



    pass


if __name__ == "__main__":
    main()
