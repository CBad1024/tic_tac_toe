from Button import PlayAgainButton, PlayButton, StatsButton, LeaderBoard
from Screen import StartScreen, GridScreen, PlayerSelectScreen, StatsScreen
from Player import Player
from Score import Score


    
#Define global variables

#If play has begun yet
playerSelected = False
playStarted = False
score = Score()
winnerAnnounced = False
scorefile = "leaderboard.txt"

def setup():
    # window size and color
    size(DIMENSION,DIMENSION)
    background(0)
    textSize(DIMENSION/6)
    textAlign(CENTER)
    frameRate(4)
    startScreen.display()


#Square dimensions
DIMENSION = 600
#Values which deetermine where to place the Xs and Os on the screen, as well as acting as values which, when plugged into an equation, allow us to map each X or O to a value in squarePlaced
offset = DIMENSION/3

#Keeps track of who wins. N stands for nobody. If X wins, winner = "X", and if O wins, winner = "O"
winner = "N"

player = Player("X")


# Define all Buttons
playButton = PlayButton(offset)
playAgainButton = PlayAgainButton(offset)
statsButton = StatsButton(offset)
leaderBoardButton = LeaderBoard(offset)



# Define all  screens
startScreen = StartScreen(DIMENSION, DIMENSION, DIMENSION, leaderBoardButton) # Screen 1
playerScreen = PlayerSelectScreen(playButton, offset)  # Screen 2
gridScreen = GridScreen(offset) # Screen 3
statsScreen = StatsScreen(offset, score) # Screen 4
 



def mouseReleased():
    global playerSelected, playStarted
    
    # Mouse can be pressed and released in any of the screens, so let us include a check to see which screen is active 
    # and make decisions accordingly.
    
    if startScreen.isActive(): # Screen 1
        if leaderBoardButton.clicked(mouseX, mouseY):
            statsScreen.display()
        else:
            playerScreen.activate()
        startScreen.deactivate()
       
    elif playerScreen.isActive(): # Screen 2
        if playButton.clicked(mouseX, mouseY):
            playStarted = True
            playerScreen.deactivate()
            reset()
         
    elif gridScreen.isActive():
        if playStarted: ## redundant check
            if winner == "N": # No Winner found
                if gridScreen.tokenPlaced(mouseX, mouseY, player):
                    player.switch()
            
            else: # Winner Found or it is a Draw
                if playAgainButton.clicked(mouseX, mouseY):
                    reset()
                elif statsButton.clicked(mouseX, mouseY):
                    statsScreen.display()
                    gridScreen.deactivate()
        
    elif statsScreen.isActive():
        statsScreen.deactivate()
        reset()

def reset():
    global winner, player, gridScreen, winnerAnnounced, playStarted
    playStarted = True
    gridScreen = GridScreen(offset)
    gridScreen.display()
    
    #initialize values
    winner = "N"
    player = Player("X")
    winnerAnnounced = False

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
    playAgainButton.display()
    statsButton.display()
    
        
def randomColor():
    fill(random(255), random(255), random(255))
    
def checkTie(): 
    global winner   
    if winner == "N": # no winner found
        if  not ( 0 in gridScreen.squarePlaced):
        # this is a tie : no more empty squares
            winner = "D"  # Draw 
                
def announceWinner():
    
    global winnerAnnounced
    if gridScreen.isActive():
        if not winnerAnnounced:
            score.computeScore(winner)
        
        if winner == "X" or winner == "O": # winner found
            winScreen(str(winner) + " wins")
            winnerAnnounced = True
        elif winner == "D":
            winScreen("DRAW") 
            winnerAnnounced = True

def draw():
    if startScreen.isActive():
        startScreen.display()

    if playerScreen.isActive():
        playerScreen.display()
    
    determineWinner()
    
    checkTie()
    
    announceWinner()
    
    








# XtypeNameBounds = [0.75*offset, 1.25*offset, 1.83*offset, 2.16*offset]
# OtypeNameBounds = [1.75*offset, 2.25*offset, 1.83*offset, 2.16*offset]

# playerX = ""
# playerO = ""    
        
# def keyTyped():
#     global playerX, playerO
#     if withinBounds(mouseX, 0, XtypeNameBounds) and withinBounds(mouseY, 2, XtypeNameBounds): 
#         if key > 31 and key != CODED:
#             playerX = playerX + key
                    
#     if withinBounds(mouseX, 0, OtypeNameBounds) and withinBounds(mouseY, 2, OtypeNameBounds):
#         if key > 31 and key != CODED:
#             playerO = playerO + key
                    
    
# def withinBounds(mPos, n, bounds):
#         return mPos > bounds[n] and mPos < bounds[n+1]

    
        
