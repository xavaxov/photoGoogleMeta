from datetime import datetime
import os
import csv
from win32_setctime import setctime

data = []

with open('data.csv', 'r') as file:
    reader = csv.reader(file, delimiter = ';')
    for row in reader:
        data.append(row)

print(data)    

# Указываем путь к директории
directory = "/Users/aleksei/Downloads/!Разобрать"
 
try:
    os.remove(os.path.join(directory,'.DS_Store'))
except:
    pass

# Получаем список файлов
subdirectorys = os.listdir(directory)

# Выводим список файлов
print(subdirectorys)

for subdirectory in subdirectorys:
    files = os.listdir(os.path.join(directory,subdirectory))

    for file in files:

        for name,time in data:
            if name == file:
                os.rename(os.path.join(directory,subdirectory,name), os.path.join(directory,subdirectory,time +'_'+ name[len(name)-5:]))

