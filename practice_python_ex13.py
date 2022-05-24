#! python3
# Fibonnaci from Practice Python ex 13

def FibonnaciList(num):
    fibList = [1]
    sum = 0 
    for i in range(num):
        try:
            sum = fibList[-2] + sum
        except:
            sum = 1
        fibList.append(sum)
    return fibList[0:-1]



userRes = int(input("How many Fibonnaci numbers to do you want? "))


result = FibonnaciList(userRes)

for item in result:
    print(str(item) + " ")