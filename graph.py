from moodtracker import moodcalc

class graphmood(moodcalc): #create class for graphing moods
    import matplotlib.pyplot as plt
    plt.plot(range(10), moodlist)
    plt.show()
