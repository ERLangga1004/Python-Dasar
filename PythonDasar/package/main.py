import sains
from sains.mtk import scientific

hasil_add = sains.mtk.add(1,2,3,4,5)
print(f"Hasil add dari package adalah = {hasil_add}")

gaya = sains.fisika.gaya(90,10)
print(f"Gaya adalah = {gaya}")

hasil_kali = sains.mtk.times(1,3,4,5,6)
print(f"Hasil kali = {hasil_kali}")

pangkat3 = scientific.power(3)
print(f"Hasil pangkat = {pangkat3(5)}")