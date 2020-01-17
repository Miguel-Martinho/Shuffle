import pygame
import buttondraw

x = 420
y = 100
height = 160
width = 110
outline = 0

class Card():
    def __init__(self, color, x,y,width,height, outline, index):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.outline = outline
        self.index = index
        ##self.shape = Shape

    def draw(self,win,outline):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.circle(win, (100,100,100), 475, 160, 80)
            pygame.draw.rect(win, self.outline, (self.x,self.y,self.width+4,self.height+4),2)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),self.outline)

    def __repr__(self):
        return f"{self.color} {self.outline}"

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False


class shape():
    def __init__(self, triangle, circle, square, color):
        self.triangle = triangle
        self.circle = circle
        self.square = square
        self.color = color

def get_shape():
    compendium= []
    for i in range(0, 2):
        compendium.append(circle)
        compendium.append(square)
        compendium.append(triangle)

def get_deck():
    deck = []
    for dx in range(0, 4):
        for dy in range(0, 3):
            deck.append(Card((0,200,100), x+width*dx+(dx*10), y+height*dy+(dy*10), width, height, outline,dx+dy))
    return deck 