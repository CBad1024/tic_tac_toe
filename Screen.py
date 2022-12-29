class Screen(object):
        
    def __init__(self):
        self.active = False
        
    def isActive(self):
        return self.active
    
    def deactivate(self):
        self.active = False
    
    def activate(self):
        self.active = True
            
class StartScreen(Screen):

    def __init__(self, dim, ht, wt, button):
        super(StartScreen, self).__init__()
        self.dim = dim
        self.ht = ht
        self.wt = wt
        self.button = button
            
    def display(self):
        background(0)
        textSize(self.dim/14)
        fill(0, 255, 0)
        text("TIC TAC TOE", self.wt/2, self.ht/4)
        textSize(self.dim/18)
        text("Click anywhere to start...", self.wt/2, self.ht/2)
        self.button.display()
        self.activate()


class StatsScreen(Screen):
    
    buttonsActive = False

    def __init__(self, offset, score):
        super(StatsScreen, self).__init__()
        self.offset = offset
        self.score = score
        
    def display(self):
        DIMENSION = 600
        background(0)
        textSize(DIMENSION/12)
        fill(0, 255, 0)
        text("Leaderboard", width/2, self.offset/2)
        # text(score, 200, 200)
        textSize(DIMENSION/20)
        
        fill("#F0B905")
        text("X Wins", DIMENSION/4, self.offset)
        text(str(self.score.xWins), DIMENSION/4, DIMENSION/2)
        
        fill("#0AF0D3")
        text("O Wins", DIMENSION/2, self.offset)
        text(str(self.score.oWins), DIMENSION/2, DIMENSION/2)
        
        fill(255)
        text("Draws", 3*DIMENSION/4, self.offset)
        text(str(self.score.draws), 3*DIMENSION/4, DIMENSION/2)
        
        textSize(DIMENSION/15)
        fill(0, 255, 0)
        text("Click Anywhere to continue...", DIMENSION/2, 2*self.offset)
        self.activate()
        
        
        

class PlayerSelectScreen(Screen):
    
    def __init__(self, button, offset):
        super(PlayerSelectScreen, self).__init__()
        self.button = button
        self.offset = offset
    
    def display(self):
        DIMENSION = 600
        offset = self.offset
        
        background(0)
        textSize(DIMENSION/14)
        fill(0, 255, 0)
        text("Type your names below", width/2, height/4)
        textSize(DIMENSION/18)
        text("Player X", offset, 2*offset + 100)
        text("Player O", 2*offset, 2*offset + 100)
        fill(255)
        rectMode(CENTER)
        rect(offset, 2*offset, offset/2, offset/3)
        rect(2*offset, 2*offset, offset/2, offset/3)
        fill(0)
        text("X", offset, 2*offset)
        text("O", 2*offset, 2*offset)
        ## Call Play Button
        # btn = PlayButton(offset)
        self.button.display()
        self.activate()

class GridScreen(Screen):

    def __init__(self, offset):
        super(GridScreen, self).__init__()
        self.offset = offset
        self.bounds = [0, offset, 2*offset, 3*offset]
        self.resetValues()        
        
    def resetValues(self):
        self.squarePlaced = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.rowCount = [0,0,0]
        self.columnCount = [0,0,0]
        self.diCount = [0,0]
        self.buttonsActive = False
        
    def tokenPlaced(self, mxPos, myPos, player):
        for x in range(3):
            for y in range(3):
                if self.withinBounds(mxPos, x) and self.withinBounds(myPos, y) and self.emptySquare(x, y):
                    self.placePlayer(player, x, y)
                    return True
        return False

   
    def placePlayer(self, player, x, y):
        player.display((self.bounds[x+1]+self.bounds[x])/2, (self.bounds[y+1]+self.bounds[y])/2)

        self.squarePlaced[3*x+y] = player.tValue
        self.columnCount[x] += player.tValue
        self.rowCount[y] += player.tValue
        if x == y:
            self.diCount[0] += player.tValue
        if x+y == 2:
            self.diCount[1] += player.tValue        
    
    def emptySquare(self, x, y):
        return self.squarePlaced[3*x+y] == 0  
    
    def display(self):
        offset = self.offset
        background(0)
    
        # lines, size, and color 
        stroke(255)
        strokeWeight(5)
    
        line(offset,0,offset,height)     #Line column 1
        line(2*offset,0,2*offset,height) #Line column 2
        line(0,offset,width,offset)  #Line row 1
        line(0,2*offset,width,2*offset)   #Line row 2  
        self.activate()

        
    def withinBounds(self, mPos, n):
        return mPos > self.bounds[n] and mPos < self.bounds[n+1]
        
