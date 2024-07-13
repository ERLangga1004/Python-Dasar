'''Membaca File Eksternal'''

print(3*'=', " Membaca file txt ", 3*'=')
file = open("/Python/PythonDasar/readexternalfile/data.txt", mode='r')

print(f"Status read: {file.readable()}")
print(f"Status write: {file.writable()}")

# baca seluruh file
print(file.read())

'''baca per baris'''
# print(file.readline(), end="") # baca baris pertama
# print(file.readline(), end="") # baca baris kedua

'''baca semua baris sebagai list'''
# print(file.readlines())

print(f"Apakah file sudah diclose: {file.closed}")
file.close()
print(f"Apakah file sudah diclose: {file.closed}")

'''Salah satu teknik membuka file di python'''
print("\n", 3*"=", " Membaca file txt dengan with", 3*"=")

with open("/Python/PythonDasar/readexternalfile/data.txt", mode="r") as file:
    content = file.readline()
    print(content, end="")
    print(f"Apakah file sudah diclose: {file.closed}")

print(f"Apakah file sudah diclose: {file.closed}")