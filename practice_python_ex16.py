#! python 3
#Password Generator from Parctice Python ex 16

import random, sys

def main():
    charlist = "0123456789abcdefghijlkmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_/!$"
    #randomRange = random.randrange(8,16)

    proceed = input("Do you need a random password? Y or N\n")

    if proceed == "N" or proceed == "n":
        print("You said No, okay!")
        sys.exit()
    
    isTrue = True
    while(isTrue):
        password = ""
        for i in range(random.randrange(8, 16)):
            password = password + random.choice(charlist)
    
        print(password)

        proceed = input("Do you want another password? Y or N\n") 

        if proceed == "N" or proceed == "n":
            isTrue = False
            
    sys.exit()


if __name__ == "__main__":
    main()

