from modulemtk import tambah as add
from modulemtk import kali as tm
from modulemtk import pangkat as exp
# from modulemtk import * = # mengimport semua fungsi

hasil_add = add(1,2,3,4,5)
print(f"hasil tambah = {hasil_add}")

hasil_times = tm(1,2,3,4,5)
print(f"hasil kali = {hasil_times}")

hasil_exp = exp(3)
print(f"hasil pangkat = {hasil_exp(4)}")