#random number generator - by Spiral
import random
#prints ui
print("Type help for help")
print("Type random to get options of presets for random numbers, or chose two numbers")
print("Type custom to chose two specific numbers and get a random number from the two numbers")
#ongoing
while True:
    choice = input("Enter Option: ")
    if choice in ("help", "random", "custom"):
        if choice == "help":
            print("Type help to bring this text up again.\nType random to give options for random number presets.\nType custom to chose two specific numbers and get a random number from the two numbers\n")
            print(" ")
            print("If you type random you have a list of random number presets avaliable to use.\nAll presets chose a random number between 1 and the number of the preset.\nYou may use the following presets:\n2,\n10,\n100,\n250,\n1000,\n10000,\nand finally custom in which you choose your own digits")
        elif choice == "random":
            print("2,\n10,\n100,\n250,\n1000,\n10000,\nor custom for your own digits")    
            randomchoice = input("Enter Choice: ")
            if randomchoice in ("custom","2","10","100","250","500","1000","10000"):               
                if randomchoice == "custom":
                    num1 = int (input("Chose first number: "))
                    num2 = int (input("Chose second number: "))
                    randomNumberResult = random.randint(num1,num2)
                    print("Your random number is: ", randomNumberResult)
                    if num1 > num2:
                        print("Error: second number is larger than first number")               
                elif randomchoice == "2":
                    result = random.randint(1,2)
                    print("Your random number is: ", result)
                elif randomchoice == "10":
                    result = random.randint(1,10)
                    print("Your random number is: ", result)
                elif randomchoice == "100":
                    result = random.randint(1,100)
                    print("Your random number is: ", result)
                elif randomchoice == "250":
                    result = random.randint(1,250)
                    print("Your random number is: ", result)
                elif randomchoice == "500":
                    result = random.randint(1,500)
                    print("Your random number is: ", result)
                elif randomchoice == "1000":
                    result = random.randint(1,1000)
                    print("Your random number is: ", result)
                elif randomchoice == "10000":
                    result = random.randint(1,10000)
                    print("Your random number is: ", result)                                    
        elif choice == "custom":
                num1 = int (input("Chose first number: "))
                num2 = int (input("Chose second number: "))
                randomNumberResult = random.randint(num1, num2)
                print("Your random number is: ", randomNumberResult)
                if num1 > num2:
                    print("Error: second number is larger than first number")            
    else:
        print("Invalid Choice")