class Button(object):
    
    def __init__ (self, offset):
        self.offset = offset
        self.bounds = [0,0,0,0]
        
    def clicked(self, mX, mY):
        return mX > self.bounds[0] and mX < self.bounds[1] and mY > self.bounds[2] and mY < self.bounds[3]
    
    def display(self):
        pass


class PlayAgainButton(Button):
    def __init__ (self, offset):
        super(PlayAgainButton, self).__init__(offset)
        self.bounds = [0.625*offset, 1.375*offset, 1.875*offset, 2.125*offset]
        self.value = "PLAY AGAIN"
    
    def display(self):
        DIMENSION = 600
        offset = self.offset
        fill(30, 0, 255)
        rect(offset, 2*offset, 0.75*offset, 0.25*offset)
        textSize(DIMENSION/30)
        fill(255)
        text(self.value, offset, 2*offset)

class StatsButton(Button):
    
    def __init__ (self, offset):
        super(StatsButton, self).__init__(offset)
        self.bounds = [1.625*offset, 2.375*offset, 1.875*offset, 2.125*offset]
        self.value = "STATS"
        
    def display(self):
        DIMENSION = 600
        offset = self.offset
        fill(150)
        textSize(DIMENSION/30)
        rect(2*offset, 2*offset, 0.75*offset, 0.25*offset)
        fill(255)
        text(self.value, 2*offset, 2*offset)

    
        
class LeaderBoard(Button):
    
    def __init__ (self, offset):
        super(LeaderBoard, self).__init__(offset)
        self.bounds = [offset, 2*offset, 1.75*offset, 2.25*offset]
        self.value = "Leaderboard"
        
    def display(self):
        DIMENSION = 600
        offset = self.offset
        fill(150)
        textSize(DIMENSION/30)
        rectMode(CENTER)
        rect(DIMENSION/2, 2*offset, offset, 0.5*offset)
        fill(255)
        text(self.value, DIMENSION/2, 2*offset)
            
class PlayButton(Button):
    
    def __init__(self, offset):
        # print("PLAY CALLED")
        super(PlayButton, self).__init__(offset)
        self.bounds = [1.25*offset, 1.75*offset, 1.75*offset, 2.25*offset]
        self.value = "PLAY."
        
    def display(self):
        offset = self.offset
        fill(30, 0, 255)
        rect(width/2, 2*offset, 0.5*offset, 0.25*offset)
        fill(255)
        text(self.value, width/2, 2*offset)
