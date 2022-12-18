class Screen(object):
    
    # Buttons can be a list of buttons
    
    # TextInfo can be a list of TextInfo objects on the screen
        
    def __init__(self, bColor, buttons, textInfo):
        self.bColor = bColor
        self.buttons = buttons
        self.textInfo = textInfo
        
    def display(self):
        background(self.bColor)
        for txt in self.textInfo:
            txt.display()
        
        for button in self.buttons:
            button.display()
            
class StartScreen(object):
            
    def display(self):
        background(0)
        textSize(DIMENSION/14)
        fill(0, 255, 0)
        text("TIC TAC TOE", width/2, height/4)
        textSize(DIMENSION/18)
        text("Click anywhere to start...", width/2, height/2)

class PlayerSelectScreen(object):
    
    def __init__(self, button):
        self.button = button
    
    def display(self):
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
        text(playerX, offset, 2*offset)
        text(playerO, 2*offset, 2*offset)
        ## Call Play Button
        # btn = PlayButton(offset)
        self.button.display()

class GridScreen(object):
    
    rowCount = [0,0,0]
    columnCount = [0,0,0]
    diCount = [0,0]
    
    # This is a 3 by 3 grid screen
    squarePlaced = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    activePlay = False
    token = 1


    def __init__(self, offset):
        self.offset = offset
        self.bounds = [0, offset, 2*offset, 3*offset]


    def tokenPlaced(self, mxPos, myPos, player):
        for x in range(3):
            for y in range(3):
                if withinBounds(mxPos, x) and withinBounds(myPos, y) and emptySquare(x, y):
                    placePlayer(player, x, y)
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
        return squarePlaced[3*x+y] == 0  
    
    def display(self, offset):
        background(0)
    
        # lines, size, and color 
        stroke(255)
        strokeWeight(5)
    
        line(offset,0,offset,height)     #Line column 1
        line(2*offset,0,2*offset,height) #Line column 2
        line(0,offset,width,offset)  #Line row 1
        line(0,2*offset,width,2*offset)   #Line row 2        
        
    def withinBounds(self, mPos, n):
        return mPos > self.bounds[n] and mPos < self.bounds[n+1]
        
