import tkinter
from tkinter import *
import os

#creates a Tk() object
root = Tk()
root.title("Mood Tracker")
root.geometry("500x500")


#function to open the program on click
def openMoodint():
	os.system('c:/Users/Thara/Documents/GitHub/Mood-Tracker/tkintermoodtracker.py')

#--------------------------


canvas = tkinter.Canvas(root, height=500, width=500) #background size
canvas.pack()

label = tkinter.Label(root, font=50, text="Welcome to Daily Mood Tracker \n\nDo you wish to evaluate your Mood today? (YES/NO)")
label.place(relwidth=1, relheight=0.5)

#a button widget which will run the function for the program on click
button = tkinter.Button(root,font=50, text="Yes, Let's Go!", command=openMoodint)
button.place(relx=0.35, rely=0.4, relwidth=0.3, relheight=0.07)

button = tkinter.Button(root,font=50, text="Nope, Bye!", command=root.destroy)
button.place(relx=0.35, rely=0.5, relwidth=0.3, relheight=0.07)

#for window display
root.mainloop()
