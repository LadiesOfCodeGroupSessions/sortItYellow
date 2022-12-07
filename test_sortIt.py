from main import Balls
from main import Rack

def test_totalBalls():
    balls = Balls()
    assert balls.total == 60

def test_new_rack():
    rack = Rack()
    assert len(rack.new_rack) == 0

def test_add_ball_to_rack():
    rack = Rack()
    rack.put(20)
    assert rack.count()==1
