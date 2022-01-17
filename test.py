# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
import tkinter
from tkinter.ttk import *

# creates a Tk() object
root = Tk()

# sets the geometry of main
# root window
root.geometry("500x500")


# function to open a new window
# on a button click
def openNewWindow():
	
	# Toplevel object which will
	# be treated as a new window
	newWindow = Toplevel(root)

	# sets the title of the
	# Toplevel widget
	newWindow.title("New Window")

	# sets the geometry of toplevel
	newWindow.geometry("200x200")

	# A Label widget to show in toplevel
	Label(newWindow,
		text ="This is a new window").pack()


root.title("Mood Tracker")

canvas = tkinter.Canvas(root, height=500, width=500) #background
canvas.pack()

label = tkinter.Label(font=50, text="Welcome to Daily Mood Tracker \n\nDo you wish to evaluate your Mood today?")
label.place(relwidth=1, relheight=0.5)

# a button widget which will open a
# new window on button click
button = tkinter.Button(root,font=50, text="Yes, Let's Go!", command=openNewWindow)
button.place(relx=0.35, rely=0.4, relwidth=0.3, relheight=0.07)

button = tkinter.Button(root,font=50, text="Nope, Bye!", command=root.destroy)
button.place(relx=0.35, rely=0.5, relwidth=0.3, relheight=0.07)



# mainloop, runs infinitely
mainloop()