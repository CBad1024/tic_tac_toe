def setup():
   # winnerdow size and color
    size(600,600)
    background(0)
    
    # lines, size, and color 
    stroke(255)
    strokeWeight(5)
    line(200,0,200,600)
    line(400,0,400,600)
    line(0,200,600,200)
    line(0,400,600,400)
    
# counter that changes the player from x to o every turn
player = "X"
#list which stores the values of each square (0 means nothing in the square, +1 is an X in the square, -1 is an o in the square)
squarePlaced = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#Total value of +1 (x) and -1 (o) in a given row or column, going from left to right, top to bottom, and for the diagonals, the one going from top left ot bottom right is index 0 and the one going from bottom left to top right is index 1.
rowCount = [0,0,0]
columnCount = [0,0,0]
diCount = [0,0]

#Keeps track of who winners. N stands for nobody. If X winners, winner = "X", and if O winners, winner = "O"
winner = "N"



def placeToken(activePlayer, x, y):
    text("X", (xValues[x+1]+xValues[x])/2, (yValues[y+1]+yValues[y])/2)
    squarePlaced[3*x+y] += 1
    columnCount[x] += 1
    rowCount[y] += 1
    if x == y:
        diCount[0] += 1
    elif x+y == 2:
        diCount[1] += 1
    switchPlayer()

def mouseReleased():
    global player, squarePlaced, rowCount, columnCount, diCount
    fill(255)
    textSize(100)
    textAlign(CENTER)
    #Values which deetermine where to place the Xs and Os on the screen, as well as acting as values which, when plugged into an equation, allow us to map each X or O to a value in squarePlaced
    xValues = [0, 200, 400, 600]
    yValues = [0, 200, 400, 600]
    
    #For loop and if statement that checks where mouse is released and whether the square which the mouse was released on is already filled  
    for x in range(len(xValues)-1):
        for y in range(len(yValues)-1):
            if mouseX < xValues[x+1] and mouseY < yValues[y+1] and mouseX > xValues[x] and mouseY > yValues[y] and squarePlaced[3*x+y] == 0:
                if player == "X":
                    placeToken
                elif player == "O":
                    text("O", (xValues[x+1]+xValues[x])/2, (yValues[y+1]+yValues[y])/2)
                    squarePlaced[3*x+y] = -1
                    columnCount[x] -= 1
                    rowCount[y] -= 1
                    if x == y:
                        diCount[0] -= 1
                    elif x+y == 2:
                        diCount[1] -= 1
    
                    player = "X"
           


def determineWinner(n):
    global winner
    if winner == "N":
        if n == 3:
            winner = "X"
        elif n == -3:
            winner = "O"
    return winner

def winScreen(n):
    if n != "N":
        rectMode(CENTER)
        fill(0)
        stroke(255)
        rect(width/2, height/2, 300, 100)
        textAlign(CENTER, CENTER)
        fill(255)
        text(winner + " Wins.", width/2+5, height/2-10)
    
    
        
    
    
def draw():
    global rowCount, columnCount, diCount, winner
    for a in rowCount:
        determineWinner(a)
    for b in columnCount:
        determineWinner(b)
    for c in diCount:
        determineWinner(c)
    winScreen(winner)
        
    
