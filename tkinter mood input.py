from matplotlib import pyplot as plt
import tkinter

root=tkinter.Tk()
root.title("Mood Tracker")
root.geometry("1000x500")

WIDTH = 20
HEIGHT = 10

class moodcalc: #create class for calculating moods

    def __init__(self, morning, noon, night): #getter function, getting values: time of day, and level of mood
        self.tmorn = morning #level of mood in the morning
        self.tnoon = noon #level of mood at noon
        self.tnight = night #level of mood at night
        self.moodscore = [self.tmorn, self.tnoon, self.tnight]
        self.time_of_day = ['Morning', 'Noon', 'Night']

    def get_avg(self):
        self.tmorn()
        self.tnoon()
        self.tnight()
        self.total = (self.tmorn + self.tnoon + self.tnight)//3
        return self.total

    def __str__(self) -> str: #setter function
        self.get_avg()
        return (f"Your mood averaged at level: {self.total}")

    def graph_mood_score(self):
        plt.plot(self.time_of_day, self.moodscore)
        plt.xlabel('Time of Day')
        plt.ylabel('Mood Level')
        plt.title('Mood Level over Time')
        plt.show()

mood=moodcalc()


label =tkinter.Label (text="Welcome to Mood track.")
label.grid(row=1, column=4, pady=20)
label =tkinter.Label (text="What Level is your Mood at?")
label.grid(row=1, column=5, pady=20)

button0=tkinter.Button(root, text="0\n\nVery Bad", width=WIDTH, height=HEIGHT)
button0.grid(row=2, column=2, padx=7, pady=10)

button1=tkinter.Button(root, text="1\n\nBad and Unproductive", width=WIDTH, height=HEIGHT)
button1.grid(row=2,column=3, padx=7, pady=10)

button2=tkinter.Button(root, text="2\n\nBad but Productive", width=WIDTH, height=HEIGHT)
button2.grid(row=2,column=4, padx=7, pady=10)

button3=tkinter.Button(root, text="3\n\nNot so Good but OK", width=WIDTH, height=HEIGHT)
button3.grid(row=2,column=5, padx=7, pady=10)

button4=tkinter.Button(root, text="4\n\nGood Mood", width=WIDTH, height=HEIGHT)
button4.grid(row=2,column=6, padx=7, pady=10)

button5=tkinter.Button(root, text="5\n\nVery Good Mood", width=WIDTH, height=HEIGHT)
button5.grid(row=2,column=7, padx=7, pady=10)

label =tkinter.Label (text="Morning Mood? ")
label.grid(row=3, column=4, pady=20)
morning = tkinter.Entry(font=40, width=15)
morning.grid(row=3, column=5, pady=20)

label =tkinter.Label (text="Mood at noon? ")
label.grid(row=4, column=4, pady=20)
noon = tkinter.Entry(font=40, width=15)
noon.grid(row=4, column=5, pady=20)

label =tkinter.Label (text="Mood at night? ")
label.grid(row=5, column=4, pady=20)
night = tkinter.Entry(font=40, width=15)
night.grid(row=5, column=5, pady=20)

back =tkinter.Button (text="Go to Main Page")
back.grid(row=6, column=4, pady=20)

graph =tkinter.Button (text="Plot Graph", command=mood.graph_mood_score())
graph.grid(row=6, column=5, pady=20)


root.mainloop()