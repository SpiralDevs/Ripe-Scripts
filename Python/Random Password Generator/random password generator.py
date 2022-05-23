#Random Password Generator - by Spiral
#importing modules
import random
import string
#welcome text
print("Hello User, Welcome to Password Generator!\nType help for help\nType generate to generate a password without having to exclude anything\nType exclude to exclude a certain type from password.\nAvailable Items To Be Excluded:\nlowercase\nuppercase\nnumbers\nsymbols")

while True:
    option = input("Enter Option")
    if option in ("help", "generate", "exclude"):
        if option == "help":
            print("Type help to bring this text up again\nType generate to generate a password without having to exclude anything\nType exclude to exclude a certain type from password.\nAvailable Items To Be Excluded:\nlowercase\nuppercase\nnumbers\nsymbols")
        elif option == "generate":
            #password length
            passLength = int(input("Enter Password Length: "))
            #data
            lowercase = string.ascii_lowercase
            uppercase = string.ascii_uppercase
            number = string.digits
            symbol = string.punctuation
            #combine data
            data = lowercase + uppercase + number + symbol
            #generate password
            structure = random.sample(data,passLength)
            password = "".join(structure) 
            print(password)
        elif option == "exclude":
            print("Available Items To Be Excluded:\nlowercase\nuppercase\nnumbers\nsymbols")
            choice = input("Enter What You Want To Be Excluded: ")
            if choice in ("lowercase", "uppercase", "numbers", "symbols"):
                if choice == "lowercase":
                    #password length
                    passLength = int(input("Enter Password Length: "))
                    #data
                    uppercase = string.ascii_uppercase
                    number = string.digits
                    symbol = string.punctuation
                    #combine data
                    data = uppercase + number + symbol
                    #generate password
                    structure = random.sample(data,passLength)
                    password = "".join(structure) 
                    print(password)
                elif choice == "uppercase":
                    #password length
                    passLength = int(input("Enter Password Length: "))
                    #data
                    lowercase = string.ascii_lowercase
                    number = string.digits
                    symbol = string.punctuation
                    #combine data
                    data = lowercase + number + symbol
                    #generate password
                    structure = random.sample(data,passLength)
                    password = "".join(structure) 
                    print(password)
                elif choice == "numbers":
                    #password length
                    passLength = int(input("Enter Password Length: "))
                    #data
                    lowercase = string.ascii_lowercase
                    uppercase = string.ascii_uppercase
                    symbol = string.punctuation
                    #combine data
                    data = lowercase + uppercase + symbol
                    #generate password
                    structure = random.sample(data,passLength)
                    password = "".join(structure) 
                    print(password)
                elif choice == "symbols":
                    #password length
                    passLength = int(input("Enter Password Length: "))
                    #data
                    lowercase = string.ascii_lowercase
                    uppercase = string.ascii_uppercase
                    number = string.digits
                    #combine data
                    data = lowercase + uppercase + number
                    #generate password
                    structure = random.sample(data,passLength)
                    password = "".join(structure) 
                    print(password)
            else:
                print("Invalid Choice")
    else: 
        print("Invalid Option...")  

