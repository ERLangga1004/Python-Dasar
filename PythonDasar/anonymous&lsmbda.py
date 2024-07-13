'''Lambda function'''

def f_kuadrat(angka):
    return angka**2

print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")

# Menggunakan lambda
# Output = lambda argument: expression
kuadrat = lambda angka:angka**2
print(f"Hasil lambda kuadrat = {kuadrat(5)}")

pangkat = lambda num,pow:num**pow
print(f"Hasil lambda pamgkat = {pangkat(4,2)}")

# sorting biasa
data_list = ["Otong", "Ucup", "Dudung"]
data_list.sort()
print(f"Sorted list = {data_list}")

# sorting dengan pangjang(len)
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print(f"Sorted list by len = {data_list}")

# sort pakai lambda
data_list = ["otong", "Ucup", "Dudung"]
data_list.sort(key=lambda nama:len(nama))
print(f"Sorted list by lambda = {data_list}")

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
data_angka_baru = list(filter(lambda x:x<6, data_angka))
print(data_angka_baru)

# genap
data_genap = list(filter(lambda x:x%2==0, data_angka))
print(data_genap)

# gamjil
data_ganjil = list(filter(lambda x:x%2!=0, data_angka))
print(data_genap)

'''Anonymous function'''
# currying <- Haskell Curry

def pangkat(angka,n):
    hasil = angka**n
    return hasil
data_hasil = pangkat(5,2)
print(f"Fungsi biasa = {data_hasil}")

# dengan currying 
def pangkat(n):
    return lambda angka:angka**n
pangkat2 = pangkat(2)
print(f"5*2 = {pangkat2(5)}")

# akhir
print(f"pangkat bebas = {pangkat(4)(5)}") # 5 pangkat 4
