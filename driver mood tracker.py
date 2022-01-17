from moodtracker import moodcalc

def mainmenu():
    confirm = str(input("Welcome to Daily Mood Tracker \nDo you wish to evaluate your mood today? (YES/NO) "))
    while True: #keeps the user to prompt the question and answer with "YES" or "NO"
        if confirm.upper() == "YES":
            pass
        elif confirm.upper() == "NO":
            print("Goodbye!")
            break
        else:
            print("Please input YES or NO")
            confirm = str(input("Welcome to Daily Mood Tracker \nDo you wish to evaluate your mood today? (YES/NO) "))

def moodlistQL():

    print("Please input a number between 0 to 5")
    
    while True: #keeps the user to prompt atleast more than 0
        morning = int(input("At what level was your mood in the morning? ")) 
        noon = int(input("At what level was your mood at noon? ")) #here is to input the mood level using int which accepts integers only
        night = int(input("At what level was your mood at night? "))
        
        if (morning < 6 and morning >= 0) and (noon < 6 and noon >= 0) and (night < 6 and night >= 0):
            pass
        else:
            print("You must input a number between 0 and 5") #check if input level is between 0 and 5
            morning = int(input("At what level was your mood in the morning? ")) 
            noon = int(input("At what level was your mood at noon? ")) #here is to input the mood level using int which accepts integers only
            night = int(input("At what level was your mood at night? "))
        
        print(f"Your mood averaged at level: {(morning + noon + night)//3}")#calculate average mood level

moodlistQL()