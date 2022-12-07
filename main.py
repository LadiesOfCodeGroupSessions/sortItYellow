class Balls:

    def __init__(self):
        self.total = 60

class Rack:

    def __init__(self):
        self.new_rack = []
        self.number_on_the_ball = 0
        self.firstElement = self.new_rack[:1]

    def put(self, number_on_the_ball):
        self.new_rack.append(number_on_the_ball)

    def count(self):
        return len(self.new_rack)

    def add(self, firstElement, number_on_the_ball):
        if firstElement < number_on_the_ball:
            self.new_rack.insert(1, number_on_the_ball)