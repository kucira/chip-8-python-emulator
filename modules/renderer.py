import pygame
from modules.keyboard import Keyboard
import math

class Renderer:
    def __init__(self, scale) -> None:
        self.pygame = pygame
        self.cols = 64
        self.rows = 32
        self.scale = scale
        self.display = [0] * self.cols * self.rows

        pygame.init()
        self.screen = pygame.display.set_mode(((self.cols * scale, self.rows * scale)))
        self.clock = pygame.time.Clock()

        #test set pixel render
        self.setPixel(0, 0)
        self.setPixel(5, 2)

    def setPixel(self, x, y):
        if(x > self.cols):
            x -= self.cols
        elif(x < 0):
            x += self.cols
        
        if(y > self.rows):
            y -= self.rows
        elif(y < 0):
            y += self.rows

        pixelLoc = x + (y * self.cols)
        self.display[pixelLoc] ^= 1

        return not self.display[pixelLoc]


    def clear(self):
        self.display = [0] * self.cols * self.rows 
    
    def render(self):
        for i in range(self.cols * self.rows):
            x = (i % self.cols) * self.scale
            y = math.floor(i / self.cols) * self.scale

            if(self.display[i] == 1):
                pygame.draw.rect(self.screen, 0x000000, [x, y, self.scale, self.scale])

    def run(self, keyboard):
        running = True
        
        while running:
           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    print('keydown')
                    keyboard.keyDown(event.key)
  
                if event.type == pygame.KEYUP:
                    print('keyup')
                    keyboard.keyUp(event.key)


            self.clock.tick(60)
            self.screen.fill(0xffffff)
 
            self.render()

            pygame.display.flip()