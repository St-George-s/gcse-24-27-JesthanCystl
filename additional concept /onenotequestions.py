userString = input("Enter a sentence: ")
print(userString[0])
print(userString[-1])

userString = input("Enter a sentence: ")
reversedString = ""
for character in userString:
     reversedString = character + reversedString
print(reversedString)

import random
myRandom = random.randint(1,6)
print(myRandom)

import random
myFirstDice = random.randint(1,6)
mySecondDice = random.randint(1,6)
print(str(myFirstDice) + " + " + str(mySecondDice) + "=")
print(str(myFirstDice + mySecondDice))