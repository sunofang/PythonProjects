import random
import time
import json

#Welcome to the nightmare that is P(Y)OLY
stoppedit = False
stoppedyet = 0

PolyLines = json.load(open("lines.json"))


while stoppedit == False:
    print(random.choice(PolyLines))
    stoppedyet += 1
    time.sleep(0.5)
    if stoppedyet >= 10: #Important! Modify this if statement to modify the amount of lines before you wanna ask the user to stop.
        dowantstop = input("Do you want to stop this joke yet? Y/N : ")
        if dowantstop == "y": #Stops the poly looping stuff
            stoppedit = True
            print("Very well.")
        else:
            print("Well then. I wont judge you.")
            time.sleep(1)
            stoppedyet = 1
