import math

print("Welcome to the AgeToPi program!")
print("")
age = (int)(input('How old are you? '))
ageInPi = int(age / math.pi)


print("You are " + (str)(ageInPi) +  " pi years old.")

nextPiBirthday = (math.ceil)(math.pi - (age % math.pi))

if (age < 4):
    nextPiBirthday = (4 - age)
     
nextPiBirthdayString = (str)(nextPiBirthday)

print("Your next pi birthday is in " + nextPiBirthdayString + " normal year(s)!")
