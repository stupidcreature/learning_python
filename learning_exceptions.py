def exceptions():

    class MyException(Exception):
        def __init__(self, *args, **kwargs):
            Exception.__init__(self, *args, **kwargs)

    try:
        num1, num2 = input("Enter two numbers separated by SPACE: ").split(" ")

        div = int(num1) / int(num2)

        print("{} / {} = {}".format(num1, num2, div))

        # raise MyException

    except ZeroDivisionError as ex:
        print("Division by Zero occured")
        print(ex)

    except MyException as ex:
        # does not happen, because 'raise MyException' is commented out
        print("My Exception was raised")
        print(ex)

    except Exception as ex:
        print("An unknown exception occured")
        print(ex)

    else:
        print("Nice, everything worked out.")

    finally:
        print("This is always executed")


