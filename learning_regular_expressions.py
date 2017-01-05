import re

# nice to know: (?m) -> sets the matching to multiline -> allows to use ^ on a multiline string
#               (?: at at the beginning of a () group makes it non-capturing
# see: https://www.youtube.com/watch?v=OQiKC9TTxDM
# and: https://www.youtube.com/watch?v=33EyyXf8904 (named groups at: 8:00)
#               (?=  at at the beginning of a () group makes it a look-ahead
#               (?<= at at the beginning of a () group makes it a look-behind
#               (?!  at at the beginning of a () group makes it a NEGATIVE look-ahead
#               (?<! at at the beginning of a () group makes it a NEGATIVE look-behind
#               (?P<name> at at the beginning of a group starts a named group


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


