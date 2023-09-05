from datetime import datetime

time_file = datetime.fromtimestamp(1693612201)

m = '0' + str(time_file.month) if time_file.month<10 else str(time_file.month)
d = '0' + str(time_file.day) if time_file.day<10 else str(time_file.day)
h = '0' + str(time_file.hour) if time_file.hour<10 else str(time_file.hour)
min = '0' + str(time_file.minute) if time_file.minute<10 else str(time_file.minute)
s = '0' + str(time_file.second) if time_file.second<10 else str(time_file.second)

time_file_str = str(time_file.year) + ':' + m + ':' + d + ' ' + h + ':' + min + ':' + s
print(time_file_str)

