'''
`**kwargs` (Keyword Arguments)
'''

def contoh_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

contoh_kwargs(nama="Budi", umur=25)
print("\n")

'''
**kwargs mengumpulkan semua argumen kata kunci yang dilewatkan ke fungsi dan mengemasnya 
dalam bentuk dictionary. Dalam contoh ini, contoh_kwargs dapat menerima sejumlah argumen 
kata kunci dan mencetak masing-masing pasangan kunci-nilai.
'''

# Kombinasi `*args` dan `**kwargs`
print("-"*30)
print("Kombinasi `*args` dan `**kwargs` ")
def contoh_kombinasi(arg1, *args, **kwargs):
    # argumen posisional pertama
    print("args1:", arg1)

    # mengumpulkan argumen posisional tambahan dalam bentuk tuple
    print("\nargs:")
    for arg in args:
        print(arg)

    # mengumpulkan argumen kata kunci dalam bentuk dictionary
    print("\nkwargs")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

contoh_kombinasi(10,20,30, nama="Budi", umur=25)