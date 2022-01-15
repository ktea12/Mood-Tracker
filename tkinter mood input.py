import tkinter
from turtle import width

root=tkinter.Tk()
root.title("Mood Tracker")
root.geometry("1000x500")

WIDTH = 20
HEIGHT = 10

label =tkinter.Label ( text="Welcome to Mood track.")
label.grid(row=1, column=4)
label =tkinter.Label ( text="What Level is your Mood at?")
label.grid(row=1, column=5)

button0=tkinter.Button(root, text="0\n\nVery Bad", width=WIDTH, height=HEIGHT)
button0.grid(row=2, column=2, padx=7)

button1=tkinter.Button(root, text="1\n\nBad and Unproductive", width=WIDTH, height=HEIGHT)
button1.grid(row=2,column=3, padx=7)

button2=tkinter.Button(root, text="2\n\nBad but Productive", width=WIDTH, height=HEIGHT)
button2.grid(row=2,column=4, padx=7)

button3=tkinter.Button(root, text="3\n\nNot so Good but OK", width=WIDTH, height=HEIGHT)
button3.grid(row=2,column=5, padx=7)

button4=tkinter.Button(root, text="4\n\nGood Mood", width=WIDTH, height=HEIGHT)
button4.grid(row=2,column=6, padx=7)

button5=tkinter.Button(root, text="5\n\nVery Good Mood", width=WIDTH, height=HEIGHT)
button5.grid(row=2,column=7, padx=7)

root.mainloop()