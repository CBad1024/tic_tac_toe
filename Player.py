class Player(object):
    
    def __init__(self, token):
        self.token = token
        self.setValues()

            
    def setValues(self):
        if self.token == "X":
            self.tColor = "#F0B905"
            self.tValue = 1
        else:
            self.tColor = "#0AF0D3"
            self.tValue = -1
        
    def display(self, x, y):
        textSize(DIMENSION/6)
        fill(self.tColor)
        text(self.token, x, y)
    
    def switch(self):
        self.token = "O" if tValue > 0 else "X"
        setValues()
