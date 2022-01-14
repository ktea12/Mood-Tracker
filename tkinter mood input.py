import tkinter as tk

HEIGHT = 100
WIDTH = 100

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=HEIGHT) #background
canvas.pack()

label = tk.Label(text="How is your mood today?")
label.pack()

button = tk.Button(root, text="1")
button.pack()

button = tk.Button(root, text="2")
button.pack()

button = tk.Button(root, text="3")
button.pack()

button = tk.Button(root, text="4")
button.pack()

button = tk.Button(root, text="5")
button.pack()

button = tk.Button(root, text="6")
button.pack()

button = tk.Button(root, text="7")
button.pack()

button = tk.Button(root, text="8")
button.pack()

button = tk.Button(root, text="9")
button.pack()

button = tk.Button(root, text="10")
button.pack()

root.mainloop()