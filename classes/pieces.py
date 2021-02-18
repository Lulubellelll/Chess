from .squares import *
from .images import *

# LISTS
ids = []
Choosen = []
fulls = []
tehditfulls = []
Sthreats = []
Bthreats = []
Btnew = []
Stnew = []
threats = []


# CLASSES
class Pieces(object):
    def __init__(self, color, alive, posx, posy, img):
        self.color = color
        self.alive = alive
        self.posx = posx
        self.posy = posy
        self.img = img

    def death(self):
        self.alive = False


class Kale(Pieces):
    def __init__(self, color, alive, posx, posy, img):
        super().__init__(color, alive, posx, posy, img)

    def threat(self, id, square):
        print(ids)

        sat = (id // 8) + 1
        süt = (id % 8) + 1

        for x in kareler:
            if x.onIt != 'Empty':
                fulls.append(x.id[4])

        # Sağ
        for i in range(1, 9 - süt):
            if (id + 1 * i) in fulls:
                tehditfulls.append(id + 1 * i)
                break
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 1 * i)
                else:
                    Sthreats.append(id + 1 * i)


        # Sol
        for i in range(1, süt):
            if (id - 1 * i) in fulls:
                tehditfulls.append(id - 1 * i)
                break
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 1 * i)
                else:
                    Sthreats.append(id - 1 * i)

        # Aşşağı
        for i in range(1, sat):
            if (id - 8 * i) in fulls:
                tehditfulls.append(id - 8 * i)
                break
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 8 * i)
                else:
                    Sthreats.append(id - 8 * i)

        # Yukarı
        for i in range(1, 9 - sat):
            if (id + 8 * i) in fulls:
                tehditfulls.append(id + 8 * i)
                break
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 8 * i)
                else:
                    Sthreats.append(id + 8 * i)

        del_dup(threats)
        print(threats, Choosen, tehditfulls)

        for elements in squares:
            if elements[4] in ids:
                elements[5] = True
            else:
                pass

        for elements in squares:
            if elements[4] in tehditfulls:
                elements[6] = True
            else:
                pass

        for elements in squares:
            if elements[6]:
                print(elements)

        fulls.clear()
        tehditfulls.clear()

    def press(self, id, square):
        print(ids)

        sat = (id // 8) + 1
        süt = (id % 8) + 1

        print('sat: ', sat)
        print('süt: ', süt)

        for x in kareler:
            if x.onIt != 'Empty':
                fulls.append(x.id[4])

        print(fulls)

        # Sağ
        for i in range(1, 9 - süt):
            if (id + 1 * i) in fulls:
                tehditfulls.append(id + 1 * i)
                break
            else:
                ids.append(id + 1 * i)

        # Sol
        for i in range(1, süt):
            if (id - 1 * i) in fulls:
                tehditfulls.append(id - 1 * i)
                break
            else:
                ids.append(id - 1 * i)

        # Aşşağı
        for i in range(1, sat):
            if (id - 8 * i) in fulls:
                tehditfulls.append(id - 8 * i)
                break
            else:
                ids.append(id - 8 * i)

        # Yukarı
        for i in range(1, 9 - sat):
            if (id + 8 * i) in fulls:
                tehditfulls.append(id + 8 * i)
                break
            else:
                ids.append(id + 8 * i)

        del_dup(ids)
        Choosen.append(square)
        print(ids, Choosen, tehditfulls)

        for elements in squares:
            if elements[4] in ids:
                elements[5] = True
            else:
                pass

        for elements in squares:
            if elements[4] in tehditfulls:
                elements[6] = True
            else:
                pass

        for elements in squares:
            if elements[6]:
                print(elements)

        ids.clear()
        fulls.clear()
        tehditfulls.clear()

    def press_again(self):
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

        ids.clear()
        Choosen.clear()
        tehditfulls.clear()
        fulls.clear()
        print(ids, Choosen, fulls)


class Fil(Pieces):
    def __init__(self, color, alive, posx, posy, scolor, img):
        super().__init__(color, alive, posx, posy, img)
        self.scolor = scolor

    def threat(self, id, square):

        sat = (id // 8) + 1
        süt = (id % 8) + 1

        for x in kareler:
            if x.onIt != 'Empty':
                fulls.append(x.id[4])

        # Sağ Yukarı
        if sat >= süt:
            for i in range(1, 9 - sat):
                if (id + 9 * i) in fulls:
                    tehditfulls.append(id + 9 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id + 9 * i)
                    else:
                        Sthreats.append(id + 9 * i)

        else:
            for i in range(1, (8 - süt) + 1):
                if (id + 9 * i) in fulls:
                    tehditfulls.append(id + 9 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id + 9 * i)
                    else:
                        Sthreats.append(id + 9 * i)

        # Sol Aşşağı
        if sat >= süt:
            for i in range(1, süt):
                if (id - 9 * i) in fulls:
                    tehditfulls.append(id - 9 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id - 9 * i)
                    else:
                        Sthreats.append(id - 9 * i)
        else:
            for i in range(1, sat):
                if (id - 9 * i) in fulls:
                    tehditfulls.append(id - 9 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id - 9 * i)
                    else:
                        Sthreats.append(id - 9 * i)

        # Sol Yukarı
        if sat + süt >= 9:
            for i in range(1, (8 - sat) + 1):
                if (id + 7 * i) in fulls:
                    tehditfulls.append(id + 7 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id + 7 * i)
                    else:
                        Sthreats.append(id + 7 * i)
        else:
            for i in range(1, süt):
                if (id + 7 * i) in fulls:
                    tehditfulls.append(id + 7 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id + 7 * i)
                    else:
                        Sthreats.append(id + 7 * i)

        # sağ Aşşağı
        if sat + süt >= 9:
            for i in range(1, 9 - süt):
                if (id - 7 * i) in fulls:
                    tehditfulls.append(id - 7 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id - 7 * i)
                    else:
                        Sthreats.append(id - 7 * i)

        else:
            for i in range(1, sat):
                if (id - 7 * i) in fulls:
                    tehditfulls.append(id - 7 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id - 7 * i)
                    else:
                        Sthreats.append(id - 7 * i)

        del_dup(threats)
        print(threats, Choosen, tehditfulls)

        for elements in squares:
            if elements[4] in ids:
                elements[5] = True
            else:
                pass

        for elements in squares:
            if elements[4] in tehditfulls:
                elements[6] = True
            else:
                pass

        for elements in squares:
            if elements[6]:
                print(elements)

        fulls.clear()
        tehditfulls.clear()

    def press(self, id, square):
        print(ids)

        sat = (id // 8) + 1
        süt = (id % 8) + 1

        print('sat: ', sat)
        print('süt: ', süt)

        for x in kareler:
            if x.onIt != 'Empty':
                fulls.append(x.id[4])

        print(fulls)

        # Sağ Yukarı
        if sat >= süt:
            for i in range(1, 9 - sat):
                if (id + 9 * i) in fulls:
                    tehditfulls.append(id + 9 * i)
                    break
                else:
                    ids.append(id + 9 * i)

        else:
            for i in range(1, (8 - süt) + 1):
                if (id + 9 * i) in fulls:
                    tehditfulls.append(id + 9 * i)
                    break
                else:
                    ids.append(id + 9 * i)

        # Sol Aşşağı
        if sat >= süt:
            for i in range(1, süt):
                if (id - 9 * i) in fulls:
                    tehditfulls.append(id - 9 * i)
                    break
                else:
                    ids.append(id - 9 * i)
        else:
            for i in range(1, sat):
                if (id - 9 * i) in fulls:
                    tehditfulls.append(id - 9 * i)
                    break
                else:
                    ids.append(id - 9 * i)

        # Sol Yukarı
        if sat + süt >= 9:
            for i in range(1, (8 - sat) + 1):
                if (id + 7 * i) in fulls:
                    tehditfulls.append(id + 7 * i)
                    break
                else:
                    ids.append(id + 7 * i)
        else:
            for i in range(1, süt):
                if (id + 7 * i) in fulls:
                    tehditfulls.append(id + 7 * i)
                    break
                else:
                    ids.append(id + 7 * i)

        # sağ Aşşağı
        if sat + süt >= 9:
            for i in range(1, 9 - süt):
                if (id - 7 * i) in fulls:
                    tehditfulls.append(id - 7 * i)
                    break
                else:
                    ids.append(id - 7 * i)

        else:
            for i in range(1, sat):
                if (id - 7 * i) in fulls:
                    tehditfulls.append(id - 7 * i)
                    break
                else:
                    ids.append(id - 7 * i)

        del_dup(ids)
        Choosen.append(square)
        print(ids, Choosen, tehditfulls)

        for elements in squares:
            if elements[4] in ids:
                elements[5] = True
            else:
                pass

        for elements in squares:
            if elements[4] in tehditfulls:
                elements[6] = True
            else:
                pass

        for elements in squares:
            if elements[6]:
                print(elements)

        ids.clear()
        fulls.clear()
        tehditfulls.clear()

    def press_again(self):
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

        ids.clear()
        Choosen.clear()
        tehditfulls.clear()
        fulls.clear()
        print(ids, Choosen, fulls)


class Vezir(Pieces):
    def __init__(self, color, alive, posx, posy, img):
        super().__init__(color, alive, posx, posy, img)

    def threat(self, id, square):

        sat = (id // 8) + 1
        süt = (id % 8) + 1

        for x in kareler:
            if x.onIt != 'Empty':
                fulls.append(x.id[4])

        # Sağ Yukarı
        if sat >= süt:
            for i in range(1, 9 - sat):
                if (id + 9 * i) in fulls:
                    tehditfulls.append(id + 9 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id + 9 * i)
                    else:
                        Sthreats.append(id + 9 * i)
        else:
            for i in range(1, (8 - süt) + 1):
                if (id + 9 * i) in fulls:
                    tehditfulls.append(id + 9 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id + 9 * i)
                    else:
                        Sthreats.append(id + 9 * i)

        # Sol Aşşağı
        if sat >= süt:
            for i in range(1, süt):
                if (id - 9 * i) in fulls:
                    tehditfulls.append(id - 9 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id - 9 * i)
                    else:
                        Sthreats.append(id - 9 * i)
        else:
            for i in range(1, sat):
                if (id - 9 * i) in fulls:
                    tehditfulls.append(id - 9 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id - 9 * i)
                    else:
                        Sthreats.append(id - 9 * i)

        # Sol Yukarı
        if sat + süt >= 9:
            for i in range(1, (8 - sat) + 1):
                if (id + 7 * i) in fulls:
                    tehditfulls.append(id + 7 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id + 7 * i)
                    else:
                        Sthreats.append(id + 7 * i)
        else:
            for i in range(1, süt):
                if (id + 7 * i) in fulls:
                    tehditfulls.append(id + 7 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id + 7 * i)
                    else:
                        Sthreats.append(id + 7 * i)

        # sağ Aşşağı
        if sat + süt >= 9:
            for i in range(1, 9 - süt):
                if (id - 7 * i) in fulls:
                    tehditfulls.append(id - 7 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id - 7 * i)
                    else:
                        Sthreats.append(id - 7 * i)
        else:
            for i in range(1, sat):
                if (id - 7 * i) in fulls:
                    tehditfulls.append(id - 7 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id - 7 * i)
                    else:
                        Sthreats.append(id - 7 * i)

        # Sağ
        for i in range(1, 9 - süt):
            if (id + 1 * i) in fulls:
                tehditfulls.append(id + 1 * i)
                break
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 1 * i)
                else:
                    Sthreats.append(id + 1 * i)

        # Sol
        for i in range(1, süt):
            if (id - 1 * i) in fulls:
                tehditfulls.append(id - 1 * i)
                break
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 1 * i)
                else:
                    Sthreats.append(id - 1 * i)

        # Aşşağı
        for i in range(1, sat):
            if (id - 8 * i) in fulls:
                tehditfulls.append(id - 8 * i)
                break
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 8 * i)
                else:
                    Sthreats.append(id - 8 * i)

        # Yukarı
        for i in range(1, 9 - sat):
            if (id + 8 * i) in fulls:
                tehditfulls.append(id + 8 * i)
                break
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 8 * i)
                else:
                    Sthreats.append(id + 8 * i)

        del_dup(threats)
        print(threats, Choosen, tehditfulls)

        for elements in squares:
            if elements[4] in ids:
                elements[5] = True
            else:
                pass

        for elements in squares:
            if elements[4] in tehditfulls:
                elements[6] = True
            else:
                pass

        for elements in squares:
            if elements[6]:
                print(elements)

        fulls.clear()
        tehditfulls.clear()

    def press(self, id, square):
        print(ids)

        sat = (id // 8) + 1
        süt = (id % 8) + 1

        print('sat: ', sat)
        print('süt: ', süt)

        for x in kareler:
            if x.onIt != 'Empty':
                fulls.append(x.id[4])

        print(fulls)

        # Sağ Yukarı
        if sat >= süt:
            for i in range(1, 9 - sat):
                if (id + 9 * i) in fulls:
                    tehditfulls.append(id + 9 * i)
                    break
                else:
                    ids.append(id + 9 * i)
        else:
            for i in range(1, (8 - süt) + 1):
                if (id + 9 * i) in fulls:
                    tehditfulls.append(id + 9 * i)
                    break
                else:
                    ids.append(id + 9 * i)

        # Sol Aşşağı
        if sat >= süt:
            for i in range(1, süt):
                if (id - 9 * i) in fulls:
                    tehditfulls.append(id - 9 * i)
                    break
                else:
                    ids.append(id - 9 * i)
        else:
            for i in range(1, sat):
                if (id - 9 * i) in fulls:
                    tehditfulls.append(id - 9 * i)
                    break
                else:
                    ids.append(id - 9 * i)

        # Sol Yukarı
        if sat + süt >= 9:
            for i in range(1, (8 - sat) + 1):
                if (id + 7 * i) in fulls:
                    tehditfulls.append(id + 7 * i)
                    break
                else:
                    ids.append(id + 7 * i)
        else:
            for i in range(1, süt):
                if (id + 7 * i) in fulls:
                    tehditfulls.append(id + 7 * i)
                    break
                else:
                    ids.append(id + 7 * i)

        # sağ Aşşağı
        if sat + süt >= 9:
            for i in range(1, 9 - süt):
                if (id - 7 * i) in fulls:
                    tehditfulls.append(id - 7 * i)
                    break
                else:
                    ids.append(id - 7 * i)
        else:
            for i in range(1, sat):
                if (id - 7 * i) in fulls:
                    tehditfulls.append(id - 7 * i)
                    break
                else:
                    ids.append(id - 7 * i)

        # Sağ
        for i in range(1, 9 - süt):
            if (id + 1 * i) in fulls:
                tehditfulls.append(id + 1 * i)
                break
            else:
                ids.append(id + 1 * i)

        # Sol
        for i in range(1, süt):
            if (id - 1 * i) in fulls:
                tehditfulls.append(id - 1 * i)
                break
            else:
                ids.append(id - 1 * i)

        # Aşşağı
        for i in range(1, sat):
            if (id - 8 * i) in fulls:
                tehditfulls.append(id - 8 * i)
                break
            else:
                ids.append(id - 8 * i)

        # Yukarı
        for i in range(1, 9 - sat):
            if (id + 8 * i) in fulls:
                tehditfulls.append(id + 8 * i)
                break
            else:
                ids.append(id + 8 * i)

        del_dup(ids)
        Choosen.append(square)
        print(ids, Choosen, tehditfulls)

        for elements in squares:
            if elements[4] in ids:
                elements[5] = True
            else:
                pass

        for elements in squares:
            if elements[4] in tehditfulls:
                elements[6] = True
            else:
                pass

        for elements in squares:
            if elements[6]:
                print(elements)

        ids.clear()
        fulls.clear()
        tehditfulls.clear()

    def press_again(self):
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

        ids.clear()
        Choosen.clear()
        tehditfulls.clear()
        fulls.clear()
        print(ids, Choosen, fulls)


class At(Pieces):
    def __init__(self, color, alive, posx, posy, img):
        super().__init__(color, alive, posx, posy, img)

    def threat(self, id, square):

        sat = (id // 8) + 1
        süt = (id % 8) + 1

        for x in kareler:
            if x.onIt != 'Empty':
                fulls.append(x.id[4])

        # Yukarı
        if sat != 7 and sat != 8 and süt != 8:
            if (id + 17) in fulls:
                tehditfulls.append(id + 17)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 17)
                else:
                    Sthreats.append(id + 17)

        if sat != 7 and sat != 8 and süt != 1:
            if (id + 15) in fulls:
                tehditfulls.append(id + 15)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 15)
                else:
                    Sthreats.append(id + 15)

        # Aşşağı
        if sat != 1 and sat != 2 and süt != 1:
            if (id - 17) in fulls:
                tehditfulls.append(id - 17)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 17)
                else:
                    Sthreats.append(id - 17)

        if sat != 1 and sat != 2 and süt != 8:
            if (id - 15) in fulls:
                tehditfulls.append(id - 15)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 15)
                else:
                    Sthreats.append(id - 15)

        # Sol
        if süt != 1 and süt != 2 and sat != 1:
            if (id - 10) in fulls:
                tehditfulls.append(id - 10)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 10)
                else:
                    Sthreats.append(id - 10)

        if süt != 1 and süt != 2 and sat != 8:
            if (id + 6) in fulls:
                tehditfulls.append(id + 6)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 6)
                else:
                    Sthreats.append(id + 6)

        # Sağ
        if süt != 7 and süt != 8 and sat != 1:
            if (id - 6) in fulls:
                tehditfulls.append(id - 6)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 6)
                else:
                    Sthreats.append(id - 6)

        if süt != 7 and süt != 8 and sat != 8:
            if (id + 10) in fulls:
                tehditfulls.append(id + 10)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 10)
                else:
                    Sthreats.append(id + 10)

        del_dup(threats)
        print(threats, Choosen, tehditfulls)

        for elements in squares:
            if elements[4] in ids:
                elements[5] = True
            else:
                pass

        for elements in squares:
            if elements[4] in tehditfulls:
                elements[6] = True
            else:
                pass

        for elements in squares:
            if elements[6]:
                print(elements)

        fulls.clear()
        tehditfulls.clear()

    def press(self, id, square):
        print(ids)

        sat = (id // 8) + 1
        süt = (id % 8) + 1

        print('sat: ', sat)
        print('süt: ', süt)

        for x in kareler:
            if x.onIt != 'Empty':
                fulls.append(x.id[4])

        print(fulls)

        # Yukarı
        if sat != 7 and sat != 8 and süt != 8:
            if (id + 17) in fulls:
                tehditfulls.append(id + 17)
            else:
                ids.append(id + 17)

        if sat != 7 and sat != 8 and süt != 1:
            if (id + 15) in fulls:
                tehditfulls.append(id + 15)
            else:
                ids.append(id + 15)

        # Aşşağı
        if sat != 1 and sat != 2 and süt != 1:
            if (id - 17) in fulls:
                tehditfulls.append(id - 17)
            else:
                ids.append(id - 17)

        if sat != 1 and sat != 2 and süt != 8:
            if (id - 15) in fulls:
                tehditfulls.append(id - 15)
            else:
                ids.append(id - 15)

        # Sol
        if süt != 1 and süt != 2 and sat != 1:
            if (id - 10) in fulls:
                tehditfulls.append(id - 10)
            else:
                ids.append(id - 10)

        if süt != 1 and süt != 2 and sat != 8:
            if (id + 6) in fulls:
                tehditfulls.append(id + 6)
            else:
                ids.append(id + 6)

        # Sağ
        if süt != 7 and süt != 8 and sat != 1:
            if (id - 6) in fulls:
                tehditfulls.append(id - 6)
            else:
                ids.append(id - 6)

        if süt != 7 and süt != 8 and sat != 8:
            if (id + 10) in fulls:
                tehditfulls.append(id + 10)
            else:
                ids.append(id + 10)

        del_dup(ids)
        Choosen.append(square)
        print(ids, Choosen, tehditfulls)

        for elements in squares:
            if elements[4] in ids:
                elements[5] = True
            else:
                pass

        for elements in squares:
            if elements[4] in tehditfulls:
                elements[6] = True
            else:
                pass

        for elements in squares:
            if elements[6]:
                print(elements)

        ids.clear()
        fulls.clear()
        tehditfulls.clear()

    def press_again(self):
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

        ids.clear()
        Choosen.clear()
        tehditfulls.clear()
        fulls.clear()
        print(ids, Choosen, fulls)


class Şah(Pieces):
    def __init__(self, color, alive, posx, posy, img):
        super().__init__(color, alive, posx, posy, img)

    def threat(self, id, square):

        sat = (id // 8) + 1
        süt = (id % 8) + 1

        for x in kareler:
            if x.onIt != 'Empty':
                fulls.append(x.id[4])

        # Sağ
        if süt != 8:
            if (id + 1) in fulls:
                tehditfulls.append(id + 1)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 1)
                else:
                    Sthreats.append(id + 1)

        # Sağ Yukarı
        if süt != 8 and sat != 8:
            if (id + 9) in fulls:
                tehditfulls.append(id + 9)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 9)
                else:
                    Sthreats.append(id + 9)

        # Sağ Aşşağı
        if süt != 8 and sat != 1:
            if (id - 7) in fulls:
                tehditfulls.append(id - 7)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 7)
                else:
                    Sthreats.append(id - 7)

        # Sol
        if süt != 1:
            if (id + 1) in fulls:
                tehditfulls.append(id - 1)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 1)
                else:
                    Sthreats.append(id - 1)

        # Sol Yukarı
        if süt != 1 and sat != 8:
            if (id + 7) in fulls:
                tehditfulls.append(id + 7)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 7)
                else:
                    Sthreats.append(id + 7)

        # Sol Aşşağı
        if süt != 1 and sat != 1:
            if (id - 9) in fulls:
                tehditfulls.append(id - 9)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 9)
                else:
                    Sthreats.append(id - 9)

        # Aşşağı
        if sat != 1:
            if (id + 1) in fulls:
                tehditfulls.append(id - 8)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 8)
                else:
                    Sthreats.append(id - 8)

        # Yukarı
        if sat != 8:
            if (id + 1) in fulls:
                tehditfulls.append(id + 8)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 8)
                else:
                    Sthreats.append(id + 8)

        del_dup(threats)
        print(threats, Choosen, tehditfulls)

        for elements in squares:
            if elements[4] in ids:
                elements[5] = True
            else:
                pass

        for elements in squares:
            if elements[4] in tehditfulls:
                elements[6] = True
            else:
                pass

        for elements in squares:
            if elements[6]:
                print(elements)

        fulls.clear()
        tehditfulls.clear()

    def press(self, id, square):

        global Sthreats
        global Bthreats

        sat = (id // 8) + 1
        süt = (id % 8) + 1

        for x in kareler:
            if x.onIt == 'Empty':
                pass
            else:
                x.onIt.threat(x.id[4], x)

        for i in Sthreats:
            if i not in Stnew:
                Stnew.append(i)

        for i in Bthreats:
            if i not in Btnew:
                Btnew.append(i)

        Sthreats = Stnew
        print('Sthreats:', Stnew)

        Bthreats = Btnew
        print('Bthreats:', Btnew)

        for x in kareler:
            if x.onIt != 'Empty':
                fulls.append(x.id[4])

        # Sağ
        if süt != 8:
            if (id + 1) in fulls:
                tehditfulls.append(id + 1)
            else:
                ids.append(id + 1)

        # Sağ Yukarı
        if süt != 8 and sat != 8:
            if (id + 9) in fulls:
                tehditfulls.append(id + 9)
            else:
                ids.append(id + 9)

        # Sağ Aşşağı
        if süt != 8 and sat != 1:
            if (id - 7) in fulls:
                tehditfulls.append(id - 7)
            else:
                ids.append(id - 7)

        # Sol
        if süt != 1:
            if (id + 1) in fulls:
                tehditfulls.append(id - 1)
            else:
                ids.append(id - 1)

        # Sol Yukarı
        if süt != 1 and sat != 8:
            if (id + 7) in fulls:
                tehditfulls.append(id + 7)
            else:
                ids.append(id + 7)

        # Sol Aşşağı
        if süt != 1 and sat != 1:
            if (id - 9) in fulls:
                tehditfulls.append(id - 9)
            else:
                ids.append(id - 9)

        # Aşşağı
        if sat != 1:
            if (id - 8) in fulls:
                tehditfulls.append(id - 8)
            else:
                ids.append(id - 8)

        # Yukarı
        if sat != 8:
            if (id + 8) in fulls:
                tehditfulls.append(id + 8)
            else:
                ids.append(id + 8)

        del_dup(ids)
        Choosen.append(square)
        print(ids, Choosen, tehditfulls, fulls)

        if square.onIt.color == 'beyaz':
            for e in kareler:
                if e.id[4] in ids and e.id[4] in Stnew:
                    print(e.id[4], 'Silindi')
                    ids.remove(e.id[4])
        else:
            for e in kareler:
                if e.id[4] in ids and e.id[4] in Btnew:
                    print(e.id[4], 'Silindi')
                    ids.remove(e.id[4])

        for elements in squares:
            if elements[4] in ids:
                elements[5] = True
            else:
                pass

        for elements in squares:
            if elements[4] in tehditfulls:
                elements[6] = True
            else:
                pass

        for elements in squares:
            if elements[6]:
                print(elements)

        square.id[6] = False  # Bu keninin anlık olarak tehdit edildiğini gösteriyor Şah çekme mekaniğinde kullnacağız

        ids.clear()
        Sthreats.clear()
        Btnew.clear()
        Bthreats.clear()
        Stnew.clear()
        fulls.clear()
        tehditfulls.clear()

    def press_again(self):
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

        ids.clear()
        Choosen.clear()
        tehditfulls.clear()
        fulls.clear()
        print(ids, Choosen, fulls)


# PIECES
SF1 = Fil('siyah', True, c8[0], c8[2], 'black', BB)
SF2 = Fil('siyah', True, f8[0], f8[2], 'white', BB)
BF1 = Fil('beyaz', True, c1[0], c1[2], 'white', WB)
BF2 = Fil('beyaz', True, f1[0], f1[2], 'black', WB)
SK1 = Kale('siyah', True, a8[0], a8[2], BR)
SK2 = Kale('siyah', True, h8[0], h8[2], BR)
BK1 = Kale('beyaz', True, a1[0], a1[2], WR)
BK2 = Kale('beyaz', True, h1[0], h1[2], WR)
BV = Vezir('beyaz', True, d1[0], d1[2], WQ)
SV = Vezir('siyah', True, d8[0], d8[2], BQ)
SA1 = At('siyah', True, b8[0], b8[2], BKN)
SA2 = At('siyah', True, g8[0], g8[2], BKN)
BA1 = At('beyaz', True, g1[0], g1[2], WKN)
BA2 = At('beyaz', True, b1[0], b1[2], WKN)
BS = Şah('beyaz', True, e1[0], e1[2], WK)
SS = Şah('siyah', True, e8[0], e8[2], BK)

pieces = [SF1, SF2, BF1, BF2, SK1, SK2, BV, SA1, SA2, SS, BK1, BK2, BA1, BA2, BS, SV]


# FUNCTIONS
def delChoosen():
    Choosen.clear()


def del_dup(test_list):
    return list(dict.fromkeys(test_list))


# SQUARES
class Kareler(object):
    def __init__(self, situation, onIt, id):
        self.situation = situation
        self.onIt = onIt
        self.id = id

    def change_onIt(self, onIt):
        self.onIt = onIt

    def change_sit(self, situation):
        self.situation = situation


A1 = Kareler('full', BK1, a1)
A2 = Kareler('empty', 'Empty', a2)
A3 = Kareler('empty', 'Empty', a3)
A4 = Kareler('empty', 'Empty', a4)
A5 = Kareler('empty', 'Empty', a5)
A6 = Kareler('empty', 'Empty', a6)
A7 = Kareler('empty', 'Empty', a7)
A8 = Kareler('empty', SK1, a8)

B1 = Kareler('empty', BA2, b1)
B2 = Kareler('empty', 'Empty', b2)
B3 = Kareler('empty', 'Empty', b3)
B4 = Kareler('empty', 'Empty', b4)
B5 = Kareler('empty', 'Empty', b5)
B6 = Kareler('empty', 'Empty', b6)
B7 = Kareler('empty', 'Empty', b7)
B8 = Kareler('empty', SA1, b8)

C1 = Kareler('empty', BF1, c1)
C2 = Kareler('empty', 'Empty', c2)
C3 = Kareler('empty', 'Empty', c3)
C4 = Kareler('empty', 'Empty', c4)
C5 = Kareler('empty', 'Empty', c5)
C6 = Kareler('empty', 'Empty', c6)
C7 = Kareler('empty', 'Empty', c7)
C8 = Kareler('empty', SF1, c8)

D1 = Kareler('empty', BV, d1)
D2 = Kareler('empty', 'Empty', d2)
D3 = Kareler('empty', 'Empty', d3)
D4 = Kareler('empty', 'Empty', d4)
D5 = Kareler('empty', 'Empty', d5)
D6 = Kareler('empty', 'Empty', d6)
D7 = Kareler('empty', 'Empty', d7)
D8 = Kareler('empty', SV, d8)

E1 = Kareler('empty', BS, e1)
E2 = Kareler('empty', 'Empty', e2)
E3 = Kareler('empty', 'Empty', e3)
E4 = Kareler('empty', 'Empty', e4)
E5 = Kareler('empty', 'Empty', e5)
E6 = Kareler('empty', 'Empty', e6)
E7 = Kareler('empty', 'Empty', e7)
E8 = Kareler('empty', SS, e8)

F1 = Kareler('empty', BF2, f1)
F2 = Kareler('empty', 'Empty', f2)
F3 = Kareler('empty', 'Empty', f3)
F4 = Kareler('empty', 'Empty', f4)
F5 = Kareler('empty', 'Empty', f5)
F6 = Kareler('empty', 'Empty', f6)
F7 = Kareler('empty', 'Empty', f7)
F8 = Kareler('empty', SF2, f8)

G1 = Kareler('empty', BA1, g1)
G2 = Kareler('empty', 'Empty', g2)
G3 = Kareler('empty', 'Empty', g3)
G4 = Kareler('empty', 'Empty', g4)
G5 = Kareler('empty', 'Empty', g5)
G6 = Kareler('empty', 'Empty', g6)
G7 = Kareler('empty', 'Empty', g7)
G8 = Kareler('empty', SA2, g8)

H1 = Kareler('empty', BK2, h1)
H2 = Kareler('empty', 'Empty', h2)
H3 = Kareler('empty', 'Empty', h3)
H4 = Kareler('empty', 'Empty', h4)
H5 = Kareler('empty', 'Empty', h5)
H6 = Kareler('empty', 'Empty', h6)
H7 = Kareler('empty', 'Empty', h7)
H8 = Kareler('empty', SK2, h8)

kareler = [A1, A2, A3, A4, A5, A6, A7, A8, B1, B2, B3, B4, B5, B6, B7, B8, C1, C2, C3, C4, C5, C6, C7, C8, D1, D2, D3,
           D4, D5, D6, D7, D8, E1, E2, E3, E4, E5, E6, E7, E8, F1, F2, F3, F4, F5, F6, F7, F8, G1, G2, G3, G4, G5, G6,
           G7, G8, H1, H2, H3, H4, H5, H6, H7, H8]

beyazlar = [A1, A3, A5, A7, B2, B4, B6, B8, C1, C3, C5, C7, D2, D4, D6, D8, E1, E3, E5, E7, F2, F4, F6, F8, G1, G3, G5,
            G7, H2, H4, H6, H8]

siyahlar = [A2, A4, A6, A8, B1, B3, B5, B7, C2, C4, C6, C8, D1, D3, D5, D7, E2, E4, E6, E8, F1, F3, F5, F7, G2, G4, G6,
            G8, H1, H3, H5, H7]
