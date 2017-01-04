import random
import threading
import time


def threads():
    def execute_thread(i):
        print("Thread {} sleeps at {}".format(i, time.strftime("%H:%M:%S", time.localtime())))
        rand_sleep_time = random.randint(1, 5)
        time.sleep(rand_sleep_time)
        print("Thread {} stops sleeping at {}".format(i, time.strftime("%H:%M:%S", time.localtime())))

    # starts 10 threads
    all_threads = []
    for i in range(10):
        thread = threading.Thread(target=execute_thread, args=(i + 1,))
        all_threads.append(thread)
        thread.start()

    print("Active Threads:", threading.activeCount())
    print("Thread Objects:", threading.enumerate())

    # one way to wait for all threads to end is this fancy one
    # better and easier would be to use call .join() on each thread
    while any(list(map((lambda x: x.isAlive()), all_threads))):
        time.sleep(1)

    # using a custom thread object
    class CustomThread(threading.Thread):
        def __init__(self, name):
            threading.Thread.__init__(self)
            self.__name = name

        @property
        def name(self):
            return self.__name

        def run(self):
            getTime(self.name)
            print("Thread:", self.name, "-> execution ends.")

    def getTime(name):
        print("Thread {} reporting for duty at: {}".format(name, time.strftime("%H:%H:%M", time.localtime())))
        time.sleep(3)
        print("Thread {} ends execution at: {}".format(name, time.strftime("%H:%H:%M", time.localtime())))


    thread1 = CustomThread("My Thread 1")
    thread1.start()

    thread1.join()