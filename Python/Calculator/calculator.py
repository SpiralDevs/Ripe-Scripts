#operand
print("+ for Addition")#
print("- for Subtraction")#
print("* for Multiplcation")#
print("/ for Division")#

while True:
    
    #input operand
    choice = input("Enter Operand: ")#
    
    if choice in ("+", "-", "*", "/"):

        #nums
        num1 = float (input("Enter First Number: "))#
        num2 = float (input("Enter Second Number: "))#
        
        # results
        addresult = num1+num2#
        subresult = num1-num2#
        mulresult = num1*num2#
        divresult = num1/num2#
        
        if choice == "+":
            print(num1, "+", num2, "=", addresult)#
        elif choice == "-":
            print(num1, "-", num2, "=", subresult)#
        elif choice == "*":
            print(num1, "*", num2, "=", mulresult)#
        elif choice == "/":
            if num2 == 0.0:
                print("Divide by 0 error")
            else:
                print(num1, "/", num2, "=", divresult)#

        else: 
            print("Invalid Choice")#