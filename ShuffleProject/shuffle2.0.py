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
deck = get_deck(0, 0)

gameDisplay = pygame.display.set_mode((res))
gameDisplay.blit(myimage, imagerect)

yellowbutton4x3 = button(yellow, 560, 250, 125, 30, '4x3')
yellowbutton4x4 = button(yellow, 560, 290, 125, 30, '4x4')
yellowbutton5x4 = button(yellow, 560, 330, 125, 30, '5x4')
yellowbutton6x5 = button(yellow, 560, 370, 125, 30, '6x5')
yellowbutton6x6 = button(yellow, 560, 410, 125, 30, '6x6')
exitbutton = button(yellow, 560, 480, 125, 30, 'EXIT')
exitbutton2 = button(yellow, 50, 660, 125, 30, 'EXIT')

numberofcardsturned = 0
car1turned = 0
car2turned = 0


def get_index(x, y):
    index = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18]
    indextemp = index[:(x*y)]
    random.shuffle(indextemp)
    for i in range(0, x*y):
        print(i)
        deck[i].index = indextemp[i]
        deck[i].text = str(indextemp[i])
    return deck

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
            

pygame.display.set_caption('Shuffle')
clock = pygame.time.Clock()
crashed = False
gamescreen = False
timetowait = 0
while not crashed:
    if numberofcardsturned == 2:
        timetowait = 1000
    gameDisplay.fill(black)

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if event.type == pygame.QUIT:
            crashed = True
        
    #MOUSE OVER MENU
    if gamescreen == False:
        mouse_over_check(pos)
        main_menu_draw()

    #MOUSE OVER IN-GAME
    if gamescreen == True:
        for i in range(0,len(deck)):
            if deck[i].isOver(pos):
                if deck[i].flipped == 0:
                    deck[i].color = (200,200,200)
                    for Card in deck:
                        Card.draw(gameDisplay ,0 , deck[i].flipped)
                elif deck[i].flipped == 1:
                    deck[i].color = (200,200,200)
                    for Card in deck:
                        Card.draw(gameDisplay ,2 , deck[i].flipped)
            else:
                deck[i].color = (0,200,100)
                for Card in deck:
                    Card.draw(gameDisplay, 0)
            exitbutton2.draw(gameDisplay)
        
    
    #MOUSE CLICK
    if mouse_click[0] == 1:
        #MOUSE CLICK IN MENU
        if gamescreen == False:
            if yellowbutton4x3.isOver(pos):
                gameDisplay.fill(black)
                gamescreen = True
                deck = get_deck(4, 3)
                get_index(4, 3)
                for Card in deck:
                    Card.draw(gameDisplay)
                exitbutton2.draw(gameDisplay)
                

            if gamescreen == False and yellowbutton4x4.isOver(pos):
                gameDisplay.fill(black)
                gamescreen = True
                deck = get_deck(4, 4)
                get_index(4, 4)
                for Card in deck:
                    Card.draw(gameDisplay, 0)
                exitbutton2.draw(gameDisplay)
                pygame.display.flip()
                
            
            if gamescreen == False and yellowbutton5x4.isOver(pos):
                gameDisplay.fill(black)
                gamescreen = True
                deck = get_deck(5, 4)
                get_index(5, 4)
                for Card in deck:
                    Card.draw(gameDisplay, 0)
                exitbutton2.draw(gameDisplay)
                pygame.display.flip()
            
            if gamescreen == False and yellowbutton6x5.isOver(pos):
                gameDisplay.fill(black)
                gamescreen = True
                deck = get_deck(6, 5)
                get_index(6, 5)
                for Card in deck:
                    Card.draw(gameDisplay, 0)
                exitbutton2.draw(gameDisplay)
                pygame.display.flip()

            if gamescreen == False and yellowbutton6x6.isOver(pos):
                gameDisplay.fill(black)
                gamescreen = True
                deck = get_deck(6, 6)
                get_index(6, 6)
                for Card in deck:
                    Card.draw(gameDisplay, 0)
                exitbutton2.draw(gameDisplay)
                pygame.display.flip()
                

            if gamescreen == False and exitbutton.isOver(pos):
                quit()
        #MOUSE CLICK IN-GAME
        elif gamescreen == True:
            i = 0
            while i in range(0,len(deck)):
                if deck[i].isOver(pos):
                    deck[i].outline = 2
                    deck[i].color == (0,200,100)
                    if deck[i].flipped == 0:
                        deck[i].flipped = 1
                        if car1turned == 0:
                            car1turned = i
                            numberofcardsturned += 1
                        else:
                            car2turned = i
                            numberofcardsturned += 1
                    
                        if numberofcardsturned == 2:
                            if deck[car1turned].index == deck[car2turned].index:
                                deck[car1turned].ingame = 0
                                deck[car2turned].ingame = 0
                                car1turned = 0
                                car2turned = 0
                            else:
                                deck[car1turned].flipped = 0
                                deck[car2turned].flipped = 0
                                car1turned = 0
                                car2turned = 0
                                numberofcardsturned = 0


                else:
                    deck[i].color = (0,200,100)
                i += 1
            if gamescreen == True and exitbutton2.isOver(pos):
                gamescreen = False
    if timetowait > 0:
        pygame.time.wait(timetowait)
        numberofcardsturned = 0
        timetowait = 0
                
    pygame.display.flip()

clock.tick(60)
