app.background = 'salmon'

# thermometer
Rect(50, 90, 100, 250, fill='gainsboro')
Circle(100, 90, 50, fill='gainsboro')
Circle(70, 340, 20, fill='gainsboro')
Circle(130, 340, 20, fill='gainsboro')
Rect(70, 340, 60, 20, fill='gainsboro')

Circle(100, 320, 20, fill='white')
Rect(90, 75, 20, 250, fill='white')
Circle(100, 75, 10, fill='white')
Circle(100, 320, 13, fill='salmon')

# number labels and markings down the side
Line(78, 300, 78, 80, lineWidth=12, dashes=(1, 5))
Line(120, 300, 120, 80, lineWidth=5, dashes=(1, 3))
Label('F', 120, 70)
Label(20, 135, 290)
Label(40, 135, 250)
Label(60, 135, 210)
Label(80, 135, 170)
Label(100, 135, 130)
Label(120, 135, 90)

# display
Label("° Fahrenheit", 275, 250, size=20)
temperature = Label(120, 280, 180, size=60)

meter = Line(100, 320, 100, 90, fill='salmon', lineWidth=5)

def onMousePress(mouseX, mouseY):
    # First, adjust the meter length and display number depending on mouseY.
    ### (HINT: Use the inspector and try to scale mouseY values onto the
    #          possible meter and temperature values.)
    ### Place Your Code Here ###
    temperature.value = 120-(mouseY/4)  
    meter.y2 = 90+(mouseY/2)
    
    # Then, change the background according to the mouseY.
    ### (HINT: There are 8 different backgrounds. Start with the coldest first.)
    ### Place Your Code Here ###
    pass
    if (360 < mouseY <= 400):
        app.background = "royalBlue"
    if (290 < mouseY <= 360):
        app.background = "lightSkyBlue"
    if (250 < mouseY <= 290):
        app.background = "lightCyan"
    if (210 < mouseY <= 250):
        app.background = "honeyDew"
    if (170 < mouseY <= 210):
        app.background = "yellowGreen"
    if (130 < mouseY <= 170):
        app.background = "moccasin"
    if (90 < mouseY <= 130):
        app.background = "gold"
    if (0 < mouseY <= 90):
        app.background = "salmon"

