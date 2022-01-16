from logging import root
from matplotlib import pyplot as plt
import tkinter

#

class Bill_App:
    def __init__(self, root):
        root=tkinter.Tk()
        self.root = root
        self.root.geometry("1000x500")
        self.root.title("Mood Tracker")

        self.morningent = tkinter.IntVar()
        self.noonent = tkinter.IntVar()
        self.nightent = tkinter.IntVar()

        mornq = tkinter.Label(text="Morning Mood? ").grid(row=3, column=4, pady=20)
        morninglvl = tkinter.Entry(textvariable=self.morningent).grid(row=3, column=5, pady=20)
        self.options_list1 = [0, 1, 2, 3, 4, 5]
        self.morn.set("Morning:")

        tmorn = tkinter.OptionMenu(self.tmorn, *self.options_list1)
        tmorn.place(x=98,y=15,width=50,height=30)


        noonq = tkinter.Label(text="Mood at Noon? ").grid(row=3, column=4, pady=20)
        noonlvl = tkinter.Entry(textvariable=self.noonent).grid(row=3, column=5, pady=20)
        self.options_list2 = [0, 1, 2, 3, 4, 5]
        self.noon.set("Noon:")

        tnoon = tkinter.OptionMenu(self.tnoon, *self.options_list2)
        tnoon.place(x=98,y=15,width=50,height=30)


        nightq = tkinter.Label(text="Mood at Noon? ").grid(row=3, column=4, pady=20)
        nightlvl = tkinter.Entry(textvariable=self.nightent).grid(row=3, column=5, pady=20)
        self.options_list3 = [0, 1, 2, 3, 4, 5]
        self.night.set("Noon:")

        tnight = tkinter.OptionMenu(self.tnight, *self.options_list3)
        tnight.place(x=98,y=15,width=50,height=30)
        
        
        root.mainloop()