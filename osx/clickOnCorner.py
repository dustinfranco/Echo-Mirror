from pymouse import PyMouse

def clickOnCorner():
    m = PyMouse()
    x = 1438
    y = 2558
    m.move(x,y)
    m.click(x,y) #the third argument "1" represents the mouse button
    m.press(x,y) #mouse button press
    m.release(x,y) #mouse button release
