import numpy as np

list_a = [1,2,3,4] # list biasa
vektor_a = np.array([1,2,3,4])

print(f"list a = {list_a}") #  hasil list biasa
# print(list_a**2) -> Tidak bisa dikuadratkan langsung
print(f"vektor a = {vektor_a}")
print(f"a pangkat 2 = {vektor_a**2}") # Bisa
print(f"a kali 5 = {vektor_a*5}") # Bisa

matrix_b = np.array([(1,3),(4,1)])
print(f"matrix b = \n{matrix_b}")
print(f"matrix b^2 = \n{matrix_b**2}")

zeros_c = np.zeros((2,2))
print(f"zeros c = \n{zeros_c}")

ones_d = np.ones((2,2))
print(f"zeros c = \n{ones_d}")

jumlah = matrix_b + matrix_b**2 + ones_d
print(f"jumlah = \n{jumlah}")