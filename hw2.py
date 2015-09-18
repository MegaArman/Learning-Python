
#Arman Bahraini
#9/18/14
#hw2 Python CS 1064 (SELF TEACHING)
#Is this twitter or something? Hashtags??

import math

p_float = float(input("Please enter the principal amount: ")) #principal
t_int = int(input("Enter the number of years: ")) #time in years
r_int = int(input("Enter the interest rate percentage as an integer "))
balance = p_float*math.pow(math.e, (r_int / 100) * t_int)
print("The final balance is ", balance)

