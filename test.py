# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from moodtracker import moodcalc
import tkinter
from tkinter import *
from tkinter.ttk import *

# creates a Tk() object
root = Tk()

# sets the geometry of main
# root window
root.geometry("500x500")


# function to open a new window
# on a button click
def openMoodint():
	
	# Toplevel object which will be treated as a new window
	Moodint = Toplevel(root)
	Moodint.title("Mood Tracker")
	Moodint.geometry("1000x500")

	WIDTH = 20
	HEIGHT = 10

	label =tkinter.Label (Moodint, text="Welcome to Mood track.")
	label.grid(row=1, column=4, pady=20)
	label =tkinter.Label (Moodint, text="What Level is your Mood at?")
	label.grid(row=1, column=5, pady=20)

	button0=tkinter.Button(Moodint, text="0\n\nVery Bad", width=WIDTH, height=HEIGHT, bg="red")
	button0.grid(row=2, column=2, padx=7, pady=10)

	button1=tkinter.Button(Moodint, text="1\n\nBad and Unproductive", width=WIDTH, height=HEIGHT, bg="orange")
	button1.grid(row=2,column=3, padx=7, pady=10)

	button2=tkinter.Button(Moodint, text="2\n\nBad but Productive", width=WIDTH, height=HEIGHT, bg="yellow")
	button2.grid(row=2,column=4, padx=7, pady=10)

	button3=tkinter.Button(Moodint, text="3\n\nNormal", width=WIDTH, height=HEIGHT, bg="dark green")
	button3.grid(row=2,column=5, padx=7, pady=10)

	button4=tkinter.Button(Moodint, text="4\n\nGood Mood", width=WIDTH, height=HEIGHT, bg="green")
	button4.grid(row=2,column=6, padx=7, pady=10)

	button5=tkinter.Button(Moodint, text="5\n\nVery Good Mood", width=WIDTH, height=HEIGHT, bg="light green")
	button5.grid(row=2,column=7, padx=7, pady=10)

	label =tkinter.Label (Moodint, text="Morning Mood? ")
	label.grid(row=3, column=4, pady=20)

	label =tkinter.Label (Moodint,text="Mood at noon? ")
	label.grid(row=4, column=4, pady=20)

	label =tkinter.Label (Moodint, text="Mood at night? ")
	label.grid(row=5, column=4, pady=20)

	entry1 = tkinter.Entry(Moodint, font=40, width=15)
	entry1.grid(row=3, column=5, pady=20)

	
	entry2 = tkinter.Entry(Moodint, font=40, width=15)
	entry2.grid(row=4, column=5, pady=20)

	entry3 = tkinter.Entry(Moodint, font=40, width=15)
	entry3.grid(row=5, column=5, pady=20)

	# morning2 = int(morning.get())
	# noon2 = int(noon.get())
	# night2 = int(night.get())

	# moodlevel = [morning2,afternoon2,night2]

	# mood=moodcalc(morning2,noon2,night2)

	mood=moodcalc(0,0,0)

	mood.morntf = entry1
	mood.noontf = entry2
	mood.nighttf = entry3

	graph =tkinter.Button(Moodint, text="Plot Graph", command=mood.graph_mood_score)
	graph.grid(row=6, column=5, pady=20) #Fuction graph : -> get values that was entered in the field and graph in the matplot

#--------------------------
root.title("Mood Tracker")

canvas = tkinter.Canvas(root, height=500, width=500) #background
canvas.pack()

label = tkinter.Label(font=50, text="Welcome to Daily Mood Tracker \n\nDo you wish to evaluate your Mood today?")
label.place(relwidth=1, relheight=0.5)

# a button widget which will open a
# new window on button click
button = tkinter.Button(root,font=50, text="Yes, Let's Go!", command=openMoodint)
button.place(relx=0.35, rely=0.4, relwidth=0.3, relheight=0.07)

button = tkinter.Button(root,font=50, text="Nope, Bye!", command=root.destroy)
button.place(relx=0.35, rely=0.5, relwidth=0.3, relheight=0.07)

# mainloop, runs infinitely
root.mainloop()