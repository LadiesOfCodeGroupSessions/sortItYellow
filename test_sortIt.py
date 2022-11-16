from main import Balls
from main import Rack

def test_totalBalls():
    balls = Balls()
    assert balls.total == 60

def test_new_rack():
    rack = Rack()
    assert rack.__eq__([])

def test_add_ball_to_rack():
    rack = Rack()
    rack.add(20)
    assert rack.__eq__([20])