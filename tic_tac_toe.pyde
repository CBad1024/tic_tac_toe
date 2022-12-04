
def setup():
    # window size and color
    size(DIMENSION,DIMENSION)
    background(0)
    textSize(DIMENSION/6)
    textAlign(CENTER)
    frameRate(4)
    grid()

    
#Define global variables

#Square dimensions
DIMENSION = 600

#list which stores the values of each square (0 means nothing in the square, +1 is an X in the square, -1 is an o in the square)
squarePlaced = [0, 0, 0, 0, 0, 0, 0, 0, 0]

#Total value of +1 (x) and -1 (o) in a given row or column, going from left to right, top to bottom, and for the diagonals, the one going from top left ot bottom right is index 0 and the one going from bottom left to top right is index 1.
rowCount = [0,0,0]
columnCount = [0,0,0]
diCount = [0,0]

#Keeps track of who wins. N stands for nobody. If X wins, winner = "X", and if O wins, winner = "O"
winner = "N"

# counter that changes the player from x to o every turn
player = "X"
token = 1
xColor = "#F0B905"
oColor = "#0AF0D3"
tokenColor = xColor # initial Color for "X" token

#Values which deetermine where to place the Xs and Os on the screen, as well as acting as values which, when plugged into an equation, allow us to map each X or O to a value in squarePlaced
offset = DIMENSION/3

# Grid bounds
bounds = [0, offset, 2*offset, 3*offset]

# Button bounds
playAgainBtnBounds = [0.625*offset, 1.375*offset, 1.875*offset, 2.125*offset]
statsBtnBounds = [1.625*offset, 2.375*offset, 1.875*offset, 2.125*offset]


# Define helper functions

def switchPlayer():
    global player, token, tokenColor
    
    if player == "X":
        player = "O"
        tokenColor = oColor
    else:
        player = "X"
        tokenColor = xColor
    token *= -1

def placeToken(activePlayer, x, y):
    global squarePlaced, columnCount, diCount, rowCount
    textSize(DIMENSION/6)
    fill(tokenColor)
    text(activePlayer, (bounds[x+1]+bounds[x])/2, (bounds[y+1]+bounds[y])/2)
    squarePlaced[3*x+y] = token
    columnCount[x] += token
    rowCount[y] += token
    if x == y:
        diCount[0] += token
    if x+y == 2:
        diCount[1] += token
    switchPlayer()

def mouseReleased():
    
    if winner == "N":
        #For loop and if statement that checks where mouse is released and whether the square which the mouse was released on is already filled  
        for x in range(3):
            for y in range(3):
                if withinBounds(mouseX, x, bounds) and withinBounds(mouseY, y, bounds) and emptySquare(x, y):
                    placeToken(player, x, y)        
    else: # Winner Found or it is a Draw
        if playAgainClicked(): # Check if PlayAgain is Clicked
            reset()
            
def playAgainClicked():
    return withinBounds(mouseX,0, playAgainBtnBounds) and withinBounds(mouseY,2, playAgainBtnBounds)

def statsClicked():
    return withinBounds(mouseX,0, statsBtnBounds) and withinBounds(mouseY,2, statsBtnBounds)

def withinBounds(mPos, n, bounds):
    return mPos > bounds[n] and mPos < bounds[n+1]

def grid():
    background(0)
    
    # lines, size, and color 
    stroke(255)
    strokeWeight(5)

    line(offset,0,offset,height)     #Line column 1
    line(2*offset,0,2*offset,height) #Line column 2
    line(0,offset,width,offset)  #Line row 1
    line(0,2*offset,width,2*offset)   #Line row 2

def reset():
    global winner, squarePlaced, rowCount, columnCount, diCount, player, tokenColor, token
    
    grid()
    
    #initialize values
    winner = "N"
    squarePlaced = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    rowCount = [0, 0, 0]
    columnCount = [0, 0, 0]
    diCount = [0, 0]
    player = "X"
    tokenColor = xColor
    token = 1

def emptySquare(x, y):
    global squarePlaced
    return squarePlaced[3*x+y] == 0

def determineWinner(n):
    global winner
    
    if winner == "N":
        if n == 3:
            winner = "X"
        elif n == -3:
            winner = "O"
    if winner == "STOP":
        pass
    
    return winner

def winScreen(message):
    rectMode(CENTER)
    fill(0)
    stroke(255)
    rect(width/2, height/2, 1.5*offset, 0.5*offset)
    textSize(DIMENSION/6)
    randomColor()
    textAlign(CENTER)
    text(message, width/2, height/2+offset/10)
    playAgain()
    leaderboard()

def playAgain():    
        fill(30, 0, 255)
        rect(offset, 2*offset, 0.75*offset, 0.25*offset)
        textSize(DIMENSION/30)
        fill(255)
        text("PLAY AGAIN", offset, 2*offset)
        textSize(DIMENSION/6) ## reset the text size
        
def randomColor():
    fill(random(255), random(255), random(255))
    
def checkTie(): 
    global winner   
    if winner == "N": # no winner found
        if  not ( 0 in squarePlaced):
        # this is a tie : no more empty squares
            winner = "D"  # Draw 
        

def statsScreen():
    if mousePressed:
        background(0)
        textSize(DIMENSION/12)
        text("Type your name below:", width/2, offset/2)
def leaderboard(): 
    global squarePlaced, winner
    fill(150)
    textSize(DIMENSION/30)
    rect(2*offset, 2*offset, 0.75*offset, 0.25*offset)
    fill(255)
    text("STATS", 2*offset, 2*offset)
    
    if winner != "N" and winner != "STOP": 
        f = createWriter("leaderboard.txt")
        f.print(winner)
        f.flush()
        f.close
    if statsClicked() and mousePressed:
        reset()
        winner = "STOP"
        squarePlaced = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
        statsScreen()
        r = createReader("leaderboard.txt")
        winStats = [r.readLine()]
        # for "X" in winStats:
        #     print("X")
        
        
  
    
    
def draw():
    for tokenCount in rowCount:
        determineWinner(tokenCount)

    for tokenCount in columnCount:
        determineWinner(tokenCount)

    for tokenCount in diCount:
        determineWinner(tokenCount)
        

    checkTie()
    
    if winner == "X" or winner == "O": # winner found
        winScreen(str(winner) + " wins")
    elif winner == "D":
        winScreen("DRAW")
    
    
        
