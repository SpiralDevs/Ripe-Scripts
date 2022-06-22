import random
from pystyle import Colors, Write
Write.Print("Welcome to the number guessing game!\n\nType help for help\n", Colors.cyan, interval=0.0025)
while True:
    command = Write.Input("Please enter a command: ", Colors.light_red, interval=0.0025, hide_cursor=False)
    if command in ("help", "h", "10", "ten", "100", "hundred", "custom", "c", "exit", "e", "quit", "q"):
        if command == "help" or command == "h":
            Write.Print("\nCommands:\n\nhelp/h - Prints this help message\n\n10/ten - Guesses a number between 1 and 10\n\n100/hundred - Guesses a number between 1 and 100\n\ncustom/c - Guesses a number between 1 and your input\n\n", Colors.cyan, interval=0.0025)
        if command == "10" or command == "ten":
            Write.Print("\nYou have chosen to guess a number between 1 and 10.\n", Colors.cyan, interval=0.0025)
            number = random.randint(1, 10)
            guess = int(Write.Input("\nGuess a number between 1 and 10: ", Colors.light_red, interval=0.0025, hide_cursor=False))
            if guess == number:
                Write.Print(f"\nYou guessed correctly!\nThe number is {number}\n", Colors.green, interval=0.0025)
            else:
                Write.Print(f"\nYou guessed incorrectly!\nThe number is {number}\n", Colors.red, interval=0.0025)
        if command == "100" or command == "hundred":
            Write.Print("\nYou have chosen to guess a number between 1 and 100.\n", Colors.cyan, interval=0.0025)
            number = random.randint(1, 100)
            guess = int(Write.Input("\nGuess a number between 1 and 100\n", Colors.light_red, interval=0.0025, hide_cursor=False))
            if guess == number:
                Write.Print(f"\nYou guessed correctly!\n The number is {number}\n", Colors.green, interval=0.0025)
            else:
                Write.Print(f"\nYou guessed incorrectly!\n The number is {number}\n", Colors.red, interval=0.0025)
        if command == "custom" or command == "c":
            number = random.randint(1, int(Write.Input("Please enter a number: ", Colors.light_red, interval=0.0025, hide_cursor=False)))
            guess = int(Write.Input("Please guess the number: ", Colors.light_red, interval=0.0025, hide_cursor=False))
            if guess == number:
                Write.Print(f"\nYou guessed the number correctly!\nThe number is {number}\n", Colors.green)
            else:
                Write.Print(f"\nYou guessed the number incorrectly!\nThe number is {number}\n", Colors.red)          
        if command == "exit" or command == "quit" or command == "e" or command == "q":
            Write.Print("\n\nThank you for playing!\n\n", Colors.cyan, interval=0.0025)
            break
    else:
        Write.Print("\n\nInvalid command!\n\n", Colors.dark_gray, interval=0.0025)