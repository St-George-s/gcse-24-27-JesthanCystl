totalHeight = 0
counter = 0
for i in range(6):
    height = input("height?")
    totalHeight = totalHeight + int(height)
    counter = counter + 1 
print("Average is : ", totalHeight/counter)


counta = 0
while counta < 3:
    word = input("input a word: ")
    counta = 0 

    for letter in 