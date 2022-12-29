from Button import PlayAgainButton, PlayButton, StatsButton
from Screen import StartScreen, GridScreen, PlayerSelectScreen
from Player import Player

def setup():
    # window size and color
    size(DIMENSION,DIMENSION)
    background(0)
    textSize(DIMENSION/6)
    textAlign(CENTER)
    
    

    
#Define global variables

#If play has begun yet
playStarted = False
playerSelected = False
play = False





#Square dimensions
DIMENSION = 600
#Values which deetermine where to place the Xs and Os on the screen, as well as acting as values which, when plugged into an equation, allow us to map each X or O to a value in squarePlaced
offset = DIMENSION/3

#Keeps track of who wins. N stands for nobody. If X wins, winner = "X", and if O wins, winner = "O"
winner = "N"

player = Player("X")


playButton = PlayButton(offset)
gridScreen = GridScreen(offset)
playAgainButton = PlayAgainButton(offset)

XtypeNameBounds = [0.75*offset, 1.25*offset, 1.83*offset, 2.16*offset]
OtypeNameBounds = [1.75*offset, 2.25*offset, 1.83*offset, 2.16*offset]


leaders = []


# Define helper functions
def showStartScreen():
    global playerSelected
    StartScreen(DIMENSION, height, width).display()
    if mousePressed:
        println("Called ###")
        playerSelected = True
        reset()
            

playerScreen = PlayerSelectScreen(playButton, offset)  


def showPlayerSelectScreen():
    if playerSelected and not play:
        playerScreen.display()
        

playerX = ""
playerO = ""    
        
def keyTyped():
    global playerX, playerO
    if withinBounds(mouseX, 0, XtypeNameBounds) and withinBounds(mouseY, 2, XtypeNameBounds): 
        if key > 31 and key != CODED:
            playerX = playerX + key
                    
    if withinBounds(mouseX, 0, OtypeNameBounds) and withinBounds(mouseY, 2, OtypeNameBounds):
        if key > 31 and key != CODED:
            playerO = playerO + key
                    
    
def withinBounds(mPos, n, bounds):
        return mPos > bounds[n] and mPos < bounds[n+1]



def mouseReleased():
    println("Called***")

    if play:
        println("Called!!!")
        if winner == "N":
            if gridScreen.tokenPlaced(mouseX, mouseY, player):
                player.switch()
        
        else: # Winner Found or it is a Draw
            # f = createWriter("leaderboard.txt")
            # f.print(winner)
            # f.flush()
            # f.close()
            
            if playAgainButton.clicked(mouseX, mouseY):
                reset()

    else:
        println("Called here")
        if playButton.clicked(mouseX, mouseY):
            play = True
            reset()


def statsClicked():
    return withinBounds(mouseX,0, statsBtnBounds) and withinBounds(mouseY,2, statsBtnBounds)


def reset():
    global winner, player, gridScreen
    println("Inside reset")
    
    gridScreen.reset()
    gridScreen.display()
    
    #initialize values
    winner = "N"
    player = Player("X")

def determineWinner():
    for tokenCount in gridScreen.rowCount:
        findWinner(tokenCount)

    for tokenCount in gridScreen.columnCount:
        findWinner(tokenCount)

    for tokenCount in gridScreen.diCount:
        findWinner(tokenCount)

def findWinner(n):
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
        
def randomColor():
    fill(random(255), random(255), random(255))
    
def checkTie(): 
    global winner   
    if winner == "N": # no winner found
        if  not ( 0 in gridScreen.squarePlaced):
        # this is a tie : no more empty squares
            winner = "D"  # Draw 
        

def statsScreen():
    if mousePressed:
        background(0)
        textSize(DIMENSION/12)
        text("Leaderboard", width/2, offset/2)
        
def leaderboard(): 
    global squarePlaced, winner, leaders
    # Call Stats Button
    # fill(150)
    # textSize(DIMENSION/30)
    # rect(2*offset, 2*offset, 0.75*offset, 0.25*offset)
    # fill(255)
    # text("STATS", 2*offset, 2*offset)
    
    if winner != "N" and winner != "STOP": 
        if statsClicked() and mousePressed:
            reset()
            winner = "STOP"
            squarePlaced = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
            statsScreen()
            print(1)
            r = createReader("leaderboard.txt")
            for line in r:
                overallWinner = line.strip()
                leaders.append(overallWinner)
                print(leaders)
                
def announceWinner():
    if winner == "X" or winner == "O": # winner found
        winScreen(str(winner) + " wins")
    elif winner == "D":
        winScreen("DRAW")  
              
def draw():
    if not playerSelected:
        showStartScreen()
    
    if playerSelected:
        showPlayerSelectScreen()
    
    determineWinner()
    
    checkTie()
    
    announceWinner()
    
    
    
    
        
