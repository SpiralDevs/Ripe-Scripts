import random as r
print("Welcome to the Game genre, name, and mode Generator\n\nType help for help\nType generate to generate a random game.\n\nDM on discord at 'Spiral#1234' if you want me to help you with ideas or suggestions for your game.")
while True:
    cmd = input("Enter Command: ")
    if cmd in ("help", "generate"):
        if cmd == "help":
            print("This is the Game genre, name, and mode Generator\n\nType help to reopen this text\nType generate to generate a random game.\n\nDM on discord at 'Spiral#1234' if you want me to help you with ideas or suggestions for your game.")
        if cmd == "generate":
            print("Details successfully generated randomly")
            #name
            namelist1 = ["Dark", "Dead", "Silent", "Until", "Final", "Super", "Mega", "System", "Raid", "Last", "Chase", "Non-stop", "Cave", "Target", "Wave", "Double", "Straight", "Bubble", "Orange"]
            namelist2 = ["Phobia", "Evil", "Death", "Auto", "Super", "Age", "Ultimate", "Theory", "Craft", "Prime", "Dash", "Together", "Revenge", "Ditch", "Raze", "Dart", "Curve", "Back", "Waiver"]
            chooseFromName1 = r.choice(namelist1)
            chooseFromName2= r.choice(namelist2)
            name = chooseFromName1 + " " +chooseFromName2
            #genre
            genreList = ["Sandbox", "Real-time strategy (RTS)", "Shooter (FPS and TPS)", "Multiplayer online battle arena (MOBA)", "Role-playing (RPG, ARPG)", "Simulation", "Puzzle", "Party Game", "Action-adventure", "Survival/Horror", "Platformer"]
            chooseFromGenre = r.choice(genreList)
            genre = chooseFromGenre
            #Error Fix
            #mode
            if genre == "Multiplayer online battle arena (MOBA)":
                mode = "Multiplayer"
            elif genre == "Party Game":
                mode = "Multiplayer/Co-op"
            else:
                modelist = ["Single Player", "Multiplayer", "Co-op"]
                chooseFromMode = r.choice(modelist)
                mode = chooseFromMode
            print("Game Generated... Details Below:\n\nGenerated Game Name: ", name, "\nGenerated Game Genre: ", genre, "\nGenerated Player Mode: ", mode)
    else: 
        print("Invalid Command...")