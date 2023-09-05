from exif import Image
import json
from datetime import datetime
import os

# Указываем путь к директории
directory = "/Загрузки/Takeout/Google Фото"
 
# Получаем список файлов
files = os.listdir(directory)
 
# Выводим список файлов
print(files)

for name in files:
    subfiles = os.listdir(directory + name)

    for i in range(len(subfiles)-1):
        file_img = subfiles[i]
        if file_img[len(file_img)-3:] == 'jpg':
            if subfiles[i+1] == file_img + '.json':
                file_json = subfiles[i+1]
                print(subfiles[i], end = ' ')

                with open(os.path.join(directory,name,file_img), 'rb') as img:
                    img = Image(img)

                with open(os.path.join(directory,name,file_img), 'r') as file_json:
                    templates = json.load(file_json)

                timestamp_file = int(templates['photoTakenTime']['timestamp']) - 3*60*60
               
                time_file_str = datetime.fromtimestamp(timestamp_file).strftime('%Y:%m:%d %H:%M:%S')
                print(time_file_str)

                try:
                    img.delete_all()
                    img.datetime_original = time_file_str
                    with open(directory + name + '/'  + file_img, 'wb') as updated_img:
                        updated_img.write(img.get_file())

                except:
                    print('\n\n--- bug --- \n' + file_img, end = '\n\n')

                