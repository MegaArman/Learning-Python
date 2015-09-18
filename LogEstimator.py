# Arman Bahraini
# 10/3/2014
# Calculate log base 2 of a positive using only arithmetic operations. Output a range if the answer is not an integer (ex: 6-7 for log base-2 of 81)
# Note: There are more efficient solutions.

# This is for CS 2104 HW 5

y = float(input("Input a positive number: "))

def LogEstimate(y):
    
    x = 2
    counter = 0
    breakEven = False
     
    if (y > 1):
    
        while (x <= y):
            
            if (x == y):
                counter = counter + 1                
                print("The logarithm base-2 of " + str(y) + " is " + str(counter))
                breakEven = True
                
            x = x * 2
            counter = counter + 1
    
        if (breakEven is False):
                print("The logarithm base-2 of " + str(y) + " lies between " + str(counter) + " and " + str(counter + 1))
   
    if (y < 1 and y > 0):
        
        x = 1
        
        while (x >= y):

            if (x == y):
                
                print("The logarithm base-2 of " + str(y) + " is " + str(counter))
                breakEven = True
                
            x = x / 2
            counter = counter - 1
    
        if (breakEven is False):
            
                print("The logarithm base-2 of " + str(y) + " lies between " + str(counter + 1) + " and " + str(counter))
                
    if (y == 1):
        
        print("The logarithm base-2 of 1 is 0")
    
    if (y <= 0):
        
        print("Cannot compute the log of numbers less than or equal to 0!")


LogEstimate(y)
