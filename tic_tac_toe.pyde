def setup():
   # window size and color
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

#Keeps track of who wins. N stands for nobody. If X wins, win = "X", and if O wins, win = "O"
win = "N"

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
                    text("X", 0.5*xValues[x+1]+0.5*xValues[x], 0.5*yValues[y+1]+0.5*yValues[y])
                    squarePlaced[3*x+y] += 1
                    columnCount[x] += 1
                    rowCount[y] += 1
                    if x == y:
                        diCount[0] += 1
                    elif x+y == 2:
                        diCount[1] += 1
                    player = "O"
                elif player == "O":
                    text("O", 0.5*xValues[x+1]+0.5*xValues[x], 0.5*yValues[y+1]+0.5*yValues[y])
                    squarePlaced[3*x+y] = -1
                    columnCount[x] -= 1
                    rowCount[y] -= 1
                    if x == y:
                        diCount[0] -= 1
                    elif x+y == 2:
                        diCount[1] -= 1
    
                    player = "X"
           



def winScreen():
    global win
    for x in range(256):
        background(0, x)
    for c in range(256):
        fill(255, c)
        text(win + " Wins.")
    
    
        
    
    
def draw():
    global rowCount, columnCount, diCount, win
    for a in rowCount:
        if a == 3:
            win = "X"
            winScreen()
        elif a == -3:
            win = "O"
            winScreen()
    for b in columnCount:
        if b == 3:
            win = "X"
            winScreen()
        elif b == -3:
            win = "O"
            winScreen()
    for c in diCount:
        if c == 3:
            win = "X"
            winScreen()
        elif c == -3:
            win = "O"
            winScreen()
        
