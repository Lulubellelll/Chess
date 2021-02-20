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
    def __init__(self, color, alive, posx, posy, img, pressed):
        self.color = color
        self.alive = alive
        self.posx = posx
        self.posy = posy
        self.img = img
        self.pressed = pressed

    def death(self):
        self.alive = False


class Kale(Pieces):
    def __init__(self, color, alive, posx, posy, img, pressed):
        super().__init__(color, alive, posx, posy, img, pressed)

    def threat(self, id, square):

        sat = (id // 8) + 1
        süt = (id % 8) + 1

        for x in kareler:
            if x.onIt != 'Empty':
                fulls.append(x.id[4])

        # Sağ
        for i in range(1, 9 - süt):
            if (id + 1 * i) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 1 * i)
                else:
                    Sthreats.append(id + 1 * i)
                break
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 1 * i)
                else:
                    Sthreats.append(id + 1 * i)

        # Sol
        for i in range(1, süt):
            if (id - 1 * i) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 1 * i)
                else:
                    Sthreats.append(id - 1 * i)
                break
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 1 * i)
                else:
                    Sthreats.append(id - 1 * i)

        # Aşşağı
        for i in range(1, sat):
            if (id - 8 * i) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 8 * i)
                else:
                    Sthreats.append(id - 8 * i)
                break
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 8 * i)
                else:
                    Sthreats.append(id - 8 * i)

        # Yukarı
        for i in range(1, 9 - sat):
            if (id + 8 * i) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 8 * i)
                else:
                    Sthreats.append(id + 8 * i)
                break
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 8 * i)
                else:
                    Sthreats.append(id + 8 * i)

        fulls.clear()

    def press(self, id, square):
        print(ids)

        self.pressed = True

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
        Sthreats.clear()
        Btnew.clear()
        Bthreats.clear()
        Stnew.clear()
        fulls.clear()
        tehditfulls.clear()

    def press_again(self):

        self.pressed = False

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
    def __init__(self, color, alive, posx, posy, scolor, img, pressed):
        super().__init__(color, alive, posx, posy, img, pressed)
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
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id + 9 * i)
                    else:
                        Sthreats.append(id + 9 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id + 9 * i)
                    else:
                        Sthreats.append(id + 9 * i)

        else:
            for i in range(1, (8 - süt) + 1):
                if (id + 9 * i) in fulls:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id + 9 * i)
                    else:
                        Sthreats.append(id + 9 * i)
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
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id - 9 * i)
                    else:
                        Sthreats.append(id - 9 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id - 9 * i)
                    else:
                        Sthreats.append(id - 9 * i)
        else:
            for i in range(1, sat):
                if (id - 9 * i) in fulls:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id - 9 * i)
                    else:
                        Sthreats.append(id - 9 * i)
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
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id + 7 * i)
                    else:
                        Sthreats.append(id + 7 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id + 7 * i)
                    else:
                        Sthreats.append(id + 7 * i)
        else:
            for i in range(1, süt):
                if (id + 7 * i) in fulls:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id + 7 * i)
                    else:
                        Sthreats.append(id + 7 * i)
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
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id - 7 * i)
                    else:
                        Sthreats.append(id - 7 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id - 7 * i)
                    else:
                        Sthreats.append(id - 7 * i)

        else:
            for i in range(1, sat):
                if (id - 7 * i) in fulls:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id - 7 * i)
                    else:
                        Sthreats.append(id - 7 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id - 7 * i)
                    else:
                        Sthreats.append(id - 7 * i)

        fulls.clear()

    def press(self, id, square):
        print(ids)

        self.pressed = True

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
        Sthreats.clear()
        Btnew.clear()
        Bthreats.clear()
        Stnew.clear()
        fulls.clear()
        tehditfulls.clear()

    def press_again(self):

        self.pressed = False

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
    def __init__(self, color, alive, posx, posy, img, pressed):
        super().__init__(color, alive, posx, posy, img, pressed)

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
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id + 9 * i)
                    else:
                        Sthreats.append(id + 9 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id + 9 * i)
                    else:
                        Sthreats.append(id + 9 * i)
        else:
            for i in range(1, (8 - süt) + 1):
                if (id + 9 * i) in fulls:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id + 9 * i)
                    else:
                        Sthreats.append(id + 9 * i)
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
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id - 9 * i)
                    else:
                        Sthreats.append(id - 9 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id - 9 * i)
                    else:
                        Sthreats.append(id - 9 * i)
        else:
            for i in range(1, sat):
                if (id - 9 * i) in fulls:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id - 9 * i)
                    else:
                        Sthreats.append(id - 9 * i)
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
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id + 7 * i)
                    else:
                        Sthreats.append(id + 7 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id + 7 * i)
                    else:
                        Sthreats.append(id + 7 * i)
        else:
            for i in range(1, süt):
                if (id + 7 * i) in fulls:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id + 7 * i)
                    else:
                        Sthreats.append(id + 7 * i)
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
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id - 7 * i)
                    else:
                        Sthreats.append(id - 7 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id - 7 * i)
                    else:
                        Sthreats.append(id - 7 * i)
        else:
            for i in range(1, sat):
                if (id - 7 * i) in fulls:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id - 7 * i)
                    else:
                        Sthreats.append(id - 7 * i)
                    break
                else:
                    if square.onIt.color == 'beyaz':
                        Bthreats.append(id - 7 * i)
                    else:
                        Sthreats.append(id - 7 * i)

        # Sağ
        for i in range(1, 9 - süt):
            if (id + 1 * i) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 1 * i)
                else:
                    Sthreats.append(id + 1 * i)
                break
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 1 * i)
                else:
                    Sthreats.append(id + 1 * i)

        # Sol
        for i in range(1, süt):
            if (id - 1 * i) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 1 * i)
                else:
                    Sthreats.append(id - 1 * i)
                break
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 1 * i)
                else:
                    Sthreats.append(id - 1 * i)

        # Aşşağı
        for i in range(1, sat):
            if (id - 8 * i) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 8 * i)
                else:
                    Sthreats.append(id - 8 * i)
                break
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 8 * i)
                else:
                    Sthreats.append(id - 8 * i)

        # Yukarı
        for i in range(1, 9 - sat):
            if (id + 8 * i) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 8 * i)
                else:
                    Sthreats.append(id + 8 * i)
                break
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 8 * i)
                else:
                    Sthreats.append(id + 8 * i)

        fulls.clear()

    def press(self, id, square):
        print(ids)

        self.pressed = True

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
        Sthreats.clear()
        Btnew.clear()
        Bthreats.clear()
        Stnew.clear()
        fulls.clear()
        tehditfulls.clear()

    def press_again(self):

        self.pressed = False

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
    def __init__(self, color, alive, posx, posy, img, pressed):
        super().__init__(color, alive, posx, posy, img, pressed)

    def threat(self, id, square):

        sat = (id // 8) + 1
        süt = (id % 8) + 1

        for x in kareler:
            if x.onIt != 'Empty':
                fulls.append(x.id[4])

        # Yukarı
        if sat != 7 and sat != 8 and süt != 8:
            if (id + 17) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 17)
                else:
                    Sthreats.append(id + 17)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 17)
                else:
                    Sthreats.append(id + 17)

        if sat != 7 and sat != 8 and süt != 1:
            if (id + 15) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 15)
                else:
                    Sthreats.append(id + 15)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 15)
                else:
                    Sthreats.append(id + 15)

        # Aşşağı
        if sat != 1 and sat != 2 and süt != 1:
            if (id - 17) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 17)
                else:
                    Sthreats.append(id - 17)
                pass
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 17)
                else:
                    Sthreats.append(id - 17)

        if sat != 1 and sat != 2 and süt != 8:
            if (id - 15) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 15)
                else:
                    Sthreats.append(id - 15)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 15)
                else:
                    Sthreats.append(id - 15)

        # Sol
        if süt != 1 and süt != 2 and sat != 1:
            if (id - 10) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 10)
                else:
                    Sthreats.append(id - 10)
                pass
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 10)
                else:
                    Sthreats.append(id - 10)

        if süt != 1 and süt != 2 and sat != 8:
            if (id + 6) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 6)
                else:
                    Sthreats.append(id + 6)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 6)
                else:
                    Sthreats.append(id + 6)

        # Sağ
        if süt != 7 and süt != 8 and sat != 1:
            if (id - 6) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 6)
                else:
                    Sthreats.append(id - 6)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 6)
                else:
                    Sthreats.append(id - 6)

        if süt != 7 and süt != 8 and sat != 8:
            if (id + 10) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 10)
                else:
                    Sthreats.append(id + 10)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 10)
                else:
                    Sthreats.append(id + 10)

        fulls.clear()

    def press(self, id, square):
        print(ids)

        self.pressed = True

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
        Sthreats.clear()
        Btnew.clear()
        Bthreats.clear()
        Stnew.clear()
        fulls.clear()
        tehditfulls.clear()

    def press_again(self):

        self.pressed = False

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


