app.background = 'black'

# center line
Line(200, 0, 200, 400, fill='white', dashes=True)

leftPlayer = Rect(10, 200, 10, 50, fill='white')
rightPlayer = Rect(380, 200, 10, 50, fill='white')
ball = Circle(200, 200, 10, fill='white')
ball.dx = randrange(5, 10)
ball.dy = randrange(5, 10)

def onMouseMove(mouseX, mouseY):
    # move right player
    rightPlayer.centerY = mouseY

def onKeyPress(key):
    # move left player
    if (key == 'up'):
        leftPlayer.centerY -= 30

    if (key == 'down'):
        leftPlayer.centerY += 30

def onStep():
    # Move the ball by ball.dx and ball.dy.
    ball.centerX += ball.dx
    ball.centerY += ball.dy

    # Make the ball bounce off the top and bottom of the screen.
    if (ball.top <= 0):
        ball.dy = randrange(5, 10)
    if (ball.bottom >= 400):
        ball.dy = -randrange(5, 10)

    if (ball.hitsShape(leftPlayer) == True):
        ball.dx = randrange(5, 10)

    if (ball.hitsShape(rightPlayer) == True):
        ball.dx = randrange(-10, -5)

    # If the ball goes off the left side of the screen, the right player
    # should win. If the ball goes off the right side of the screen,
    # the left player should win. Also, use app.stop() after either player
    # wins to stop the game.
    ### (HINT: Let one player win and use the inspector to draw the correct
    #          message!)
    ### Place Your Code Here ###
    if (ball.centerX < 0):
        Label("Right Player Wins!", 200, 200, fill='white', size=40, font='arial')
        app.stop()
    if (ball.centerX > 400):
        Label("Left Player Wins!", 200, 200, fill='white', size=40, font='arial')
        app.stop()


