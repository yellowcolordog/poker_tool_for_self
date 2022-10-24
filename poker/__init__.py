import random
import time
import os
import pa

'''
cl:card list
cp:card picture
rl:range list
rp:range picture(图形)
rg:range goal(二维表)
solver_rl: solver 能用的范围格式.
'''


class Poker:
    def __init__(self):
        self.all_card = []
        self.number = []
        for i in range(2, 10):
            self.number.append(str(i))
        self.number.extend(['T', 'J', 'Q', 'K', 'A'])
        self.number.reverse()
        self.color = ['♠', '♥', '♦', '♣']
        self.card_number = {}
        idx = 1
        for n in self.number:
            for s in self.color:
                card = s + n
                self.all_card.append(card)
                self.card_number[card] = idx
                idx += 1
        self.deck = self.all_card[:]
        random.shuffle(self.deck)
        self.all_range = []
        for idx, card1 in enumerate(self.all_card):
            for card2 in self.all_card[idx + 1:]:
                hand = card1 + card2
                self.all_range.append(hand)

        # self.type = 1
        # if self.type == 1:
        self.rg_style = {
            24: '██', 22: '█▉', 20: '█▋', 18: '█▌', 16: '█▍', 14: '█▏',
            12: '█ ', 10: '▉ ', 8: '▋ ', 6: '▌ ', 4: '▍ ', 2: '▏ ', 0: '  '
        }
        # elif self.type == '2':
        #     self.rg_style = {
        #         24:'██',22:'█▓',20:'█▓',18:'█▒',16:'█▒',14:'█░',
        #         12:'█ ',10:'▓ ', 8:'▓ ',6:'▒ ',4:'▒ '2:'░ '
        #     }
        self.rp_rg = {
            '██': 24, '█▉': 22, '█▋': 20, '█▌': 18, '█▍': 16, '█▏': 14,
            '█ ': 12, '▉ ': 10, '▋ ': 8, '▌ ': 6, '▍ ': 4, '▏ ': 2, '  ': 0
        }


P = Poker()
PioSolver_range_path = r'D:\PioSOLVER\Ranges'

def get_blank_range():
    l = []
    for i in range(13):
        l2 = []
        for j in range(13):
            l2.append(0)
        l.append(l2)
    return l


def num_sorted(num,re=True):
    num.sort(key=lambda x:P.number.index(x),reverse=re)


def card_sorted(deck, re=True):
    deck.sort(key=lambda x: P.all_card.index(x), reverse=re)


def range_sorted(rl, type='type0'):
    if type == 'big':
        rl.sort(key=lambda x: P.all_range.index(x))

    def _(hand):
        if hand[1] == hand[3]:
            return 1
        elif hand[0] == hand[2]:
            return 2
        else:
            return 3

    if type == 'type0':
        rl.sort(key=lambda x: P.all_range.index(x))
        rl.sort(key=_)
    if type == 'type1':
        rl.sort(key=lambda x: P.all_range.index(x))
        rl.sort(key=lambda x: P.card_number[x[:2]])
        rl.sort(key=_)


def rl_to_rg(rl):
    rg = get_blank_range()
    for hand in rl:
        pos1 = P.number.index(hand[1])  # position
        pos2 = P.number.index(hand[3])
        if hand[1] == hand[3]:  # 对子
            rg[pos1][pos1] += 4  # 4/24
        elif hand[0] == hand[2]:  # 同色
            rg[pos1][pos2] += 6  # 6/24
        else:
            rg[pos2][pos1] += 2  # 2/24

    return rg


def rg_to_rp(rg):
    rp = ''
    for l1 in rg:
        for goal in l1:
            picture = P.rg_style.get(goal, '  ')
            rp = rp + picture + ' '
        rp += '\n'

    return rp


def rl_to_rp(rl):
    range_sorted(rl)
    rg = rl_to_rg(rl)
    rp = rg_to_rp(rg)
    return rp


def rp_to_rg(rp):
    rp = rp.replace('\n', '')
    rg = get_blank_range()
    for i in range(13):
        for j in range(13):
            picture = rp[:2]
            goal = P.rp_rg[picture]
            rg[i][j] = goal
            rp = rp[3:]
    return rg


