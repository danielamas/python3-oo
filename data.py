class Data:

    def __init__(self, day, mounth, year):
        self.day = day
        self.mounth = mounth
        self.year = year

    def formatada(self):
        print("{0}/{1}/{2}".format(self.day,self.mounth,self.year))