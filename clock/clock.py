class Clock:
    def __init__(self, hour, minute):
        minutes = minute + hour*60
        self.hour = (minutes//60)%24
        self.minute = minutes %60

    def __repr__(self):
        return "%02d:%02d" % (self.hour, self.minute)

    def __eq__(self, other):
        return self.minute == other.minute and self.hour == other.hour

    def __add__(self, minutes):
        return Clock(self.hour, self.minute+minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute-minutes)