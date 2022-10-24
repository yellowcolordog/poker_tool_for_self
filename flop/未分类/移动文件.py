import os
import shutil

for file in os.listdir():
    if os.path.isdir(file):
        if len(file) == 4:
            shutil.move(file,os.path.join('1',file))
        if len(file) == 3:
            shutil.move(file,os.path.join('2',file))