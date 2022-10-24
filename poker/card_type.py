from poker import *
straight_list = [
    {'Q', 'T', 'K', 'A', 'J'},
    {'Q', '9', 'T', 'K', 'J'},
    {'Q', '9', 'T', '8', 'J'},
    {'9', 'T', '8', '7', 'J'},
    {'9', 'T', '8', '6', '7'},
    {'9', '8', '7', '6', '5'},
    {'4', '8', '7', '6', '5'},
    {'4', '3', '6', '7', '5'},
    {'4', '3', '6', '5', '2'},
    {'4', 'A', '3', '5', '2'}
]
# new_p = P.number[:]
# new_p.append('A')
# for i in range(10):
#     s = set()
#     for j in new_p[i:i+5]:
#         s.add(j)
#     straight_list.append(s)
#
# print(straight_list)

def CardType(cl):
    card_sorted(cl)


def get_suit(cl):
    suit_list = []
    for c in cl:
        s,n = c[0],c[1]
        suit_list.append(s)
    return suit_list


def S_flush(cl):
    res_cl = []
    # 1 同花色需要超过5张 2. 这些同花色的牌能组成顺子
    suit_cl = Suit(cl,flush_flag=True)
    res_cl = Straight(suit_cl)
    return res_cl



def Suit(cl,flush_flag=False):
    res_cl = []
    # 同花色需要超过5张
    suit_list = get_suit(cl)
    suit_set = set(suit_list)
    for s in suit_set:
        if suit_list.count(s) >= 5:
            for c in cl:
                if c[0] == s:
                    res_cl.append(c)
    card_sorted(res_cl)
    if not flush_flag:res_cl=res_cl[:5]
    return res_cl


def Straight(cl):
    res_cl = []

    num_set = set()
    str_set = set()
    cl2 = []
    for c in cl:
        str_set.add(c[1])
        if c[1] not in num_set:
            cl2.append(c)
        num_set.add(c[1])
    cl = cl2 # 去重

    stra_mode = set()
    for s_model in straight_list:
        if len(str_set & s_model) == 5:
            stra_mode = s_model

    for c in cl2:
        if c[1] in stra_mode:
            res_cl.append(c)

    return res_cl


def get_num(cl):
    num_list = []
    for c in cl:
        num_list.append(c[1])
    num_set = set(num_list)

    num_dic = {}
    for n in num_set:
        num_dic[n] = num_list.count(n)
    return num_dic


def Kings(cl):
    res_cl = []
    num_count_dic = get_num(cl)

    param = ''
    for n,count in num_count_dic.items():
        if count == 4:
            param = n
    if param:
        kickflag = 1
        for c in cl:
            if c[1] == param:
                res_cl.append(c)
            elif kickflag:
                res_cl.append(c)
                kickflag = 0

    return res_cl


def Fullhouse(cl):
    res_cl = []
    num_count_dic = get_num(cl)
    param1_list = []
    param2_list = []
    for n,count in num_count_dic.items():
        if count == 3:
            param1_list.append(n)
        if count>=2:
            param2_list.append(n)

    # 判断存在葫芦
    if len(param1_list)>=1 and len(param2_list)>=2:
        num_sorted(param1_list)
        num_sorted(param2_list)
        param1 = param1_list[0]
        param2 = ''
        for p in param2_list:
            if p != param1:
                param2 = p
                break
        for c in cl:
            if c[1] == param1:
                res_cl.append(c)
            if c[1] == param2:
                res_cl.append(c)
    return res_cl[:5]

def Trips()

def Pair(cl):
    pass
