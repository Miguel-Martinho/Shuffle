import pygame
from buttondraw import *
from card_naming import *

pygame.init()

black = (0,0,0)
white = (255,255,255)
yellow = (255, 255, 0,)
green = (0,255,0)
myimage = pygame.image.load("shuffle.png")
imagerect = (210,-50)
res = [1280, 720]
card_x = 0
card_y= 0
deck = []

gameDisplay = pygame.display.set_mode((res))
gameDisplay.blit(myimage, imagerect)

yellowbutton4x3 = button(yellow, 560, 250, 125, 30, '4x3')
yellowbutton4x4 = button(yellow, 560, 290, 125, 30, '4x4')
yellowbutton5x4 = button(yellow, 560, 330, 125, 30, '5x4')
yellowbutton6x5 = button(yellow, 560, 370, 125, 30, '6x5')
yellowbutton6x6 = button(yellow, 560, 410, 125, 30, '6x6')
exitbutton = button(yellow, 560, 480, 125, 30, 'EXIT')
exitbutton2 = button(yellow, 50, 660, 125, 30, 'EXIT')

def main_menu_draw():
    yellowbutton4x3.draw (gameDisplay, (0,0,0))
    yellowbutton4x4.draw (gameDisplay, (0,0,0))
    yellowbutton5x4.draw (gameDisplay, (0,0,0))
    yellowbutton6x5.draw (gameDisplay, (0,0,0))
    yellowbutton6x6.draw (gameDisplay, (0,0,0))
    exitbutton.draw (gameDisplay, (0,0,0))
    exitbutton2.draw (gameDisplay, (0,0,0))

def mouse_over_check(pos):
    if yellowbutton4x3.isOver(pos):
        yellowbutton4x3.color = white
        main_menu_draw
    else:
        yellowbutton4x3.color = yellow
        main_menu_draw
    if yellowbutton4x4.isOver(pos):
        yellowbutton4x4.color = white
        main_menu_draw
    else:
        yellowbutton4x4.color = yellow
        main_menu_draw
    if yellowbutton5x4.isOver(pos):
        yellowbutton5x4.color = white
        main_menu_draw
    else:
        yellowbutton5x4.color = yellow
        main_menu_draw
    if yellowbutton6x5.isOver(pos):
        yellowbutton6x5.color = white
        main_menu_draw
    else:
        yellowbutton6x5.color = yellow
        main_menu_draw
    if yellowbutton6x6.isOver(pos):
        yellowbutton6x6.color = white
        main_menu_draw
    else:
        yellowbutton6x6.color = yellow
        main_menu_draw

def get_deck():
    deck = []
    j= 0
    for dx in range(0, 4):
        for dy in range(0, 3):
            deck.append(Card((0,255,0), x+width*dx, y+height*dy, width, height, 0))
    return deck 

def playcardgame4x4():
    get_deck(card_x, card_y)

    for card in deck:
        card.draw (gameDisplay, (0,0,0))

    if event.type == pygame.MOUSEMOTION:
        if card.isOver(pos):
            card.color = white
            for card in deck:
                card.draw (gameDisplay, (0,0,0))
            
    exitbutton2.draw (gameDisplay, (0,0,0))


def playcardgame5x4():
    get_deck(card_x, card_y)
    for card in deck:
        card.draw (gameDisplay, (0,0,0))
    if event.type == pygame.MOUSEMOTION:
        if card.isOver(pos):
            card.color = white
            for card in deck:
                card.draw (gameDisplay, (0,0,0))
            
    exitbutton2.draw (gameDisplay, (0,0,0))


pygame.display.set_caption('Shuffle')
clock = pygame.time.Clock()
crashed = False
gamescreen = False
while not crashed:

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            crashed = True
        
        if event.type == pygame.MOUSEMOTION and gamescreen == False:
            mouse_over_check(pos)
            main_menu_draw()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if yellowbutton4x3.isOver(pos):
                gamescreen = True
                card_x = 4
                card_y = 3
                deck = get_deck()
                print(deck[1])
                while (gamescreen == True):
                    gameDisplay.fill(black)
                    print(len(deck))
                    for card in deck:
                        card.draw (gameDisplay, (0,0,0))
                    if event.type == pygame.MOUSEMOTION:
                        if card.isOver(pos):
                            card.color = white
                            for card in deck:
                                card.draw (gameDisplay, (0,0,0))
                    exitbutton2.draw (gameDisplay, (0,0,0))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if exitbutton2.isOver(pos):
                            gamescreen = False

            if yellowbutton4x4.isOver(pos):
                gameDisplay.fill(black)
                card_x = 4
                card_y = 4
                playcardgame4x4()
                gamescreen = True
            if yellowbutton5x4.isOver(pos):
                gameDisplay.fill(black)
                card_x = 5
                card_y = 4
                playcardgame5x4()
                gamescreen = True
            if exitbutton.isOver(pos):
                quit()


    pygame.display.flip()

print(event)


#pygame.display.update()
clock.tick(60)
