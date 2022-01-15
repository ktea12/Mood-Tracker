import tkinter as tk

HEIGHT = 500
WIDTH = 700

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=HEIGHT) #background
canvas.pack()

label = tk.Label(font=50, text="Welcome to Daily Mood Tracker \n Do you wish to evaluate your mood today? (YES/NO)")
label.place(relwidth=1, relheight=0.5)

entry = tk.Entry(font=40)
entry.place(relx=0.35, rely=0.4, relwidth=0.3)

button = tk.Button(root,font=50, text="Next")
button.place(relx=0.35, rely=0.5, relwidth=0.3, relheight=0.07)

root.mainloop()