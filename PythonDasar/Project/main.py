import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
    
    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("="*25)

    # Chek database ada atau tidak
    CRUD.init_console()

    while(True):

        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("="*25)

        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")

        user_option = input("Masukan Opsi: ") 

        print("="*25)    

        match user_option:
            case "1": print("Read Data")
            case "2": print("Create Data")
            case "3": print("Update Data")
            case "4": print("Delete Data")

        print("="*25)  

        is_done = input("Apakah Selesai (y/n)? ")
        if is_done == "y" or is_done == "Y":
            break
    
    print("Program Berakhir, Terima Kasih!")



