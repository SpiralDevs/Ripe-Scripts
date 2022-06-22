import time #SpiralGaming (github)
print("Welcome to Py-Timer")
while True:
    length = int(input("Enter Timer Length: "))
    def countdown(time_sec):
        while time_sec:
            mins, secs = divmod(time_sec, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat,end='\r')
            time.sleep(1)
            time_sec -= 1
        print("Timer Ended")
    yn = input("Continue? (y/n): ")
    if yn in ("y", "n"):
        if yn == "y":
            countdown(length)
        if yn == "n":
            print("Alright...")
    else:
        countdown(length)