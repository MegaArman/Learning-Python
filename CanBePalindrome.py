    # palindromes must be symmetrical, each char must be paired with another of the same, except in an odd array..must have 1 odd, ex : aba
    # doesn't matter where you start search
    # can do in O(n) - meaning 1 traversal or k * N traversals....
    # <= N+128 solution!!!!!!!!!!! N being the length of the word
    
def canBePalindrome(charArray):

    #can be reduced to just letters depending on spec
    count = [0] * 128 # creates an array of 128 zeros (to represent all ASCII keys), every time a certain char is found +1 it's value in the table
    # ex.. every time 'a' is found +1 the ASCII value for a in count (so count[97]+=1)
    # afterwards check if there is a permissible number of odds in count[] - DONE! 
    numOdd = 0 #count # of chars that appear odd #s of times
    
    if (len(charArray) == 1):
        return True
        
    for i in range(len(charArray)): # 0-length of array
        count[ord(charArray[i])] += 1 #ord converts chars to ints

    for j in range(len(count)): #searches the table for odds
         # if (count[ord(charArray[j])] % 2 != 0):  wrong.. otherwise same # can be counted twice
         if (count[j] %2 != 0):
            numOdd += 1 # reason not to check if numOdd is too large is because it doesn't make a difference overall? possible optimization or no???
            #print(numOdd)
            
    if (len(charArray)%2 == 0 and numOdd == 0): #evens can not have any odds
        return True
    if (len(charArray)%2 != 0 and numOdd == 1):  #every odd length word should have only 1 char who has an odd numbers of appearances..
        # parity property means we don't need to check # evens
        return True
   
    return False
#test cases-------------------------------

if (canBePalindrome(['a'])):
    print("yes!")
else:
    print("No =(")
    
if (canBePalindrome(['a', 'b', 'a'])): #odd
    print("yes!")
else:
    print("No =(")

if (canBePalindrome(['a', 'b', 'a', 'a', 'b'])): #baaab
    print("yes!")
else:
    print("No =(")

if (canBePalindrome(['a', 'b', 'a', 'b','a','b'])): # 3as, 3bs
    print("yes!")
else:
    print("No =(")
    
if (canBePalindrome(['a', 'b', 'c'])): 
    print("yes!")
else:
    print("No =(")
    
if (canBePalindrome(['a', 'b', 'c','a','b','c'])):  #even
    print("yes!")
else:
    print("No =(")
    
