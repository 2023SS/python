
app.background = 'black'

breakoutRects = Group()

player = Rect(150, 350, 100, 25, fill='orange')
ball = Circle(200, 340, 10, fill='orange')

def drawBlocks():
    for row in range(5):
        top = 50 + row * 20
        height = 20
        for col in range(6):
            left = 50 + col * 50
            width = 50
            if (row == 0):
                color = 'paleVioletRed'
            if (row == 1):
                color = 'darkTurquoise'
            if (row == 2):
                color = 'lightGreen'
            if (row == 3):
                color = 'gold'
            if (row == 4):
                color = 'mediumPurple'
            breakoutRects.add(
                Rect(left, top, width, height, fill=color, border='black')
                )

drawBlocks()

# Set ball.dx to a random number between 5 and 10, and ball.dy to -5.
ball.dx = randrange(5, 10)
ball.dy = -5

def onMouseMove(mouseX, mouseY):
    # Move the centerX of the player to the x coordinate of the mouse.
    player.centerX = mouseX

def onStep():
    # Move the ball by using the ball.dx and ball.dy properties.
    ball.centerX += ball.dx
    ball.centerY += ball.dy

    # If ball.centerX hits the left edge of the canvas, set the ball.dx to
    # a random number between 5 and 10.
    if (ball.centerX <= 0):
        ball.dx = randrange(5, 10)

    # If ball.centerX hits the right edge of the canvas, set the ball.dx to
    # a random number between -10 and -5.
    if (ball.centerX >= 400):
        ball.dx = randrange(-10, -5)

    # If ball.centerY hits the top of the canvas, set the ball.dy to 5.
    if (ball.centerY <= 0):
        ball.dy = 5

    # If the ball hits the player, set the ball.dy to -5.
    if (ball.hitsShape(player) == True):
        ball.dy = -5

    # Use a for loop to loop over each rectangle in the breakoutRects group.
    # If a ball hits one of the rectangles, remove it from the group and set
    # ball.dy to -ball.dy so it reverses direction.
    ### Place Your Code Here ###
    for rectangles in breakoutRects:
        if (ball.hitsShape(rectangles) == True):
            breakoutRects.remove(rectangles)
            ball.dy = -ball.dy
        
    # If the ball's center goes off the bottom of the canvas, draw a game over
    # message and use app.stop() to stop the game.
    ### (HINT: Lose the game and then use the inspector to draw the
    #          correct message.)
    ### Place Your Code Here ###
    if (ball.centerY >= 400):
            Label('GAME-OVER!', 200, 200, fill='white', font='arial', size=50)
            app.stop()

