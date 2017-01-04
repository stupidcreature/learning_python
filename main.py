# import is used to make specialty functions available
# These are called modules

import threading
import time
import random

# main function simply for calling all the demo functions (one for each topic)
# that way we can have everything in one file
from learning_list_comprehension_iterators_and_generators import iterators_list_comprehension_generators


def threads():
    def execute_thread(i):
        print("Thread {} sleeps at {}".format(i, time.strftime("%H:%M:%S", time.localtime())))
        rand_sleep_time = random.randint(1, 5)
        time.sleep(rand_sleep_time)
        print("Thread {} stops sleeping at {}".format(i, time.strftime("%H:%M:%S", time.localtime())))

    # starts 10 threads
    for i in range(10):
        thread = threading.Thread(target=execute_thread, args=(i+1,))
        thread.start()

    print("Active Threads:", threading.activeCount())
    print("Thread Objects:", threading.enumerate())




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
    threads()



    # # more comprehensive problems (smaller ones are embedded into the functions above
    # primes()


    pass


if __name__ == "__main__":
    main()
