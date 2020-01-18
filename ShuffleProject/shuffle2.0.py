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


def get_index():
    index = [1,1,2,2,3,3,4,4,5,5,6,6]
    random.shuffle(index)
    for i in range(0, 12):
            deck[i].index = (index[i])
    return deck 

'''
def get_shape(deck):
    compendium = []
    for dx in range(0, 4):
        for dy in range(0, 3):
            compendium.append(Tirangle(random.randint(0,255),200,random.randint(0,255)), ((deck[dx].x/2, deck[dy].y/3), (deck[dx].x/3,deck[dy].y/3), ((deck[dx].x/3)*2,deck[dy].y/3))
    return deck
'''
def main_menu_draw():
    gameDisplay.blit(myimage, imagerect)
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
        
        #MOUSE OVER MENU
        if event.type == pygame.MOUSEMOTION and gamescreen == False:
            mouse_over_check(pos)
            main_menu_draw()

        #MOUSE OVER IN-GAME
        if gamescreen == True and event.type == pygame.MOUSEMOTION:
            for i in range(0,len(deck)):
                if deck[i].isOver(pos):
                    deck[i].color = (200,200,200)
                    for Card in deck:
                        Card.draw(gameDisplay ,0)
                else:
                    deck[i].color = (0,200,100)
                    for Card in deck:
                        Card.draw(gameDisplay, 0)
        #MOUSE CLICK
        if event.type == pygame.MOUSEBUTTONDOWN:
            #MOUSE CLICK IN MENU
            if gamescreen == False:
                if yellowbutton4x3.isOver(pos):
                    gameDisplay.fill(black)
                    gamescreen = True
                    get_deck()
                    get_index()
                    for Card in deck:
                        Card.draw(gameDisplay, 0)
                    exitbutton2.draw(gameDisplay)

                if gamescreen == False and yellowbutton4x4.isOver(pos):
                    gameDisplay.fill(black)
                    gamescreen = True
                    get_deck()
                    for Card in deck:
                        Card.draw(gameDisplay, 0)
                    exitbutton2.draw(gameDisplay)
                
                if gamescreen == False and yellowbutton5x4.isOver(pos):
                    gameDisplay.fill(black)
                    gamescreen = True
                    get_deck()
                    for Card in deck:
                        Card.draw(gameDisplay, 0)
                    exitbutton2.draw(gameDisplay)

                if gamescreen == False and exitbutton.isOver(pos):
                    quit()
            #MOUSE CLICK IN-GAME
            else:
                for i in range(0,len(deck)):
                    print(len(deck))
                    if deck[i].isOver(pos):
                            deck[i].outline = 2
                            deck[i].color == (0,200,100)
                            deck_flipped.append(deck[i])
                            print(deck[i])
                            gameDisplay.fill(black)
                            if len(deck_flipped) == 1:
                                j=i
                            deck_flipped[0].draw(gameDisplay, 0)
                            for Card in deck:
                                Card.draw(gameDisplay, 0)
                            if len(deck_flipped) == 2:
                                deck[j].outline = 0
                                deck[i].outline = 0
                                if deck[j].index == deck[i].index:
                                    print("hello?")
                                    deck.pop(i)
                                    if i > j:
                                        deck.pop(j+1)
                                    else:
                                        deck.pop(j-1)
                                deck_flipped = []



                if gamescreen == True and exitbutton2.isOver(pos):
                    gameDisplay.fill(black)
                    gamescreen = False

    pygame.display.flip()

print(event)


#pygame.display.update()
clock.tick(60)
