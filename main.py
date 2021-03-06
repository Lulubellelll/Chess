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


def allEmpty(rookList):
    a = 0
    for i in rookList:
        if i.onIt == 'Empty':
            a += 1
    if a == len(rookList):
        return True
    else:
        return False


def allSafeS(rookList):
    delThs()
    defthreats()
    a = 0
    for i in rookList:
        if i.id[4] in Stnew:
            a += 1
    if a > 0:
        return False
    else:
        return True


def allSafeB(rookList):
    delThs()
    defthreats()
    a = 0
    for i in rookList:
        if i.id[4] in Stnew:
            a += 1
    if a > 0:
        return False
    else:
        return True


# Run until the user asks to quit
running = True
while running:

    # Definitions
    (mx, my) = pygame.mouse.get_pos()
    uzunBeyazRok = [B1, C1, D1]
    kısaBeyazRok = [F1, G1]
    uzunSiyahRok = [B1, C8, D8]
    kısaSiyahRok = [F8, G8]

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

                    # Special Situations
                    if e.KARE.onIt == BS and whitesTurn and not reClick and not BS.threatened:
                        if allEmpty(uzunBeyazRok) and BS.fm and BK1.fm and allSafeB(uzunBeyazRok):
                            BK1.rookability = True
                        else:
                            delThs()
                        if allEmpty(kısaBeyazRok) and BS.fm and BK2.fm and allSafeB(kısaBeyazRok):
                            BK2.rookability = True
                        else:
                            delThs()
                    elif e.KARE.onIt == BS and whitesTurn and reClick:
                        # Düzeltemeler
                        delThs()
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
                        for b in rooks:
                            b.rookability = False
                    if e.KARE.onIt == SS and not whitesTurn and not reClick and not SS.threatened:
                        if allEmpty(uzunSiyahRok) and SS.fm and SK1.fm and allSafeS(uzunSiyahRok):
                            SK1.rookability = True
                        else:
                            delThs()
                        if allEmpty(kısaSiyahRok) and SS.fm and SK2.fm and allSafeS(kısaSiyahRok):
                            SK2.rookability = True
                        else:
                            delThs()
                    elif e.KARE.onIt == SS and not whitesTurn and reClick:
                        delThs()
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
                        for b in rooks:
                            b.rookability = False

                    if e.KARE.onIt in rooks:
                        if e.KARE.onIt == BK1 and BK1.rookability:

                            # Düzeltemeler
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
                            for b in rooks:
                                b.rookability = False

                            Choosen.clear()
                            BS.posx = c1[0]
                            BS.posy = c1[2]
                            BK1.posx = d1[0]
                            BK1.posy = d1[2]
                            D1.onIt = BK1
                            e.KARE.change_onIt('Empty')
                            E1.change_onIt('Empty')
                            E1.change_sit('empty')
                            whitesTurn = not whitesTurn
                            moveSound.play()
                        if e.KARE.onIt == BK2 and BK2.rookability:

                            # Düzeltemeler
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
                            for b in rooks:
                                b.rookability = False

                            Choosen.clear()
                            BS.posx = g1[0]
                            BS.posy = g1[2]
                            BK2.posx = f1[0]
                            BK2.posy = f1[2]
                            F1.onIt = BK1
                            e.KARE.change_onIt('Empty')
                            E1.change_onIt('Empty')
                            E1.change_sit('empty')
                            whitesTurn = not whitesTurn
                            moveSound.play()
                        if e.KARE.onIt == SK1 and SK1.rookability:

                            # Düzeltemeler
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
                            for b in rooks:
                                b.rookability = False

                            Choosen.clear()
                            SS.posx = c8[0]
                            SS.posy = c8[2]
                            SK1.posx = d8[0]
                            SK1.posy = d8[2]
                            D8.onIt = SK1
                            e.KARE.change_onIt('Empty')
                            E8.change_onIt('Empty')
                            E8.change_sit('empty')
                            whitesTurn = not whitesTurn
                            moveSound.play()
                        if e.KARE.onIt == SK2 and SK2.rookability:

                            # Düzeltemeler
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
                            for b in rooks:
                                b.rookability = False

                            Choosen.clear()
                            SS.posx = g8[0]
                            SS.posy = g8[2]
                            SK2.posx = f8[0]
                            SK2.posy = f8[2]
                            F8.onIt = SK1
                            e.KARE.change_onIt('Empty')
                            E8.change_onIt('Empty')
                            E8.change_sit('empty')
                            whitesTurn = not whitesTurn
                            moveSound.play()

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

                            for b in rooks:
                                b.rookability = False

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

                            for b in rooks:
                                b.rookability = False

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
                                if veriSaklama[0] in kings:
                                    veriSaklama[0].change_fm()
                                if veriSaklama[0] in rooks:
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
    tSign = pygame.image.load('images/tehdit60i.png')
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

        # Rok Özel
        if e.onIt in rooks:
            if e.onIt.rookability:
                screen.blit(tSign, (e.id[0], e.id[2]))

    # Pieces
    for e in pieces:
        if e.alive:
            screen.blit(e.img, (e.posx, e.posy))

    # Flip the display
    pygame.display.flip()

pygame.quit()
