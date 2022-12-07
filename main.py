class BallsCollection:

    def __init__(self):
        self.balls = set(list(range(0, 60)))
        print(self.balls)

    def takeaway(self, ball):
        self.balls.remove(ball)

    def count(self):
        return len(self.balls)


class Rack:

    def __init__(self):
        self.new_rack = []

    def put(self, ball):
        self.new_rack.append(ball)

    def count(self):
        return len(self.new_rack)

    def add(self, firstElement, number_on_the_ball):
        if firstElement < number_on_the_ball:
            self.new_rack.insert(1, number_on_the_ball)