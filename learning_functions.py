def functions():
    # FUNCTIONS -------------
    # Functions allow you to reuse and write readable code
    # Type def (define), function name and parameters it receives
    # return is used to return something to the caller of the function
    def addNumbers(fNum, sNum):
        sumNum = fNum + sNum
        return sumNum

    print(addNumbers(1, 4))

    # Can't get the value of rNum because it was created in a function
    # It is said to be out of scope
    # print(sumNum)

    # If you define a variable outside of the function it works every place
    newNum = 0

    def subNumbers(fNum, sNum):
        newNum = fNum - sNum
        return newNum

    print(subNumbers(1, 4))

    def sumManyNumbers(*numbers):
        sum = 0
        for num in numbers:
            sum += num
        return sum

    print("1+2+3+4+5 =", sumManyNumbers(1, 2, 3, 4, 5))