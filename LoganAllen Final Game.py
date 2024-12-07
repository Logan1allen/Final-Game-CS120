import pygame, simpleGE, random
pygame.init()


class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("brick.png")
        backgroundnoise = simpleGE.Sound("crickets.MP3")
        backgroundnoise.play()
        self.sprites = [
            
            ]
        
        
def main():
    
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()