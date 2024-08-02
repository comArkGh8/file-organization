
import os

files = os.listdir()
for _ ,file in enumerate(files):
    split_title = file.split('master-')
    if len(split_title) > 1:
        os.remove(file)
    if file.startswith('dno'):
        if not file.endswith('.tex'):
            os.remove(file)
