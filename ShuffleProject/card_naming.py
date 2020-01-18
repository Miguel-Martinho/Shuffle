import pygame
import buttondraw
import random

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
        self.index = 1

    def draw(self,win,outline):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, self.outline, (self.x,self.y,self.width+4,self.height+4),2)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),self.outline)

    def __repr__(self):
        return f"{self.color} {self.index}"

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

def get_deck():
    deck = []
    for dx in range(0, 4):
        for dy in range(0, 3):
            deck.append(Card((0,200,100), x+width*dx+(dx*10), y+height*dy+(dy*10), width, height, outline, 0))
    return deck 

class Circle():
    def __init__(self, color, x,y, radius, outline, index):
        self.color = color
        self.x = Card.x
        self.y = Card.y
        self.radius = radius
        self.index = index

    def draw(self,win):
        #Call this method to draw the button on the screen
        pygame.draw.circle(win, (100,100,100), 475, 160, 80)


class Triangle():
    def __init__(self, color, points, outline):
        self.color = color
        self.points = points()
        self.outline = outline

    def draw(self,win):
        #Call this method to draw the button on the screen
        pygame.draw.polygon(win, (200,200,0), ((475, 140), (435,210), (515, 210)))

#dois arrays 1 com cartas e 1 com shapes, cartas.append(shapes)


class Square():
    def __init__(self, color, x,y,width,height, outline):
        self.color = color
        self.x = Card.x
        self.y = Card.y
        self.width = width
        self.height = height
        self.outline = outline

    def draw(self,win,outline):
        #Call this method to draw the button on the screen
        pygame.draw.rect(win, (100,100,100), (400,100), (200,200), 0)