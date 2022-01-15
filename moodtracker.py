from matplotlib import pyplot as plt

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
        plt.ylabel('Mood Score')
        plt.title('Mood Score over Time')
        plt.show()

mood=moodcalc(1,2,3)
mood.graph_mood_score()