class Sah(Pieces):
    def __init__(self, color, alive, posx, posy, img, threatened, pressed):
        super().__init__(color, alive, posx, posy, img, pressed)
        self.threatened = threatened

    def true_thr(self):
        self.threatened = True

    def false_thr(self):
        self.threatened = False

    def threat(self, id, square):



        sat = (id // 8) + 1
        süt = (id % 8) + 1

        for x in kareler:
            if x.onIt != 'Empty':
                fulls.append(x.id[4])

        # Sağ
        if süt != 8:
            if (id + 1) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 1)
                else:
                    Sthreats.append(id + 1)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 1)
                else:
                    Sthreats.append(id + 1)

        # Sağ Yukarı
        if süt != 8 and sat != 8:
            if (id + 9) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 9)
                else:
                    Sthreats.append(id + 9)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 9)
                else:
                    Sthreats.append(id + 9)

        # Sağ Aşşağı
        if süt != 8 and sat != 1:
            if (id - 7) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 7)
                else:
                    Sthreats.append(id - 7)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 7)
                else:
                    Sthreats.append(id - 7)

        # Sol
        if süt != 1:
            if (id + 1) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 1)
                else:
                    Sthreats.append(id - 1)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 1)
                else:
                    Sthreats.append(id - 1)

        # Sol Yukarı
        if süt != 1 and sat != 8:
            if (id + 7) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 7)
                else:
                    Sthreats.append(id + 7)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 7)
                else:
                    Sthreats.append(id + 7)

        # Sol Aşşağı
        if süt != 1 and sat != 1:
            if (id - 9) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 9)
                else:
                    Sthreats.append(id - 9)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 9)
                else:
                    Sthreats.append(id - 9)

        # Aşşağı
        if sat != 1:
            if (id - 8) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 8)
                else:
                    Sthreats.append(id - 8)
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 8)
                else:
                    Sthreats.append(id - 8)

        # Yukarı
        if sat != 8:
            if (id + 8) in fulls:
                pass
            else:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 8)
                else:
                    Sthreats.append(id + 8)

        fulls.clear()

    def press(self, id, square):

        self.pressed = True

        sat = (id // 8) + 1
        süt = (id % 8) + 1

        defthreats()

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
                    ids.remove(e.id[4])
        else:
            for e in kareler:
                if e.id[4] in ids and e.id[4] in Btnew:
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

        ids.clear()
        Sthreats.clear()
        Btnew.clear()
        Bthreats.clear()
        Stnew.clear()
        fulls.clear()
        tehditfulls.clear()

    def press_again(self):

        self.pressed = False

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


class Piyon(Pieces):
    def __init__(self, color, alive, posx, posy, img, firstMove, pressed):
        super().__init__(color, alive, posx, posy, img, pressed)
        self.firstMove = firstMove

    def threat(self, id, square):

        sat = (id // 8) + 1
        süt = (id % 8) + 1

        for x in kareler:
            if x.onIt != 'Empty':
                fulls.append(x.id[4])

        if square.onIt.color == 'beyaz':
            # Sağ Yukarı
            if (id + 9) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 9)
                else:
                    Sthreats.append(id + 9)

            # Sol Yukarı
            if (id + 7) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id + 7)
                else:
                    Sthreats.append(id + 7)
        else:
            # Sağ Yukarı
            if (id - 9) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 9)
                else:
                    Sthreats.append(id - 9)

            # Sol Yukarı
            if (id + 7) in fulls:
                if square.onIt.color == 'beyaz':
                    Bthreats.append(id - 7)
                else:
                    Sthreats.append(id - 7)

        fulls.clear()

    def press(self, id, square):
        print(ids)

        self.pressed = True

        sat = (id // 8) + 1
        süt = (id % 8) + 1

        print('sat: ', sat)
        print('süt: ', süt)

        for x in kareler:
            if x.onIt != 'Empty':
                fulls.append(x.id[4])

        print(fulls)

        if square.onIt.color == 'beyaz':
            # Yukarı
            if square.onIt.firstMove:
                for x in range(1, 3):
                    if (id + 8 * x) in fulls:
                        break
                    else:
                        ids.append(id + 8 * x)
            else:
                if (id + 8) in fulls:
                    pass
                else:
                    ids.append(id + 8)

            # Sol Yukarı
            if (id + 7) in fulls:
                tehditfulls.append(id + 7)

            # Sağ Yukarı
            if (id + 9) in fulls:
                tehditfulls.append(id + 9)
        else:
            # Yukarı
            if square.onIt.firstMove:
                for x in range(1, 3):
                    if (id - 8 * x) in fulls:
                        break
                    else:
                        ids.append(id - 8 * x)
            else:
                if (id - 8) in fulls:
                    pass
                else:
                    ids.append(id - 8)

            # Sol Yukarı
            if (id - 7) in fulls:
                tehditfulls.append(id - 7)

            # Sağ Yukarı
            if (id - 9) in fulls:
                tehditfulls.append(id - 9)

        if self.firstMove:
            self.firstMove = False

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
        Sthreats.clear()
        Btnew.clear()
        Bthreats.clear()
        Stnew.clear()
        fulls.clear()
        tehditfulls.clear()

    def press_again(self):

        self. pressed = False

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

        if not self.firstMove:
            self.firstMove = True

        ids.clear()
        Choosen.clear()
        tehditfulls.clear()
        fulls.clear()
        print(ids, Choosen, fulls)


# PIECES
SF1 = Fil('siyah', True, c8[0], c8[2], 'black', BB, False)
SF2 = Fil('siyah', True, f8[0], f8[2], 'white', BB, False)
BF1 = Fil('beyaz', True, c1[0], c1[2], 'white', WB, False)
BF2 = Fil('beyaz', True, f1[0], f1[2], 'black', WB, False)

SK1 = Kale('siyah', True, a8[0], a8[2], BR, False)
SK2 = Kale('siyah', True, h8[0], h8[2], BR, False)
BK1 = Kale('beyaz', True, a1[0], a1[2], WR, False)
BK2 = Kale('beyaz', True, h1[0], h1[2], WR, False)
BV = Vezir('beyaz', True, d1[0], d1[2], WQ, False)
SV = Vezir('siyah', True, d8[0], d8[2], BQ, False)

SA1 = At('siyah', True, b8[0], b8[2], BKN, False)
SA2 = At('siyah', True, g8[0], g8[2], BKN, False)
BA1 = At('beyaz', True, g1[0], g1[2], WKN, False)
BA2 = At('beyaz', True, b1[0], b1[2], WKN, False)

BS = Sah('beyaz', True, e1[0], e1[2], WK, False, False)
SS = Sah('siyah', True, e8[0], e8[2], BK, False, False)

BP1 = Piyon('beyaz', True, a2[0], a2[2], WP, True, False)
BP2 = Piyon('beyaz', True, b2[0], b2[2], WP, True, False)
BP3 = Piyon('beyaz', True, c2[0], c2[2], WP, True, False)
BP4 = Piyon('beyaz', True, d2[0], d2[2], WP, True, False)
BP5 = Piyon('beyaz', True, e2[0], e2[2], WP, True, False)
BP6 = Piyon('beyaz', True, f2[0], f2[2], WP, True, False)
BP7 = Piyon('beyaz', True, g2[0], g2[2], WP, True, False)
BP8 = Piyon('beyaz', True, h2[0], h2[2], WP, True, False)
SP1 = Piyon('siyah', True, a7[0], a7[2], BP, True, False)
SP2 = Piyon('siyah', True, b7[0], b7[2], BP, True, False)
SP3 = Piyon('siyah', True, c7[0], c7[2], BP, True, False)
SP4 = Piyon('siyah', True, d7[0], d7[2], BP, True, False)
SP5 = Piyon('siyah', True, e7[0], e7[2], BP, True, False)
SP6 = Piyon('siyah', True, f7[0], f7[2], BP, True, False)
SP7 = Piyon('siyah', True, g7[0], g7[2], BP, True, False)
SP8 = Piyon('siyah', True, h7[0], h7[2], BP, True, False)


pieces = [SF1, SF2, BF1, BF2, SK1, SK2, BV, SA1, SA2, SS, BK1, BK2, BA1, BA2, BS, SV, BP1, BP2,
          BP3, BP4, BP5, BP6, BP7, BP8, SP1, SP2, SP3, SP4, SP5, SP6, SP7, SP8]


# FUNCTIONS
def delChoosen():
    Choosen.clear()


def del_dup(test_list):
    return list(dict.fromkeys(test_list))


def defthreats():
    global Sthreats
    global Bthreats

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
    print('Stnew:', Stnew)

    Bthreats = Btnew
    print('Btnew:', Btnew)


# SQUARES
class Kareler(object):
    def __init__(self, situation, onIt, id, chose, chosen):
        self.situation = situation
        self.onIt = onIt
        self.id = id
        self.chose = chose
        self.chosen = chosen

    def change_onIt(self, onIt):
        self.onIt = onIt

    def change_sit(self, situation):
        self.situation = situation


A1 = Kareler('empty', BK1, a1, False, False)
A2 = Kareler('empty', BP1, a2, False, False)
A3 = Kareler('empty', 'Empty', a3, False, False)
A4 = Kareler('empty', 'Empty', a4, False, False)
A5 = Kareler('empty', 'Empty', a5, False, False)
A6 = Kareler('empty', 'Empty', a6, False, False)
A7 = Kareler('empty', SP1, a7, False, False)
A8 = Kareler('empty', SK1, a8, False, False)

B1 = Kareler('empty', BA2, b1, False, False)
B2 = Kareler('empty', BP2, b2, False, False)
B3 = Kareler('empty', 'Empty', b3, False, False)
B4 = Kareler('empty', 'Empty', b4, False, False)
B5 = Kareler('empty', 'Empty', b5, False, False)
B6 = Kareler('empty', 'Empty', b6, False, False)
B7 = Kareler('empty', SP2, b7, False, False)
B8 = Kareler('empty', SA1, b8, False, False)

C1 = Kareler('empty', BF1, c1, False, False)
C2 = Kareler('empty', BP3, c2, False, False)
C3 = Kareler('empty', 'Empty', c3, False, False)
C4 = Kareler('empty', 'Empty', c4, False, False)
C5 = Kareler('empty', 'Empty', c5, False, False)
C6 = Kareler('empty', 'Empty', c6, False, False)
C7 = Kareler('empty', SP3, c7, False, False)
C8 = Kareler('empty', SF1, c8, False, False)

D1 = Kareler('empty', BV, d1, False, False)
D2 = Kareler('empty', BP4, d2, False, False)
D3 = Kareler('empty', 'Empty', d3, False, False)
D4 = Kareler('empty', 'Empty', d4, False, False)
D5 = Kareler('empty', 'Empty', d5, False, False)
D6 = Kareler('empty', 'Empty', d6, False, False)
D7 = Kareler('empty', SP4, d7, False, False)
D8 = Kareler('empty', SV, d8, False, False)

E1 = Kareler('empty', BS, e1, False, False)
E2 = Kareler('empty', BP5, e2, False, False)
E3 = Kareler('empty', 'Empty', e3, False, False)
E4 = Kareler('empty', 'Empty', e4, False, False)
E5 = Kareler('empty', 'Empty', e5, False, False)
E6 = Kareler('empty', 'Empty', e6, False, False)
E7 = Kareler('empty', SP5, e7, False, False)
E8 = Kareler('empty', SS, e8, False, False)

F1 = Kareler('empty', BF2, f1, False, False)
F2 = Kareler('empty', BP6, f2, False, False)
F3 = Kareler('empty', 'Empty', f3, False, False)
F4 = Kareler('empty', 'Empty', f4, False, False)
F5 = Kareler('empty', 'Empty', f5, False, False)
F6 = Kareler('empty', 'Empty', f6, False, False)
F7 = Kareler('empty', SP6, f7, False, False)
F8 = Kareler('empty', SF2, f8, False, False)

G1 = Kareler('empty', BA1, g1, False, False)
G2 = Kareler('empty', BP7, g2, False, False)
G3 = Kareler('empty', 'Empty', g3, False, False)
G4 = Kareler('empty', 'Empty', g4, False, False)
G5 = Kareler('empty', 'Empty', g5, False, False)
G6 = Kareler('empty', 'Empty', g6, False, False)
G7 = Kareler('empty', SP7, g7, False, False)
G8 = Kareler('empty', SA2, g8, False, False)

H1 = Kareler('empty', BK2, h1, False, False)
H2 = Kareler('empty', BP8, h2, False, False)
H3 = Kareler('empty', 'Empty', h3, False, False)
H4 = Kareler('empty', 'Empty', h4, False, False)
H5 = Kareler('empty', 'Empty', h5, False, False)
H6 = Kareler('empty', 'Empty', h6, False, False)
H7 = Kareler('empty', SP8, h7, False, False)
H8 = Kareler('empty', SK2, h8, False, False)

kareler = [A1, A2, A3, A4, A5, A6, A7, A8, B1, B2, B3, B4, B5, B6, B7, B8, C1, C2, C3, C4, C5, C6, C7, C8, D1, D2, D3,
           D4, D5, D6, D7, D8, E1, E2, E3, E4, E5, E6, E7, E8, F1, F2, F3, F4, F5, F6, F7, F8, G1, G2, G3, G4, G5, G6,
           G7, G8, H1, H2, H3, H4, H5, H6, H7, H8]

beyazlar = [A1, A3, A5, A7, B2, B4, B6, B8, C1, C3, C5, C7, D2, D4, D6, D8, E1, E3, E5, E7, F2, F4, F6, F8, G1, G3, G5,
            G7, H2, H4, H6, H8]

siyahlar = [A2, A4, A6, A8, B1, B3, B5, B7, C2, C4, C6, C8, D1, D3, D5, D7, E2, E4, E6, E8, F1, F3, F5, F7, G2, G4, G6,
            G8, H1, H3, H5, H7]