def rg_to_rl(rg):
    rl = []
    for i in range(13):
        for j in range(13):
            n1 = P.number[i]
            n2 = P.number[j]
            if i == j:  # 对子
                count = rg[i][j] // 4
                over_count = 0
                for idx, c1 in enumerate(P.color):
                    for c2 in P.color[idx + 1:]:
                        hand = c1 + n1 + c2 + n2
                        if count <= over_count:
                            break
                        over_count += 1
                        rl.append(hand)
                    if count <= over_count:
                        break
            elif i > j:  # 杂色
                n1, n2 = n2, n1
                count = rg[i][j] // 2
                over_count = 0
                for idx1, c1 in enumerate(P.color):
                    for idx2, c2 in enumerate(P.color):
                        if idx1 == idx2: continue
                        hand = c1 + n1 + c2 + n2
                        if count <= over_count:
                            break
                        over_count += 1
                        rl.append(hand)
                    if count <= over_count:
                        break
            else:  # 同色
                count = rg[i][j] // 6
                over_count = 0
                for idx, c1 in enumerate(P.color):
                    hand = c1 + n1 + c1 + n2
                    if count <= over_count:
                        break
                    over_count += 1
                    rl.append(hand)

    return rl


def print_rp(rp):
    picture = '  '
    rp_lst = rp.split('\n')
    for idx, num in enumerate(P.number):
        picture = picture + num + '  '
        rp_lst[idx] = num + ' ' + rp_lst[idx]
    picture = picture + '\n' + '\n'.join(rp_lst)
    print(picture)


def rg_to_solver_rl(rg):
    solver_rl = []
    for i in range(13):
        for j in range(13):
            n1 = P.number[i]
            n2 = P.number[j]
            hand = n1 + n2

            if i == j:  # 对子
                pass
            elif i > j:  # 杂色
                hand += 'o'
            else:  # 同色
                hand += 's'
            try:
                if 0 < rg[i][j] < 24:
                    point = round(rg[i][j] / 24, 2)
                    hand = hand + ':' + str(point)
            except:
                print('wrong')
                print(i, j)
            if rg[i][j] > 0:
                solver_rl.append(hand)
    rlstr = ','.join(solver_rl)
    return rlstr


def solver_file_to_rg(solver_file):
    with open(solver_file, 'r') as solver_file:
        rl_str = solver_file.readline()
    solver_rl_lst = rl_str.split(',')
    rg = solver_rl_to_rg(solver_rl_lst)
    return rg


def solver_rl_to_rg(solver_rl):
    rg = get_blank_range()
    for s_hand in solver_rl:
        point = 1
        goal = 24
        hand1, hand2 = s_hand[0], s_hand[1]
        if ':' in s_hand:
            point = float(s_hand.split(':')[1])
            goal = int(point * 12) * 2
        # 3种情况: 有花色标志,没花色标志的对子,没花色标志
        i = P.number.index(hand1)
        j = P.number.index(hand2)
        if 'o' in s_hand:
            i, j = j, i
        if 's' in s_hand or 'o' in s_hand or hand1 == hand2:
            rg[i][j] = goal
        else:
            rg[i][j] = goal
            rg[j][i] = goal
    return rg


def save_solver_rl(dirname, rlstr, filename='D:\PioSOLVER\Ranges\生成范围'):
    with open(os.path.join(filename, dirname), 'w') as f:
        f.write(rlstr)


def rg1_sub_rg2(rg1, rg2):
    new_rg = get_blank_range()
    for i in range(13):
        for j in range(13):
            new_rg[i][j] = rg1[i][j] - rg2[i][j]
            if new_rg[i][j] < 0:
                new_rg[i][j] = 0
    return new_rg


def load_range(file_path='E:\扑克研究\自制扑克软件\solver_range', file_name=''):
    def open_range(path=file_path):
        name_list = []
        for name2 in os.listdir(path):
            name = os.path.join(path, name2)
            if os.path.isfile(name) and '.txt' in name:
                name_list.append(name2)
            elif os.path.isdir(name):
                name_list.append(name2)

        print('选择一个打开:')
        for idx, name in enumerate(name_list):
            print(idx + 1, name)
        while 1:
            try:
                idx = int(input('输入序号:'))
                if 0 < idx <= len(name_list):
                    break
                else:
                    print('输入有问题')
            except:
                print('输入有问题')
        choise_name = name_list[idx - 1]
        new_path = os.path.join(path, choise_name)
        if os.path.isdir(new_path):
            rg = open_range(new_path)
            return rg
        else:
            rg = solver_file_to_rg(new_path)
            return rg

    return open_range()
