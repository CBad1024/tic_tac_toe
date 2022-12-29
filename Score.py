class Score(object):
    
    fileName = "leaderboard.txt"
    
    def __init__(self):
        self.xWins = 0
        self.oWins = 0
        self.draws = 0
        self.readFile()
        
    def __repr__(self):
        return ("XWins: " + str(self.xWins) + " OWins: " + str(self.oWins) + " Draws: " + str(self.draws))

        
    def computeScore(self, player):
    
        if player in ("X", "O", "D"):
            if player == "X":
                self.xWins += 1
            elif player == "O":
                self.oWins += 1
            elif player == "D":
                self.draws += 1
            self.writeFile()

            
    def readFile(self):
        with open(self.fileName, 'r') as f:
            firstLine = f.readline()
            secondLine = f.readline()
            ## Data is in the second line
            scores = secondLine.split(',')
            self.xWins = int(scores[0])
            self.oWins = int(scores[1])
            self.draws = int(scores[2])
                
    def writeFile(self):
        with open(self.fileName, "w") as f:
            f.write("X,O,D\n")
            f.write(str(self.xWins)+ "," + str(self.oWins) + "," + str(self.draws) + "\n")

        
