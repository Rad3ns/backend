
# Variabel global untuk menyimpan data Buku
buku = []

# fungsi untuk menampilkan semua data
def tampilkan_data():
    if len(buku) <= 0:                  
        print("BELUM ADA DATA")
    else:
        for indeks in range(len(buku)):
            print("[%d] %s" % (indeks, buku[indeks]))


# fungsi untuk menambah data
def isi_data():
    buku_baru = input("Judul Buku: ")
    buku.append(buku_baru)

# fungsi untuk edit data
def edit_data():
    tampilkan_data()
    indeks = int(input("Inputkan ID buku: "))
    if(indeks > len(buku)):
        print("ID salah")
    else:
        judul_baru = input("Judul baru: ")
        buku[indeks] = judul_baru

# fungsi untuk menghapus data
def hapus_data():
    tampilkan_data()
    indeks = int(input("Inputkan ID buku: "))
    if(indeks > len(buku)):
        print("ID salah")
    else:
        buku.remove(buku[indeks])

# fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\n")
    print("----------- MENU ----------")
    print("[1] Tampilkan Data")
    print("[2] Isi Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("[5] Exit")

    
    menu = input("PILIH MENU> ")
    print("\n")
    if menu == "1":
        tampilkan_data()
    elif menu == "2":
        isi_data()
    elif menu == "3":
        edit_data()
    elif menu == "4":
        hapus_data()
    elif menu == "5":
        exit()
    else:
        print("Salah pilih!")

if __name__ == "__main__":
    while(True):
            tampilkan_menu()

