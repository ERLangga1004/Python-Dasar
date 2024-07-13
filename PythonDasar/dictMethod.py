'''
items(): Mengembalikan pasangan kunci-nilai.
keys(): Mengembalikan semua kunci.
values(): Mengembalikan semua nilai.
get(): Mengakses nilai dengan aman.
update(): Memperbarui dictionary dengan pasangan kunci-nilai dari dictionary lain.
'''

# Membuat dictionary
nilai_siswa = {
    'Andi': 80,
    'Budi': 95,
    'Cici': 85
}

# mengakses nilai berdasarkan kunci
print(nilai_siswa['Andi']) # Output: 80

# Menambahkan item baru
nilai_siswa['Dewi'] = 90
print(nilai_siswa) # Output: {'Andi': 80, 'Budi': 95, 'Cici': 85, 'Dewi': 90}

# Mengubah nilai
nilai_siswa['Andi'] = 85
print(nilai_siswa) # Output: {'Andi': 85, 'Budi': 95, 'Cici': 85, 'Dewi': 90}

# Menghapus item
del nilai_siswa['Cici']
print(nilai_siswa) # Output: {'Andi': 85, 'Budi': 95, 'Dewi': 90}

# Mengiterasi dictionary
for nama, nilai in nilai_siswa.items():
    print(f"{nama} mendapatkan nilaidd {nilai}")

'''Metode-Metode Penting `dict`'''
# `dict.items()`
items = nilai_siswa.items()
print(items) # Output: dict_items([('Andi', 85), ('Budi', 95), ('Dewi', 90)])

# `dict.keys()`
keys = nilai_siswa.keys()
print(keys)  # Output: dict_keys(['Andi', 'Budi', 'Dewi'])

# `dict.values()`
values = nilai_siswa.values()
print(values) # Output: dict_values([85, 95, 90])

# `dict.get(key[, default])`
nilai_andi = nilai_siswa.get('Andi')
print(nilai_andi) # Output: 85

nilai_eko = nilai_siswa.get('Eko', 'Tidak ada nilai')
print(nilai_eko)  # Output: Tidak ada nilai