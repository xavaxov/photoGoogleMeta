from exif import Image
import json
from datetime import datetime
import os
 
# Указываем путь к директории
directory = "/Загрузки/Takeout/Google Фото/ремонт/"
 
# Получаем список файлов
files = os.listdir(directory)
 
# Выводим список файлов
print(files)

for i in range(len(files)-1):
    file_img = files[i]

    if file_img[len(file_img)-3:] == 'jpg':
        if files[i+1] == file_img + '.json':
            file_json = files[i+1]
            print(files[i], end = '')

            with open(directory + file_img, 'rb') as img:
                img = Image(img)

            with open(directory + file_json, 'r') as file_json:
                templates = json.load(file_json)

            timestamp_file = int(templates['photoTakenTime']['timestamp']) - 3*60*60
            time_file = datetime.fromtimestamp(timestamp_file)
            
            m = '0' + str(time_file.month) if time_file.month<10 else str(time_file.month)
            d = '0' + str(time_file.day) if time_file.day<10 else str(time_file.day)
            h = '0' + str(time_file.hour) if time_file.hour<10 else str(time_file.hour)
            min = '0' + str(time_file.minute) if time_file.minute<10 else str(time_file.minute)
            s = '0' + str(time_file.second) if time_file.second<10 else str(time_file.second)

            time_file_str = str(time_file.year) + ':' + m + ':' + d + ' ' + h + ':' + min + ':' + s
            print(time_file_str)

            try:
                img.delete_all()
                img.datetime_original = time_file_str
                with open(directory + file_img, 'wb') as updated_img:
                    updated_img.write(img.get_file())

            except:
                print('\n\n--- bug --- \n' + file_img, end = '\n\n')

            