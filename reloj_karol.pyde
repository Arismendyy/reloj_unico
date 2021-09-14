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
    else: 
        position_second = map(second(), 0, 59, 0, width)
    fill(map(minute(), 0, 59, 0, 255))
    ellipse(position_minute,150,50,50,)
    position_minute =+ 1
    if position_minute > width:
        position_minute = 0
    else: 
        position_minute = map(minute(), 0, 59, 0, width)
    fill(map(hour(), 0, 59, 255, 0))
    ellipse(position_hour,220,50,50,)
    position_hour =+ 1
    if position_hour > width:
        position_hour = 0
    else: 
        position_hour = map(hour(), 0, 24, 0, width)
    if position_hour < width/2:
        fill(255,233,26)
        ellipse(0,0,70,70)
    else:
        fill(162,162,156)
        ellipse(width,0,70,70)
