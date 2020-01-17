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
deck = get_deck()
deck_flipped = []

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
    yellowbutton4x3.draw (gameDisplay)
    yellowbutton4x4.draw (gameDisplay)
    yellowbutton5x4.draw (gameDisplay)
    yellowbutton6x5.draw (gameDisplay)
    yellowbutton6x6.draw (gameDisplay)
    exitbutton.draw (gameDisplay)

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
    if exitbutton.isOver(pos):
        exitbutton.color = white
        main_menu_draw
    else:
        exitbutton.color = yellow
        main_menu_draw

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

        #mouse over dentro do jogo
        if gamescreen == True and event.type == pygame.MOUSEMOTION:
            if deck[0].isOver(pos):
                deck[0].color = (200,200,200)
                for Card in deck:
                    Card.draw(gameDisplay ,0)
            else:
                deck[0].color = (0,200,100)
                for Card in deck:
                    Card.draw(gameDisplay, 0)
            
            if deck[3].isOver(pos):
                deck[3].color = (200,200,200)
                for Card in deck:
                    Card.draw(gameDisplay ,0)
            else:
                deck[3].color = (0,200,100)
                for Card in deck:
                    Card.draw(gameDisplay, 0)
        
        #mouse over no menu
        if event.type == pygame.MOUSEMOTION and gamescreen == False:
            mouse_over_check(pos)
            main_menu_draw()
        
        #clicar em coisas
        if event.type == pygame.MOUSEBUTTONDOWN:
            if yellowbutton4x3.isOver(pos):
                gameDisplay.fill(black)
                gamescreen = True
                get_deck()
                for Card in deck:
                    Card.draw(gameDisplay, 0)
                exitbutton2.draw(gameDisplay)

            if deck[0].isOver(pos):
                deck[0].outline = 2
                deck[0].color == (0,200,100)
                deck_flipped.append(deck[0])
                deck.remove(deck[0])
                print(deck[0])
                gameDisplay.fill(black)
                deck_flipped[0].draw(gameDisplay, 0)
                for Card in deck:
                    Card.draw(gameDisplay, 0)
                pygame.draw.circle(gameDisplay, (0,100,200), (475, 180), 30)

                        

#passamos o rato por uma carta, obtemos o index dessa carta, mudamos a cor dessa carta apartir do index.
                

            if yellowbutton4x4.isOver(pos):
                gameDisplay.fill(black)
            if yellowbutton5x4.isOver(pos):
                gameDisplay.fill(black)
            if exitbutton.isOver(pos):
                quit()


    pygame.display.flip()

print(event)


#pygame.display.update()
clock.tick(60)
