import datetime as dt

data_waktu = dt.datetime.now()
print(f"datetime now : {data_waktu}")
print(f"hari = {data_waktu.strftime('%A')}")
print(f"tahun : {data_waktu.year}")

from collections import Counter

data = ["a","b","c","a","f","d","c","a"]

# count = 0 
# for i in data:
#     if i == "a":
#         count += 1

# print(count)

data_count = Counter(data)
print(f"data count = {data_count}")
print(f"jumlah a = {data_count['a']}")

import io
import os

print(f"directory: {os.getcwd()}")
file = io.open("/Python/PythonDasar/library/file_text.txt", "r") 
print(file.read())