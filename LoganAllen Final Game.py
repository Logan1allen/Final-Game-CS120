import pygame, simpleGE, random
pygame.init()


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
        
        self.sprites = [
            self.btnLeft,
            self.btnRight,
            self.btnLleft,
            self.btnLright
            ]
        

        
        
#class instructions(simpleGE.Scene):
    
        
def main():
    
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()