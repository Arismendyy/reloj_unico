position_second = 0
position_minute = 0
position_hour = 0
def setup():
    size(500,300)
def draw():
    global position_second
    global position_minute
    global position_hour
    background(map(second(), 0, 59, 0, 255))
    fill(map(second(), 0, 59, 255, 0))
    ellipse(position_second,80,50,50,)
    position_second = position_second + 1
    if position_second > width:
        position_second = 0
        background(171,154,250)
