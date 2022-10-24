import os

def change_name(name):
    s_l = list(name[1::2])
    n_l = list(name[::2])
    if len(set(s_l)) == 3:
        pass
    elif len(set(s_l)) == 2:
        for idx,s in enumerate(s_l):
            if s_l.count(s) == 1:
                n_l.insert(idx+1,'o')
    else:
        n_l.insert(0,'s')
    new_name = ''.join(n_l)
    return new_name

# os.rename()
for file in os.listdir():
    if os.path.isdir(file):
        new_name= change_name(file)
        os.rename(file,new_name)


