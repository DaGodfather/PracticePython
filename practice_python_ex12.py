#! python3

def MakeCustomList(insertList):
    newlist = []
    newlist.append(insertList[0])
    newlist.append(insertList[-1])
    return newlist


a = [5, 10, 15, 20, 25]

mylist = MakeCustomList(a)

print(mylist)