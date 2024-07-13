# 1. mode write

# akan membuat file baru jika tidak ada, 
# lalu akan menimpa atau overwrite isinya

with open("data_1.txt", 'w', encoding="utf-8") as file:
    file.write("Miku")

with open("data_1.txt", 'w', encoding="utf-8") as file:
    file.write("Itsuki")

with open("data_1.txt", 'w', encoding="utf-8") as file:
    file.write("overwrite")

# 2. mode append

with open("data_2.txt", 'w', encoding="utf-8") as file:
    file.write("Miku\n")

with open("data_2.txt", 'a', encoding="utf-8") as file:
    file.write("Itsuki\n")

with open("data_2.txt", 'a', encoding="utf-8") as file:
    file.write("tambah lagi dengan append\n")  

# 3. mode r+

with open("data_3.txt", 'w', encoding="utf-8") as file:
    file.write("data ke 3\n")

with open("data_3.txt", 'r+', encoding="utf-8") as file:
    file.write("baris-1 \n")
    file.write("baris-2 \n")
    file.write("baris-3 \n")

with open("data_3.txt", 'w', encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("data_3.txt", 'r+', encoding="utf-8") as file:
    file.write("Yotsu") # menimpa isi teks sesuai dengan panjang data