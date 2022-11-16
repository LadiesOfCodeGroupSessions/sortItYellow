from main import Balls
from main import Rack

def test_totalBalls():
    balls = Balls()
    assert balls.total == 60

def test_new_rack():
    rack = Rack()
    assert len(rack.list) == 0

def test_add_ball_to_rack():
    rack = Rack()
    rack.add(20)
    assert rack.__eq__([20])

def test_add_me_correctly():
    rack = Rack()
    rack.add(10)
    rack.add(20)
    rack.add(30)
    assert  rack.__eq__([10, 20])