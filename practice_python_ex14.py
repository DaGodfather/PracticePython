#! python3
# List Remove Duplicate from Practice Python ex 14

def RemoveDuplicate(mylist):
    newList = mylist
    newList = set(newList)
    newList = list(newList)
    return newList


testList = ["apple", "banana", "mango", "grape", "banana", "apple", "pear"]


noDuplist = RemoveDuplicate(testList)

print(noDuplist)