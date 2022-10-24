import os

for file in os.listdir():
    if os.path.isdir(file):
        name = file.replace('o','')
        if name[0] == name[1]:
            os.removedirs(file)