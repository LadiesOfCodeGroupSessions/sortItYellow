class BallsCollection:

    def __init__(self):
        self.balls = {list(range(0, 59))}
        print(self.balls)

    def takeaway(self):
        pass

    def count(self):
        return len(self.balls)


class Rack:

    def __init__(self):
        self.new_rack = []

    def put(self, number_on_the_ball):
        self.new_rack.append(number_on_the_ball)

    def count(self):
        return len(self.new_rack)

    def add(self, firstElement, number_on_the_ball):
        if firstElement < number_on_the_ball:
            self.new_rack.insert(1, number_on_the_ball)