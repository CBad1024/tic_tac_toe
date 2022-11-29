
def setup():
    global player, token
   # window size and color
    size(DIMENSION,DIMENSION)
    background(0)
    textSize(DIMENSION/6)
    textAlign(CENTER)
    reset()
    player = "X"


    
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
tokenColor = xColor

#Values which deetermine where to place the Xs and Os on the screen, as well as acting as values which, when plugged into an equation, allow us to map each X or O to a value in squarePlaced
offset = DIMENSION/3
bounds = [0, offset, 2*offset, 3*offset]
#switches player for every valid mouse released
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
    global token, bounds, squarePlaced, columnCount, diCount, rowCount, tokenColor
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
    global player, squarePlaced, rowCount, columnCount, diCount
    
    if winner == "N":
    
        #For loop and if statement that checks where mouse is released and whether the square which the mouse was released on is already filled  
        for x in range(3):
            for y in range(3):
                if withinBounds(mouseX, x) and withinBounds(mouseY, y) and emptySquare(x, y):
                    placeToken(player, x, y)
    else:
        if popupClicked():
            reset()
            
def popupClicked():
    return mouseX > width/2-0.375*offset and mouseX < width/2+0.375*offset and mouseY > 1.875*offset and mouseY < 2.125*offset 



def reset():
    global winner, squarePlaced, rowCount, columnCount, diCount, player, tokenColor, xColor, oColor, token
    background(0)
    # lines, size, and color 
    stroke(255)
    strokeWeight(5)
    #Line column 1
    line(offset,0,offset,height)
    #Line column 2
    line(2*offset,0,2*offset,height)
    #Line row 1
    line(0,offset,width,offset)
    #Line row 2
    line(0,2*offset,width,2*offset)
    winner = "N"
    squarePlaced = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    rowCount = [0, 0, 0]
    columnCount = [0, 0, 0]
    diCount = [0, 0]
    player = "X"
    tokenColor = xColor
    token = 1
    textSize(100)


                
def withinBounds(mPos, n):
    global bounds
    return mPos > bounds[n] and mPos < bounds[n+1]

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
    return winner

def winScreen(n):
    global tokenColor
    if n != "N":
        rectMode(CENTER)
        fill(0)
        stroke(255)
        rect(width/2, height/2, 1.5*offset, 0.5*offset)
        
        textAlign(CENTER)
    
        randomColor()
        textSize(100)
        text(winner + " Wins", width/2, height/2+offset/10)
        
        fill(30, 0, 255)
        rect(width/2, 2*offset, 0.75*offset, 0.25*offset)
        textSize(20)
        fill(255)
        text("PLAY AGAIN", width/2, 2*offset)
        
def randomColor():
    fill(random(100,255), random(100,255), random(100,255))
    
    
        
    
def draw():
    global rowCount, columnCount, diCount, winner
    for tokenCount in rowCount:
        determineWinner(tokenCount)
        print(rowCount)
    for tokenCount in columnCount:
        determineWinner(tokenCount)
        print(columnCount)
    for tokenCount in diCount:
        determineWinner(tokenCount)
        print(diCount)
    winScreen(winner)
        
    
