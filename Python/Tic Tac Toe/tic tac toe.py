from pystyle import Write, Colors
Write.Print("Welcome To Py Tic Tac Toe\n", Colors.baby_blue, interval=0.035)
theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }
board_keys = []
for key in theBoard:
    board_keys.append(key)
while True:
    def printBoard(board):
        Write.Print(board['1'] + '|' + board['2'] + '|' + board['3'], Colors.baby_blue, interval=0.001)
        Write.Print('\n-+-+-\n', Colors.baby_blue, interval=0.001)
        Write.Print(board['4'] + '|' + board['5'] + '|' + board['6'], Colors.baby_blue, interval=0.001)
        Write.Print('\n-+-+-\n', Colors.baby_blue, interval=0.001)
        Write.Print(board['7'] + '|' + board['8'] + '|' + board['9'], Colors.baby_blue, interval=0.001)
    def game():
        turn = 'X'
        count = 0
        for i in range(10):
            printBoard(theBoard)
            Write.Print("\n\nIt's your turn, " + turn + ". Move to which place: ", Colors.dap_blue, interval=0.001)
            move = input()        
            if theBoard[move] == ' ':
                theBoard[move] = turn
                count += 1
            else:
                Write.Print("That place is already filled.\nMove to which place: \n", Colors.baby_blue, interval=0.001)
                continue
            if count >= 5:
                if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                    printBoard(theBoard)
                    Write.Print("\nGame Over.\n", Colors.red_to_green, interval=0.001)                
                    Write.Print("**** " +turn + " won. ****\n", Colors.baby_blue, interval=0.001)                
                    break
                elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                    printBoard(theBoard)
                    Write.Print("\nGame Over.\n", Colors.red_to_green, interval=0.001)                
                    Write.Print(" **** " +turn + " won. ****", Colors.baby_blue, interval=0.001)
                    break
                elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                    printBoard(theBoard)
                    Write.Print("\nGame Over.\n", Colors.red_to_green, interval=0.001)                
                    Write.Print(" **** " +turn + " won. ****", Colors.baby_blue, interval=0.001)
                    break
                elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                    printBoard(theBoard)
                    Write.Print("\nGame Over.\n", Colors.red_to_green, interval=0.001)            
                    Write.Print(" **** " +turn + " won. ****", Colors.baby_blue, interval=0.001)
                    break
                elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                    printBoard(theBoard)
                    Write.Print("\nGame Over.\n", Colors.red_to_green, interval=0.001)                
                    Write.Print(" **** " +turn + " won. ****", Colors.baby_blue, interval=0.001)
                    break
                elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                    printBoard(theBoard)
                    Write.Print("\nGame Over.\n", Colors.red_to_green, interval=0.001)                
                    Write.Print(" **** " +turn + " won. ****", Colors.baby_blue, interval=0.001)
                    break 
                elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                    printBoard(theBoard)
                    Write.Print("\nGame Over.\n", Colors.red_to_green, interval=0.001)                
                    Write.Print(" **** " +turn + " won. ****", Colors.baby_blue, interval=0.001)
                    break
                elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                    printBoard(theBoard)
                    Write.Print("\nGame Over.\n", Colors.red_to_green, interval=0.001)                
                    Write.Print(" **** " +turn + " won. ****", Colors.baby_blue, interval=0.001)
                    break 
            if count == 9:
                Write.Print("\nGame Over.\n", Colors.yellow, interval=0.001)                
                Write.Print("It's a Tie!!", Colors.baby_blue, interval=0.001)
            if turn =='X':
                turn = 'O'
            else:
                turn = 'X'
        restart = Write.Input("Do want to play Again?(y/n)", Colors.light_cyan, interval=0.001)
        if restart == "y" or restart == "Y":  
            for key in board_keys:
                theBoard[key] = " "
            game()
        elif restart == "n" or restart == "N":
            Write.Print("\nBye!!", Colors.red_to_green, interval=0.001)
            exit()
        else: 
            Write.Print("Invalid entry!!", Colors.light_cyan, interval=0.001)
    game()