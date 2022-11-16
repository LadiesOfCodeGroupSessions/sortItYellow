class Balls:

    def __init__(self):
        self.total = 60

class Rack:

    def __init__(self):
        self.list = []
        self.number_on_the_ball = 0
        self.firstElement = list[:1]

    def append(self, number_on_the_ball):
        pass

    def add(self, firstElement, number_on_the_ball):
        if firstElement < number_on_the_ball:
            list.insert(1, number_on_the_ball)