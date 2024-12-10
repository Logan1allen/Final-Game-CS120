import pygame, simpleGE, random
pygame.init()


class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("brick.png")
        backgroundnoise = simpleGE.Sound("crickets.MP3")
        backgroundnoise.play()
        
        self.btnLeft = simpleGE.Button()
        self.btnLeft.text = "Go Left"
        self.btnLeft.center = (100,400)
        
        self.btnRight = simpleGE.Button()
        self.btnRight.text = "Go Right"
        self.btnRight.center = (540,400)
        
        self.btnLleft = simpleGE.Button()
        self.btnLleft.text = "Listen"
        self.btnLleft.center = (100, 450)
        
        self.btnLright = simpleGE.Button()
        self.btnLright.text = "Listen"
        self.btnLright.center = (540, 450)
        
        self.dangerLeft = random.randint(1,2)
        print(f"{self.dangerLeft}")
        
        self.dangerRight = random.randint(3,4)
        
        if self.dangerLeft == 2:
            self.dangerRight = 1
        if self.dangerLeft == 1:
            self.dangerRight = 2
        
        
        self.score = 0
        self.lblScore = LblScore()
        
        
        self.sprites = [
            self.btnLeft,
            self.btnRight,
            self.btnLleft,
            self.btnLright,
            self.lblScore
            ]
        
    def process(self):
        if self.dangerLeft == 2:
            if self.btnLeft.clicked:
                self.response = "Go Left"
                self.stop()
            if self.btnLleft.clicked:
                self.response = "Listen"
                breathing = simpleGE.Sound("breathing.MP3")
                breathing.play()
        
        if self.dangerLeft == 1:
            if self.btnLeft.clicked:
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
                self.dangerLeft = random.randint(1,2)
                self.dangerRight = random.randint(3,4)
                if self.dangerLeft == 2:
                    self.dangerRight = 1
                if self.dangerLeft == 1:
                    self.dangerRight = 2
                
        if self.dangerRight == 2:
            if self.btnRight.clicked:
                self.response = "Go Right"
                self.stop()
            if self.btnLright.clicked:
                self.response = "Listen"
                breathing = simpleGE.Sound("breathing.MP3")
                breathing.play()
                
        if self.dangerRight == 1:
            if self.btnRight.clicked:
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
                self.dangerLeft = random.randint(1,2)
                self.dangerRight = random.randint(3,4)
                if self.dangerLeft == 2:
                    self.dangerRight = 1
                if self.dangerLeft == 1:
                    self.dangerRight = 2

        
        
class Instructions(simpleGE.Scene):
    def __init__(self, prevScore):
        super().__init__()
        
        self.prevScore = prevScore

        self.setImage("brick.png")
        self.response = "Quit"
        
        self.directions = simpleGE.MultiLabel()
        self.directions.textLines = [
        "Listen Carefully",
        "You are not alone",
        "Find the Right Path",
        "Do not choose incorrectly"
            ]
        self.directions.center= (320, 240)
        self.directions.size = (500, 250)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100,400)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (540,400)
        
        self.lblScore = simpleGE.Label()
        self.lblScore.text = "Last Score: 0"
        self.lblScore.center = (320, 400)
        self.lblScore.text = f"Last Score: {self.prevScore}"
        
        self.sprites = [self.directions,
                        self.btnPlay,
                        self.btnQuit,
                        self.lblScore]
        
    def process(self):
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
                
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
        
        
def main():
    
    keepGoing = True
    lastScore = 0
    
    while keepGoing:
        instructions = Instructions(lastScore)
        instructions.start()
        
        if instructions.response == "Play":
            game = Game()
            game.start()
            lastScore = game.score
        else:
            keepGoing = False
    
if __name__ == "__main__":
    main()