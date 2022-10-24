from poker import *


class Range:
    def __init__(self):
        self.utg = self.UTG()
        self.hj = self.HJ()
        self.co = self.CO()
        self.btn = self.BTN()
        self.sb = self.SB()
        self.tbet = self.TBet()
        self.tb_rock = self.TB_rock()
        self.md_def = self.MD_def()

    def UTG(self):
        rg = get_blank_range()
        for i in range(13):
            for j in range(13):
                if i == 0:
                    rg[i][j] = 24
                if i == 1 and j <= 5:
                    rg[i][j] = 24
                if i == 2 and j <= 4:
                    rg[i][j] = 24
                if i <= 10 and i == j:
                    rg[i][j] = 24
                if i <= 8 and j == i + 1:  # 同色连张
                    rg[i][j] = 24
        rg[3][0] = 24  # AJo
        return rg

    def HJ(self):
        rg = self.UTG()
        rg[1][6] = 24
        rg[2][5] = 24
        rg[3][1] = 24
        rg[3][2] = 24
        rg[3][5] = 24
        rg[4][0] = 24
        return rg

    def CO(self):
        rg = self.HJ()
        rg[1][7] = 24
        rg[1][8] = 24
        rg[1][9] = 24
        rg[2][6] = 24
        rg[2][7] = 24
        rg[3][6] = 24
        rg[3][7] = 24
        rg[4][6] = 24
        rg[5][7] = 24
        rg[6][8] = 24
        rg[11][11] = 24
        rg[12][12] = 24
        rg[4][1] = 24
        rg[4][2] = 24
        rg[4][3] = 24
        rg[5][0] = 24
        return rg

    def BTN(self):
        rg = self.CO()
        for i in range(13):
            for j in range(13):
                if i == 2 and j != 12:
                    rg[i][j] = 24
                if i == 3 and j <= 10:
                    rg[i][j] = 24
                if j == 0 or i == 1:
                    rg[i][j] = 24
                if j == 1 and i <= 6:
                    rg[i][j] = 24
                if i == 5 and j <= 8:
                    rg[i][j] = 24
                if i <= 8 and j == i + 2:
                    rg[i][j] = 24
        return rg

    def SB(self):
        rg = self.BTN()
        rg[2][12] = 24
        rg[3][10] = 24
        rg[9][11] = 24
        rg[10][11] = 24
        return rg

    def TBet(self):
        rg = get_blank_range()
        for i in range(13):
            for j in range(13):
                if i in (0, 1) and j <= 2:
                    rg[i][j] = 24
                if j in (3, 4) and i <= j:
                    rg[i][j] = 12

                if (i == j or i == j + 1) and 4 < i <= 10:
                    rg[i][j] = 6
        rg[2][2] = 24
        rg[0][9] = 12
        rg[0][10] = 12
        rg[0][11] = 6
        rg[1][9] = 12
        return rg

    def TB_rock(self):
        rg = get_blank_range()
        for i in range(13):
            for j in range(13):
                if i in (0, 1, 2) and j <= 4:
                    rg[i][j] = 24
        rg[2][1] = 0
        rg[3][3] = 24
        rg[4][4] = 24
        rg[3][4] = 24
        rg[4][5] = 24
        rg[5][5] = 24
        rg[0][9] = 24
        rg[0][10] = 24
        return rg

    def TB_thief(self):
        rg = get_blank_range()
        for i in range(13):
            for j in range(13):
                if i <= 3 and j <= 6:
                    rg[i][j] = 24
                if j == 6 and i <= j:
                    rg[i][j] = 12
                if j == 7 and 2 < i <= j:
                    rg[i][j] = 12
                if i == 1 and j in (8, 9, 10):
                    rg[i][j] = 12
        rg[7][8] = 12
        rg[7][9] = 12
        rg[8][9] = 12
        rg[8][10] = 12
        rg[9][10] = 12
        return rg

    def BB_3B(self):
        rg = self.TBet[:]
        for i in range(13):
            for j in range(13):
                if 9 >= i >= 5 and j == i + 1:
                    rg[i][j] = 12
        rg[4][4] = 12
        rg[5][5] = 12
        rg[4][6] = 12
        rg[5][7] = 12
        return rg

    def BB_def(self):
        rg = get_blank_range()
        for i in range(13):
            for j in range(13):
                if i <= 2:
                    rg[i][j] = 24
                if i in (3, 4) and j <= 8:
                    rg[i][j] = 24
                if i == 5 and j <= 9:
                    rg[i][j] = 24
                if j <= i <= j + 3:
                    rg[i][j] = 24

        rg[7][0] = 12
        rg[6][1] = 0
        rg[6][2] = 0
        rg[7][10] = 24
        rg1 = self.BB_3B()
        for i in range(13):
            for j in range(13):
                rg[i][j] = rg[i][j] - rg1[i][j]
        return rg

    def MD_def(self):
        rg = self.CO()
        rg1 = self.TBet()
        for i in range(13):
            for j in range(13):
                rg[i][j] = rg[i][j] - rg1[i][j]
                if j in (0, 1) and i >= 5:
                    rg[i][j] = 0
                if i in (1, 2, 3) and j >= i + 2:
                    rg[i][j] = 0
                if i in (1, 2) and i < j <= i + 2:
                    rg[i][j] = 24

        rg[0][2] = 12
        rg[3][4] = 24
        rg[3][5] = 24

        return rg

