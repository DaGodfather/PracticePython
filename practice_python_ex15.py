#! python3
# Reverse word order fro Practice python ex 15

def ReverseString(userString):
    stringList = userString.split(" ")
    newList = []
    index = -1 
    for i in range(len(stringList)):
        newList.append(stringList[index])
        index = index - 1
    
    newString = " ".join(newList)

    return newString


userRes = input("Please enter a string?")


backwardString = ReverseString(userRes)

print(backwardString)