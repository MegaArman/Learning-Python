

import math

##a = 10.5
##b = 10
##c = int(a/b) #type casting works for rounding!
##
##print(c)
#-----------------SWITCH IN PYTHON---------------
##
##num = int(input("Enter a value for x :"))
##
##x = {
##    1: "Sunday",
##    2: "Monday",
##    3: "Tuesday",
##    4: "Wednesday",
##    5: "Thursday",
##    6: "Friday",
##    7: "Saturday"
##    }
##
##print(x[num])
##
#10/8/14
##my_range = range(1, 6) # Note in Python, number of iterations = end - beginning
### so 6 - 1 = 5 in this case
##for i in my_range:
##    print("what ? ")

##number = int(input("Input some odd number:"))
##my_range = range(number - 1, -2, -2)
##numSpaces = number // 2 #integer division
##topSpaces = 0
##
##if (number % 2 == 1):
##print("Hill:")
##for i in my_range:
##   print ((number - i)*"*")
##
##if (number % 2 == 1):
##print("Triangle: ")
##for i in my_range:
##   print (numSpaces * " " + (number - i)*"*")
##   numSpaces = numSpaces - 1
##   
##if (number % 2 == 1):
##print("Hour Glass:")
##for i in my_range:
##   print (topSpaces * " " + (i + 1)*"*")
##   topSpaces = topSpaces + 1
##
##numSpaces = number//2
##
##if (number % 2 == 1):
##for i in my_range:
##   print (numSpaces * " " + (number - i)*"*")
##   numSpaces = numSpaces - 1


input_file = input("What file do you want to open? ")
date_file = open(input_file, 'r') # Read only
for line_str in data_file:
    print(line_str)
##
##results = ["1", "2", "3"]
results = [int(
    i) for i in results]
##print(results)
print("fun","poop")
print("poop")
