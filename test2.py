import tkinter as tk                

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainPage, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(font=50, text="Welcome to Daily Mood Tracker")
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, font=50, text="Let's Go!", command=lambda: controller("PageTwo"))
        button.pack


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        WIDTH = 20
        HEIGHT = 10 

        label =tk.Label (text="Welcome to Mood track.")
        label.grid(row=1, column=4, pady=20)
        label =tk.Label (text="What Level is your Mood at?")
        label.grid(row=1, column=5, pady=20)

        button0=tk.Button(self, text="0\n\nVery Bad", width=WIDTH, height=HEIGHT)
        button0.grid(row=2, column=2, padx=7, pady=10)

        button1=tk.Button(self, text="1\n\nBad and Unproductive", width=WIDTH, height=HEIGHT)
        button1.grid(row=2,column=3, padx=7, pady=10)

        button2=tk.Button(self, text="2\n\nBad but Productive", width=WIDTH, height=HEIGHT)
        button2.grid(row=2,column=4, padx=7, pady=10)

        button3=tk.Button(self, text="3\n\nNot so Good but OK", width=WIDTH, height=HEIGHT)
        button3.grid(row=2,column=5, padx=7, pady=10)

        button4=tk.Button(self, text="4\n\nGood Mood", width=WIDTH, height=HEIGHT)
        button4.grid(row=2,column=6, padx=7, pady=10)

        button5=tk.Button(self, text="5\n\nVery Good Mood", width=WIDTH, height=HEIGHT)
        button5.grid(row=2,column=7, padx=7, pady=10)

        back =tk.Button (self, text="Go to Main Page", command=lambda: controller.show_frame("MainPage"))
        back.grid(row=6, column=4, pady=20)

        #graph =tk.Button (self, text="Plot Graph", command=mood.graph_mood_score(morningent,noonent,nightent))
        #graph.grid(row=6, column=5, pady=20)

if __name__ == "__main__":
    app = SampleApp()
    app.title("Mood Tracker")
    app.geometry("1000x500")
    app.mainloop()