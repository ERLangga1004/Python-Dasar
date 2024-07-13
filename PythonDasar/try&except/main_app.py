# Exception akan terjadi saat program mengalami error saat runtime

# contoh
from math import nan

# input_user =int(input("Masukan angka: "))
# hasil = nan

# try:
#     hasil = 10/input_user
# except:
#     print("input tidak boleh 0")

# print(f"hasil = {hasil}")

## Contoh di aplikasi
while(True):
    angka = int(input("Masukan angka pembagi: "))
    try:
        hasil = 10/angka
        print(f"hasil = {hasil}")
        is_done = input("lanjutkan (y/n)? ")
        if is_done == "n":
            break
    
    except:
        print("Pembagi nol, silahkan inputkan angka lain!")

print("Akhir dari Program 1")

# contoh 2
try:
    with open("/Python/PythonDasar/try&except/data.txt", "r") as file:
        print(file.read())

except:
    print("file data.txt tidak ditemukan, membuat file baru")
    with open("/Python/PythonDasar/try&except/data.txt", "w", encoding='utf-8') as file:
        file.write("file baru")

print("Akhir dari program 2")
