class TextInfo(object):
    
    def __init__(self, xPos, yPos, message, txtSize, txtColor):
        self.xPos = xPos
        self.yPos = yPos
        self.message = message
        self.txtSize = txtSize
        self.txtColor = txtColor # txtColor is a r, g, b
        
    def display(self):
        fill(self.txtColor[0], self.txtColor[1], self.txtColor[2])
        textSize(self.txtSize)
        text(message, xPos, yPos)
