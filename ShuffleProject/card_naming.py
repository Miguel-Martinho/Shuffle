import pygame
from buttondraw import *
import random

outline = 0

class Card():
    def __init__(self, color, x,y,width,height, outline, index, flipped):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.outline = outline
        self.index = index
        self.flipped = 0
        self.ingame = True
        self.text = " "

    def draw(self, win, outline=None, flipped=None, ingame=None):
        if self.ingame == True:
            if self.flipped == 1:
                pygame.draw.rect(win, (0, 200, 100), (self.x,self.y,self.width,self.height),outline)
                if self.text != '':
                    font = pygame.font.SysFont('NotoSans-Regular.ttf', 30)
                    text = font.render(self.text, 1, (255,255,0))
                    win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

            else:    
                pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height)) 

    def __repr__(self):
        return f"{self.index} {self.outline}"

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True
            
        return False

def get_deck(cardinx, cardiny):
    x = 420
    y = 100
    height = 160
    width = 110
    if cardinx == 4 and cardiny == 4:
        y = 30
    if cardinx == 5:
        height = 120
        width = 80
    if cardinx == 6:
        y = 50
        height = 120
        width = 80
        if cardiny == 6:
            height = 100
            width = 70
    deck = []
    for dx in range(0, cardinx):
        for dy in range(0, cardiny):
            deck.append(Card((0,200,100), x+width*dx+(dx*10), y+height*dy+(dy*10), width, height, outline, 0, 0))
    return deck