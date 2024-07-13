nama_global = "Otong" #variabel global

# akses variabel global dalam fungsi
def fungsi():
    print(f"Fungsi menampilkan {nama_global}")

fungsi()

# akses variabel global dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama_global}")

# percabangan
if True:
    print(f"if menampilkan {nama_global}")


'''Variabel local scope'''

def fungsi2():
    nama_local = "Ucup" # <- variabel local scope

fungsi2()
# print(nama_local) # tidak bisa dilakukan

## Contoh 1: penggunaan akses variable
def say_otong():
    print(f"Hello {nama}")

nama = "Otong"
say_otong()

## Contoh 2: merubah variable global
angka = 0
name = "Ucup"

def ubah(nilai_baru, nama_baru):
    global angka # fungsi ini mendapat akses merubah angka
    global name
    angka=nilai_baru
    name=nama_baru

print(f"Sebelum {angka, name}")
ubah(10, "Otong")
print(f"Sesudah {angka, name}")


# COntoh 3:
angka = 0

for i in range(0,10):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)