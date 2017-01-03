import os


def file_io():
    # FILE I/O -------------

    # Overwrite or create a file for writing
    test_file = open("test.txt", mode="wb")

    # print if the file is closed (should be False, because we just opened it)
    print(test_file.closed)

    # Get the file mode used
    print(test_file.mode)

    # Get the files name
    print(test_file.name)

    # Write text to a file with a newline
    test_file.write(bytes("Write me to the file\n", 'UTF-8'))

    # Close the file
    test_file.close()

    # Opens a file for reading and writing
    test_file = open("test.txt", "r+")

    # Read text from the file
    text_in_file = test_file.read()

    print(text_in_file)

    # Close the file (otherwise it cannot be deleted)
    test_file.close()

    # Delete the file
    os.remove("test.txt")

    # create, change, print and remove directories
    directory_name = "testdirectory"
    os.mkdir(directory_name)
    os.chdir(directory_name)
    print("Current directory:", os.getcwd())
    os.chdir("..")
    os.rmdir(directory_name)