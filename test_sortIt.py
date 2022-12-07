from main import BallsCollection
from main import Rack

def test_totalBalls():
    balls = BallsCollection()
    assert balls.count() == 60

def test_new_rack():
    rack = Rack()
    assert len(rack.new_rack) == 0

def test_add_ball_to_rack():
    rack = Rack()
    balls = BallsCollection()
    balls.takeaway(20)
    rack.put(20)
    assert rack.count() == 1
    assert balls.count() == 59
