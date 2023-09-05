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

for name in subdirectory:
    files = os.listdir(os.path.join(directory,name))

    for i in range(len(files)-1):
        file_img = files[i]

        if not(file_img[len(file_img)-3:] == 'jpg' and files[i+1] == file_img + '.json'):
            continue

        file_json = files[i+1]
        print(files[i], end = ' ')

        with open(os.path.join(directory,name,file_img), 'rb') as img:
            img = Image(img)

        with open(os.path.join(directory,name,file_json), 'r') as file_json:
            templates = json.load(file_json)

        timestamp_file = int(templates['photoTakenTime']['timestamp']) - 3*60*60
        
        time_file_str = datetime.fromtimestamp(timestamp_file).strftime('%Y:%m:%d %H:%M:%S')
        time_file_year = datetime.fromtimestamp(timestamp_file).strftime('%Y')
        time_file_month = datetime.fromtimestamp(timestamp_file).strftime('%m')

        print(time_file_str)

        try:
            #img.delete_all()
            img.datetime_original = time_file_str

            try:
                os.mkdir(time_file_year)
            except:
                pass    

            try:
                os.mkdir(os.path.join(time_file_year,time_file_month))
            except:
                pass     

            with open(os.path.join(time_file_year,time_file_month,file_img), 'wb') as updated_img:
                updated_img.write(img.get_file())


            os.remove(os.path.join(directory,name,file_img))
                
        except:
            print('\n\n--- bug --- \n' + file_img, end = '\n\n')