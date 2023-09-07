from exif import Image
import json
from datetime import datetime
import os
import traceback


# Указываем путь к директории
directory = "/Users/aleksei/Desktop/Takeout/Google Фото"

try:
    os.remove(os.path.join(directory,'.DS_Store'))
except:
    pass  

# Получаем список файлов
subdirectory = os.listdir(directory)
 
# Выводим список файлов
print(subdirectory)

for name in subdirectory:
    files = os.listdir(os.path.join(directory,name))
    files.sort()
    print(files)

    for i in range(len(files)-1):
        file_img = files[i]

        if not(file_img[len(file_img)-3:] == 'jpg' and files[i+1] == file_img + '.json'):
            continue

        file_json = files[i+1]
        print(files[i], end = ' ')

        with open(os.path.join(directory,name,file_img), 'rb') as img:
            img = Image(img)

        with open(os.path.join(directory,name,file_json), 'r') as fjson:
            templates = json.load(fjson)

        timestamp_file = int(templates['photoTakenTime']['timestamp']) - 3*60*60
        
        time_file_str = datetime.fromtimestamp(timestamp_file).strftime('%Y:%m:%d %H:%M:%S')
        time_file_year = datetime.fromtimestamp(timestamp_file).strftime('%Y')
        time_file_month = datetime.fromtimestamp(timestamp_file).strftime('%m')

        print(time_file_str, end = ' ')

        try:
            img.delete_all()
            img.datetime_original = time_file_str

            try:
                os.mkdir(time_file_year)
            except:
                pass    

            try:
                os.mkdir(os.path.join(time_file_year,time_file_month))
            except:
                pass     

            with open(os.path.join(time_file_year,time_file_month,time_file_str + '.jpg'), 'wb') as updated_img:
                updated_img.write(img.get_file())


            os.remove(os.path.join(directory,name,file_img))
            os.remove(os.path.join(directory,name,file_json))
                
        except:
            print('\n\n--- bug --- \n' + file_img, end = '\n\n')