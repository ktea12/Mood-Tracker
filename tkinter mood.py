import tkinter as tk

def mainmenu():
    confirm = entry.get().strip()
    while True: #keeps the user to prompt the question and answer with "YES" or "NO"
        if confirm.upper() == str("YES"):
            pass
        elif confirm.upper() == str("NO"):
            label['text'] = "Goodbye!\nInput YES to evaluate Mood."
            break
        else:
            label['text'] = "Please input YES or NO\nDo you wish to evaluate your Mood today?"
            break

HEIGHT = 500
WIDTH = 700

root = tk.Tk()

root.title("Mood Tracker")

canvas = tk.Canvas(root, height=HEIGHT, width=HEIGHT) #background
canvas.pack()

label = tk.Label(font=50, text="Welcome to Daily Mood Tracker \n\nDo you wish to evaluate your Mood today? (YES/NO)")
label.place(relwidth=1, relheight=0.5)

entry = tk.Entry(font=40)
entry.place(relx=0.35, rely=0.4, relwidth=0.3)

entry.bind('<Return>', mainmenu) 

button = tk.Button(root,font=50, text="Enter", command=mainmenu)
button.place(relx=0.35, rely=0.5, relwidth=0.3, relheight=0.07)


entry.focus() 

root.mainloop() #for window display