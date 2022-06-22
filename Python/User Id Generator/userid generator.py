import random
import string
print("Welcome to userid generator\nType help for help\nType generate to generate a userid\nType exclude an item\nType recommended or r to get a list of 5 userids that are generated with the recommended userid settings\n")
while True:
    choice = input("Enter choice: ")
    if choice in ("help", "generate", "exclude", "recommended", "r"):
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        number = string.digits
        symbol = string.punctuation
        if choice == "help":
            print("Type help to bring this text up again\nType generate to generate a userid without having to exclude anything\nType exclude to exclude a certain type from the userid.\nAvailable Items To Be Excluded:\nlowercase\nuppercase\nnumbers\nsymbols")
        if choice == "generate":
            length = int(input("Enter userid length: "))
            uppercase = string.ascii_uppercase
            lowercase = string.ascii_lowercase
            numbers = string.digits
            symbols = string.punctuation
            data = uppercase + lowercase + numbers + symbols
            struct = random.sample(data,length)
            userid = "U+"+"".join(struct)
            print(userid)
        if choice == "exclude":
            print("Available Items To Be Excluded:\nlowercase\nuppercase\nnumbers\nsymbols")
            choice = input("Enter What You Want To Be Excluded: ")
            if choice in ("lowercase", "uppercase", "numbers", "symbols"):
                if choice == "lowercase":
                    length = int(input("Enter userid Length: "))
                    data = uppercase + number + symbol
                    structure = random.sample(data,length)
                    userid = "U+"+"".join(structure) 
                    print(userid)
                elif choice == "uppercase":
                    length = int(input("Enter userid Length: "))
                    data = lowercase + number + symbol
                    structure = random.sample(data,length)
                    userid = "U+"+"".join(structure) 
                    print(userid)
                elif choice == "numbers":
                    length = int(input("Enter userid Length: "))
                    data = lowercase + uppercase + symbol
                    structure = random.sample(data,length)
                    userid = "U+"+"".join(structure) 
                    print(userid)
                elif choice == "symbols":
                    length = int(input("Enter userid Length: "))
                    data = lowercase + uppercase + number
                    structure = random.sample(data,length)
                    userid = "U+"+"".join(structure) 
                    print(userid)
        if choice == "recommended":
            print("Here are 5 random user ids: ")
            length = 20
            data = lowercase + uppercase + number
            structure = random.sample(data,length)
            userid1 = "U+"+"".join(structure) 
            print("------------------------\n",userid1)
            structure = random.sample(data,length)
            userid2 = "U+"+"".join(structure) 
            print("------------------------\n",userid2)
            structure = random.sample(data,length)
            userid3 = "U+"+"".join(structure) 
            print("------------------------\n",userid3)
            structure = random.sample(data,length)
            userid4 = "U+"+"".join(structure) 
            print("------------------------\n",userid4)
            structure = random.sample(data,length)
            userid5 = "U+"+"".join(structure) 
            print("------------------------\n",userid5, "\n------------------------")
            print("\n\nAll 5:\n", userid1,"\n", userid2,"\n", userid3,"\n", userid4,"\n", userid5)
        if choice == "r":
            print("Here are 5 random user ids: ")
            length = 20
            data = lowercase + uppercase + number
            structure = random.sample(data,length)
            userid1 = "U+"+"".join(structure) 
            print("------------------------\n",userid1)
            structure = random.sample(data,length)
            userid2 = "U+"+"".join(structure) 
            print("------------------------\n",userid2)
            structure = random.sample(data,length)
            userid3 = "U+"+"".join(structure) 
            print("------------------------\n",userid3)
            structure = random.sample(data,length)
            userid4 = "U+"+"".join(structure) 
            print("------------------------\n",userid4)
            structure = random.sample(data,length)
            userid5 = "U+"+"".join(structure) 
            print("------------------------\n",userid5, "\n------------------------")
            print("\n\nAll 5:\n", userid1,"\n", userid2,"\n", userid3,"\n", userid4,"\n", userid5)
    else:
        print("Invalid Choice...")