import tkinter as tk

HEIGHT = 700
WIDTH = 1400

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=HEIGHT) #background
canvas.pack()

label = tk.Label(text="Welcome to Daily Mood Tracker \n Do you wish to evaluate your mood today? (YES/NO)")
label.pack()

entry = tk.Entry(font=40)
entry.pack()

button = tk.Button(root, text="Next")
button.pack()

root.mainloop()