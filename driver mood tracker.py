from moodtracker import moodcalc

def mainmenu():
    confirm = str(input("Welcome to Daily Mood Tracker \n Do you wish to evaluate your mood today? (YES/NO) "))
    while True: #keeps the user to prompt the question and answer with "YES" or "NO"
        if confirm.upper() == "YES":
            pass
        elif confirm.upper() == "NO":
            print("Goodbye!")
            break
        else:
            print("Please input YES or NO")

    def moodlistQL():
        moodlist = [] #creating an empty list

        while True: #keeps the user to prompt atleast more than 0
            print("Please input a number from 1 to 10")
            morning = int(input("At what level was your mood in the morning? ")) 
            noon = int(input("At what level was your mood at noon? ")) #here is to input the mood level using int which accepts integers only
            night = int(input("At what level was your mood at night? "))
            moodlvl = moodlistQL(morning, noon, night)
            if 11 > morning == 0:
                print("You must input a number above 0 and less than 10") #check if input level is 0 or above 10
            elif 11 > noon == 0:
                print("You must input a number above 0 and less than 10")
            elif 11 > night == 0:
                print("You must input a number above 0 and less than 10")
            else:
                break
        moodlist.append(moodlvl) #adds object to the mood list created earlier
        
        return moodlist