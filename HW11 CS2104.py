
def sumDigits(num, theSum):
    if (num < 0):
        num = num * -1
    
    if (num < 10):
        theSum = theSum + num
        print(theSum)
        return 0
    if (num % 10 == 0):
        sumDigits(num/10, theSum)

    if (num % 10 != 0):
        theSum = theSum + num % 10  # Adds the ones digit
        sumDigits(num - num % 10, theSum)

        

num = int(input("What number should I sum the digits of? "))
sumDigits(num, 0)
