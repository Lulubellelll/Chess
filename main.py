from classes.kares import *
from classes.images import *

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([980, 980])

# Definitions Out
reClick = False
whitesTurn = True

# Run until the user asks to quit
running = True
while running:

    # Definitions
    (mx, my) = pygame.mouse.get_pos()

    # Events
    for event in pygame.event.get():

        for e in kares:
            if mx in range(e.sq[0], e.sq[1]) and my in range(e.sq[2], e.sq[3]) and e.sq[5]:
                e.sq[7] = True
            else:
                e.sq[7] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(mx, my)

            for e in kares:
                # Pick
                if mx in range(e.sq[0], e.sq[1]) and my in range(e.sq[2], e.sq[3]):
                    print(whitesTurn, 'bo0')

                    # Eat
                    if e.sq[6] and e.sq[5] == False and e.KARE.onIt != 'Empty':
                        print('eat')
                        if Choosen[0].onIt.color != e.KARE.onIt.color:
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

                            defthreats()
                            for x in kareler:
                                if x.onIt == BS:
                                    if x.id[4] in Stnew:
                                        BS.true_thr()
                                        print('Beyaz: ', BS.threatened)
                                    else:
                                        BS.false_thr()
                                        print('Beyaz: ', BS.threatened)
                            for x in kareler:
                                if x.onIt == SS:
                                    if x.id[4] in Btnew:
                                        SS.true_thr()
                                        print('Siyah: ', SS.threatened)
                                    else:
                                        SS.false_thr()
                                        print('Siyah:', SS.threatened)

                            if whitesTurn and BS.threatened:
                                seçilmiş.change_onIt(e.KARE.onIt)
                                seçilmiş.change_sit(e.KARE.situation)
                                e.KARE.onIt.posx = seçilmiş.id[0]
                                e.KARE.onIt.posy = seçilmiş.id[2]
                                e.KARE.change_onIt('Empty')
                                e.KARE.change_sit('empty')
                                reClick = False
                                delChoosen()
                            elif whitesTurn == False and SS.threatened:
                                seçilmiş.change_onIt(e.KARE.onIt)
                                seçilmiş.change_sit(e.KARE.situation)
                                e.KARE.onIt.posx = seçilmiş.id[0]
                                e.KARE.onIt.posy = seçilmiş.id[2]
                                e.KARE.change_onIt('Empty')
                                e.KARE.change_sit('empty')
                                reClick = False
                                delChoosen()
                            else:
                                reClick = False
                                whitesTurn = not whitesTurn
                                delChoosen()

                        else:
                            print('KENDİ TAŞINI YİYEMEZSİN')
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

                            defthreats()
                            for x in kareler:
                                if x.onIt == BS:
                                    if x.id[4] in Stnew:
                                        BS.true_thr()
                                        print('Beyaz: ', BS.threatened)
                                    else:
                                        BS.false_thr()
                                        print('Beyaz: ', BS.threatened)
                            for x in kareler:
                                if x.onIt == SS:
                                    if x.id[4] in Btnew:
                                        SS.true_thr()
                                        print('Siyah: ', SS.threatened)
                                    else:
                                        SS.false_thr()
                                        print('Siyah:', SS.threatened)

                            if whitesTurn and BS.threatened:
                                seçilmiş.change_onIt(e.KARE.onIt)
                                seçilmiş.change_sit(e.KARE.situation)
                                e.KARE.onIt.posx = seçilmiş.id[0]
                                e.KARE.onIt.posy = seçilmiş.id[2]
                                e.KARE.change_onIt('Empty')
                                e.KARE.change_sit('empty')
                                reClick = False
                                delChoosen()
                            elif whitesTurn == False and SS.threatened:
                                seçilmiş.change_onIt(e.KARE.onIt)
                                seçilmiş.change_sit(e.KARE.situation)
                                e.KARE.onIt.posx = seçilmiş.id[0]
                                e.KARE.onIt.posy = seçilmiş.id[2]
                                e.KARE.change_onIt('Empty')
                                e.KARE.change_sit('empty')
                                reClick = False
                                delChoosen()
                            else:
                                reClick = False
                                whitesTurn = not whitesTurn
                                delChoosen()

                        # Click
                        else:
                            if whitesTurn == True and e.KARE.onIt.color == 'beyaz' or whitesTurn == False and e.KARE.onIt.color == 'siyah':
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
                                    print(whitesTurn, 'bo1')
                            else:
                                print('YANLIŞ SIRA')

        if event.type == pygame.QUIT:
            running = False

    # Draw
    img = pygame.image.load('images/chessTable.png')
    screen.blit(img, (0, 0))

    # Pieces
    for e in pieces:
        if e.alive:
            screen.blit(e.img, (e.posx, e.posy))

    # İşaretler
    sign = pygame.image.load('images/50yi.png')
    bsign = pygame.image.load('images/50i.png')
    tsign = pygame.image.load('images/tehdit50.png')

    for e in kareler:
        if e.id[5]:
            screen.blit(sign, (e.id[0], e.id[2]))
            if e.id[7]:
                screen.blit(bsign, (e.id[0], e.id[2]))
        if len(Choosen) > 0:
            if Choosen[0].onIt.color == 'beyaz':
                if e.id[6] and e.onIt.color == 'siyah':
                    screen.blit(tsign, (e.id[0], e.id[2]))
            else:
                if e.id[6] and e.onIt.color == 'beyaz':
                    screen.blit(tsign, (e.id[0], e.id[2]))

    # Flip the display
    pygame.display.flip()

pygame.quit()
