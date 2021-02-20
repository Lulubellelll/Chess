from classes.kares import *
from classes.images import *

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([980, 980])

# Definitions Out
reClick = False
whitesTurn = True
moveSound = pygame.mixer.Sound('sounds/move.mp3')
eatSound = pygame.mixer.Sound('sounds/Eat.mp3')

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

                    # Eat
                    if e.sq[6] and e.sq[5] == False and e.KARE.onIt != 'Empty':
                        print('eat')
                        if Choosen[0].onIt.color != e.KARE.onIt.color:
                            e.KARE.onIt.death()
                            print('WhitesTurn: ', whitesTurn)

                            for x in kareler:
                                if x.onIt != 'Empty':
                                    if x.onIt.pressed:
                                        x.onIt.pressed = False

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

                            veriSaklama.append(e.KARE.onIt)

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
                                e.KARE.change_onIt(veriSaklama[0])
                                reClick = False
                                e.KARE.onIt.reborn()
                                delVeri()
                                delChoosen()
                            elif not whitesTurn and SS.threatened:
                                print('BURAYA DÜŞTÜÜÜÜ')
                                seçilmiş.change_onIt(e.KARE.onIt)
                                seçilmiş.change_sit(e.KARE.situation)
                                e.KARE.onIt.posx = seçilmiş.id[0]
                                e.KARE.onIt.posy = seçilmiş.id[2]
                                e.KARE.change_onIt(veriSaklama[0])
                                e.KARE.change_sit('empty')
                                reClick = False
                                e.KARE.onIt.reborn()
                                delVeri()
                                delChoosen()
                            else:
                                if Choosen[0].onIt in pawns:
                                    if not Choosen[0].firstMove and not Choosen.fmc:
                                        Choosen[0].firstMove = True
                                        Choosen.fmc = True
                                eatSound.play()
                                e.KARE.chose = True
                                Choosen[0].chose = True
                                reClick = False
                                whitesTurn = not whitesTurn
                                delVeri()
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

                            for x in kareler:
                                if x.onIt != 'Empty':
                                    if x.onIt.pressed:
                                        x.onIt.pressed = False

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

                            save()
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
                                if veriSaklama[0] in pawns:
                                    veriSaklama[0].change_fm()
                                moveSound.play()
                                e.KARE.chose = True
                                Choosen[0].chose = True
                                reClick = False
                                whitesTurn = not whitesTurn
                                delVeri()
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
                                    for i in kareler:
                                        if i.chose:
                                            i.chose = False
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

    # İşaretler
    Sign = pygame.image.load('images/50yi.png')
    bSign = pygame.image.load('images/50i.png')
    tSign = pygame.image.load('images/tehdit50.png')
    sSign = pygame.image.load('images/seçilmiş50ii.png')
    scSign = pygame.image.load('images/sahCek20.png')

    for e in kareler:
        # Blink
        if e.id[5]:
            screen.blit(Sign, (e.id[0], e.id[2]))
            if e.id[7]:
                screen.blit(bSign, (e.id[0], e.id[2]))
        if e.chose:
            screen.blit(sSign, (e.id[0], e.id[2]))

        # Tehdit
        if len(Choosen) > 0:
            if e.onIt != 'Empty':
                if Choosen[0].onIt.color == 'beyaz':
                    if e.id[6] and e.onIt.color == 'siyah':
                        screen.blit(tSign, (e.id[0], e.id[2]))
                else:
                    if e.id[6] and e.onIt.color == 'beyaz':
                        screen.blit(tSign, (e.id[0], e.id[2]))

        # Seçilmiş
        if e.onIt != 'Empty':
            if e.onIt.pressed:
                screen.blit(Sign, (e.id[0], e.id[2]))
                screen.blit(bSign, (e.id[0], e.id[2]))

        # Şah Çekiliyor
        if e.onIt == BS or e.onIt == SS:
            if e.onIt.threatened:
                screen.blit(scSign, (e.id[0], e.id[2]))

    # Pieces
    for e in pieces:
        if e.alive:
            screen.blit(e.img, (e.posx, e.posy))

    # Flip the display
    pygame.display.flip()

pygame.quit()
