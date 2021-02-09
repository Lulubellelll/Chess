import pygame
from classes.pieces import *
from classes.squares import *
from classes.kares import *
from classes.images import *

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([980, 980])

# Definitions Out
reClick = False
beyazOynar = True


# Run until the user asks to quit
running = True
while running:

    # Definitions
    (mx, my) = pygame.mouse.get_pos()

    # Events
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(mx, my)

            for e in kares:
                # Pick
                if mx in range(e.sq[0], e.sq[1]) and my in range(e.sq[2], e.sq[3]):
                    print(beyazOynar, 'bo0')
                    for elements in squares:
                        if elements[6]:
                            print('burası', elements)
                   

                    # Eat
                    if e.sq[6] and e.sq[5] == False:
                        print('eat')

                        e.KARE.onIt.death()
                        print(e.KARE.onIt.alive)

                        for elements in squares:
                            if elements[5]:
                                elements[5] = False
                            else:
                                pass

                        for elements in squares:
                            if elements[6]:
                                elements[6] = False
                            else:
                                pass

                        seçilmiş = Choosen[0]
                        e.KARE.change_onIt(seçilmiş.onIt)
                        e.KARE.change_sit(seçilmiş.situation)
                        seçilmiş.onIt.posx = e.sq[0]
                        seçilmiş.onIt.posy = e.sq[2]
                        seçilmiş.change_onIt('Empty')
                        seçilmiş.change_sit('empty')
                        delChoosen()
                        beyazOynar = not beyazOynar
                    # Empty   
                    elif e.KARE.onIt == 'Empty' and e.sq[5] == False:
                        pass
                        print('Burada Takılıyor')
                    # Click
                    else:
                        # Move
                        if e.sq[5]:
                            print('hareket')

                            for elements in squares:
                                if elements[5]:
                                    elements[5] = False
                                else:
                                    pass

                            for elements in squares:
                                if elements[6]:
                                    elements[6] = False
                                else:
                                    pass

                            seçilmiş = Choosen[0]
                            e.KARE.change_onIt(seçilmiş.onIt)
                            e.KARE.change_sit(seçilmiş.situation)
                            seçilmiş.onIt.posx = e.sq[0]
                            seçilmiş.onIt.posy = e.sq[2]
                            seçilmiş.change_onIt('Empty')
                            seçilmiş.change_sit('empty')
                            reClick = False
                            beyazOynar = not beyazOynar
                            delChoosen()
                        # Click
                        else:
                            if beyazOynar == True and e.KARE.onIt.color == 'beyaz' or beyazOynar == False and e.KARE.onIt.color == 'siyah':
                                # Reclick
                                if reClick:
                                    print('YENIDEN TIKLANDI')
                                    e.KARE.onIt.press_again()
                                    reClick = not reClick
                                # First Click
                                else:
                                    print('İlk Evre')
                                    e.KARE.onIt.press(e.sq[4], e.KARE)
                                    reClick = not reClick
                                    print(beyazOynar, 'bo1')
                            else:
                                print('YANLIŞ SIRA')
                                
        if event.type == pygame.QUIT:
            running = False

    # Draw
    img = pygame.image.load('Chess.png')
    screen.blit(img, (0, 0))

    # Pieces
    for e in pieces:
        if e.alive:
            screen.blit(e.img, (e.posx, e.posy))

    # İşaretler
    işaret = pygame.image.load('işaret.png')

    for e in squares:
        if e[5]:
            screen.blit(işaret, (e[0], e[2]))

    # Flip the display
    pygame.display.flip()

pygame.quit()
