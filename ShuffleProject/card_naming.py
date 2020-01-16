import pygame
import buttondraw

x = 475
y = 100
height = 160
width = 110

class Card():
    def __init__(self, color, x,y,width,height, index):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.index = index
def __repr__(self):
    return f"{self.color} {self.x}"

    def draw(self,win,outline = None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4), self.index)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height), self.index)

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

def get_deck(card_x, card_y):
    deck = []
    j= 0
    for dx in range(0, 4):
        for dy in range(0, 3):
            deck.append(Card((0,255,0), x+width*dx, y+height*dy, width, height, 0))
    return deck 