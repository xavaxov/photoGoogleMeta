from exif import Image
import json
from datetime import datetime
import os

# Указываем путь к директории
directory = "/Загрузки/Takeout/Google Фото"
 
# Получаем список файлов
subdirectory = os.listdir(directory)
 
# Выводим список файлов
print(subdirectory)

data_file = open('data.csv', 'w')

for name in subdirectory:
    files = os.listdir(os.path.join(directory,name))

    for file in files:

        if not(file[len(file)-4:] == 'json'):
            continue

        try:
            with open(os.path.join(directory,name,file), 'r') as file_json:
                templates = json.load(file_json)
        except:
            pass
        
        timestamp_file = int(templates['photoTakenTime']['timestamp']) - 3*60*60
        time_file_str = datetime.fromtimestamp(timestamp_file).strftime('%Y:%m:%d %H:%M:%S')
        print(time_file_str + ', ' + file[:len(file)-5] + '\n')
        data_file.write(time_file_str + ', ' + file[:len(file)-5] + '\n')

data_file.close()