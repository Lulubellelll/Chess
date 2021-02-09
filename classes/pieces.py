from .squares import *
from .images import *

# LISTS
ids = []
Choosen = []
fulls = []
tehditfulls = []

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


class Fil(Pieces):
    def __init__(self, color, alive, posx, posy, scolor, img):
        super().__init__(color, alive, posx, posy, img)
        self.scolor = scolor

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


# PIECES
SF = Fil('siyah', True, a2[0], a2[2], 'black', BB)
BF = Fil('beyaz', True, d5[0], d5[2], 'black', WB)

pieces = [SF, BF]


# FUNCTIONS
def delChoosen():
    Choosen.clear()

def del_dup(test_list):
    return list(set(test_list))


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

A1 = Kareler('full', 'Empty', a1)
A2 = Kareler('empty', SF, a2)
A3 = Kareler('empty', 'Empty', a3)
A4 = Kareler('empty', 'Empty', a4)
A5 = Kareler('empty', 'Empty', a5)
A6 = Kareler('empty', 'Empty', a6)
A7 = Kareler('empty', 'Empty', a7)
A8 = Kareler('empty', 'Empty', a8)

B1 = Kareler('empty', 'Empty', b1)
B2 = Kareler('empty', 'Empty', b2)
B3 = Kareler('empty', 'Empty', b3)
B4 = Kareler('empty', 'Empty', b4)
B5 = Kareler('empty', 'Empty', b5)
B6 = Kareler('empty', 'Empty', b6)
B7 = Kareler('empty', 'Empty', b7)
B8 = Kareler('empty', 'Empty', b8)

C1 = Kareler('empty', 'Empty', c1)
C2 = Kareler('empty', 'Empty', c2)
C3 = Kareler('empty', 'Empty', c3)
C4 = Kareler('empty', 'Empty', c4)
C5 = Kareler('empty', 'Empty', c5)
C6 = Kareler('empty', 'Empty', c6)
C7 = Kareler('empty', 'Empty', c7)
C8 = Kareler('empty', 'Empty', c8)

D1 = Kareler('empty', 'Empty', d1)
D2 = Kareler('empty', 'Empty', d2)
D3 = Kareler('empty', 'Empty', d3)
D4 = Kareler('empty', 'Empty', d4)
D5 = Kareler('empty', BF, d5)
D6 = Kareler('empty', 'Empty', d6)
D7 = Kareler('empty', 'Empty', d7)
D8 = Kareler('empty', 'Empty', d8)

E1 = Kareler('empty', 'Empty', e1)
E2 = Kareler('empty', 'Empty', e2)
E3 = Kareler('empty', 'Empty', e3)
E4 = Kareler('empty', 'Empty', e4)
E5 = Kareler('empty', 'Empty', e5)
E6 = Kareler('empty', 'Empty', e6)
E7 = Kareler('empty', 'Empty', e7)
E8 = Kareler('empty', 'Empty', e8)

F1 = Kareler('empty', 'Empty', f1)
F2 = Kareler('empty', 'Empty', f2)
F3 = Kareler('empty', 'Empty', f3)
F4 = Kareler('empty', 'Empty', f4)
F5 = Kareler('empty', 'Empty', f5)
F6 = Kareler('empty', 'Empty', f6)
F7 = Kareler('empty', 'Empty', f7)
F8 = Kareler('empty', 'Empty', f8)

G1 = Kareler('empty', 'Empty', g1)
G2 = Kareler('empty', 'Empty', g2)
G3 = Kareler('empty', 'Empty', g3)
G4 = Kareler('empty', 'Empty', g4)
G5 = Kareler('empty', 'Empty', g5)
G6 = Kareler('empty', 'Empty', g6)
G7 = Kareler('empty', 'Empty', g7)
G8 = Kareler('empty', 'Empty', g8)

H1 = Kareler('empty', 'Empty', h1)
H2 = Kareler('empty', 'Empty', h2)
H3 = Kareler('empty', 'Empty', h3)
H4 = Kareler('empty', 'Empty', h4)
H5 = Kareler('empty', 'Empty', h5)
H6 = Kareler('empty', 'Empty', h6)
H7 = Kareler('empty', 'Empty', h7)
H8 = Kareler('empty', 'Empty', h8)

kareler = [A1, A2, A3, A4, A5, A6, A7, A8, B1, B2, B3, B4, B5, B6, B7, B8, C1, C2, C3, C4, C5, C6, C7, C8, D1, D2, D3,
           D4, D5, D6, D7, D8, E1, E2, E3, E4, E5, E6, E7, E8, F1, F2, F3, F4, F5, F6, F7, F8, G1, G2, G3, G4, G5, G6,
           G7, G8, H1, H2, H3, H4, H5, H6, H7, H8]
