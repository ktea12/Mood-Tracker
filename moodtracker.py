
from matplotlib import pyplot as plt
class moodcalc: #create class for calculating moods

    def __init__(self, morning, noon, night, ): #getter function, getting values: time of day, and level of mood
        self.tmorn = morning #level of mood in the morning
        self.tnoon = noon #level of mood at noon
        self.tnight = night #level of mood at night
        self.moodscore = [self.tmorn, self.tnoon, self.tnight]
        self.time_of_day = ['Morning', 'Noon', 'Night']
        self.morntf = None
        self.noontf = None
        self.nighttf = None

#Added attributes in the class called morningtf, noontf and nighttf
#these attributes are linking to the text field from the tkinter (morning, noon and night text fields)

    def update_inputs(self):
        morning2 = int(morning.get())
        noon2 = int(noon.get())
        night2 = int(night.get())

        self.moodscore = [morning2,noon2,night2]

    def graph_mood_score(self):
        self.update_inputs()
        plt.plot(self.time_of_day, self.moodscore)
        plt.xlabel('Time of Day')
        plt.ylabel('Mood Level')
        plt.title('Mood Level over Time')
        plt.show()