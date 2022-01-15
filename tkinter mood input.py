from tkinter import *
import tkinter as tk

# create an instance of tkinter
win = tk.Tk()

#Define the size of the window
win.geometry("500x500")

#Name the title of the window
win.title("Mood Tracker")

# number of buttons
n=6

#Defining the row and column
i=3

#Iterating over the numbers till n and
#creating the button
for j in range(n):
   mybutton= Button(win, text=j)
   mybutton.grid(row=i, column=j)

# Keep the window open
win.mainloop()