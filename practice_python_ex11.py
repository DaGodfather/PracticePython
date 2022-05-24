# !python3

def get_integer():
    return int(input("Give me a number: "))

userGuess = get_integer()

isPrime = "This is not a prime number"

for i in range(2,userGuess):
    if userGuess % i == 0:
        isPrime = "%s is not a prime number" % (userGuess)
        break
    else:
        isPrime = "%s is a prime number" % (userGuess)
     

print(isPrime)
    