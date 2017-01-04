import re

def regular_expressions():
    teststring1 = "The ape was at the apex"
    testpattern1 = "ape\S*"

    if re.search(testpattern1, teststring1):
        print("Ape found!")

    allApes = re.findall(testpattern1, teststring1)
    print(allApes)

    for i in re.finditer(testpattern1, teststring1):
        print(i.span(), "->", teststring1[i.span()[0]:i.span()[1]])

    # one way to find and iterate over all words in a string
    for i in re.finditer("\w+", teststring1):
        print(i.span(), "->", teststring1[i.span()[0]:i.span()[1]])

    # create a pattern object
    regex = re.compile(testpattern1)
    print(regex.sub("REPLACED_MATCH", teststring1))


