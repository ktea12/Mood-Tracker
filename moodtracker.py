class moodcalc: #create class for calculating moods

    def __init__(self, morning, noon, night): #getter function, getting values: time of day, and level of mood
        self.tmorn = morning #level of mood in the morning
        self.tnoon = noon #level of mood at noon
        self.tnight = night #level of mood at night

    def get_avg(self):
        self.tmorn()
        self.tnoon()
        self.tnight()
        self.total = (self.tmorn + self.tnoon + self.tnight)//3
        return self.total

    def __str__(self) -> str: #setter function
        self.get_avg()
        return (f"Your mood averaged at level: {self.total}")