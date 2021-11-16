print("===================================")
print("========= Toko Bangunan ===========")
print("===================================")
Menudibeli = []
while True:
    menu_pilihan = input(' 1.Alat Bangunan\n 2.Barang Interior\n 3.Barang Eksterior\n Masukkan menu utama 1-3: \n')
    if menu_pilihan == "1":
        print("=====================")
        print("Anda memilih nomor 1 : Alat Bangunan")
        print("Pilih Alat Bangunan anda :")
        alat_bangunan = ["Kuas cat", "Meteran", "Palu"]
        for a in range(0, len(alat_bangunan)):
            print(f'{a + 1}.{alat_bangunan[a]}')
        list_alat_bangunan = int(input('Pilih Menu 1-3:\n'))
        if list_alat_bangunan == 1:
            Menudibeli.append(alat_bangunan[0])
            print('==== Menu yang dibeli ====')
            for b in range(0,len(Menudibeli)):
                print(f'{b+1}.{Menudibeli[b]}  1x')
                continue
        elif list_alat_bangunan == 2:
            Menudibeli.append(alat_bangunan[1])
            print('==== Menu yang dibeli ====')
            for b in range(0,len(Menudibeli)):
                print(f'{b+1}.{Menudibeli[b]}  1x')
                continue
        elif list_alat_bangunan == 3:
            Menudibeli.append(alat_bangunan[2])
            print('==== Menu yang dibeli ====')
            for b in range(0,len(Menudibeli)):
                print(f'{b+1}.{Menudibeli[b]}  1x')
                continue
        else:
            print("=====================")
            print("Menu tidak tersedia\n")
            continue
    elif menu_pilihan == "2":
        print("=====================")
        print("Anda memilih nomor 2 : Barang Interior")
        print("Pilih Barang Interior anda :")
        barang_interior = ["Kursi","Meja","TV"]
        for a in range(0, len(barang_interior)):
            print(f'{a + 1}.{barang_interior[a]}')
        list_barang_interior = int(input('Pilih Menu 1-3:\n'))
        if list_barang_interior == 1:
            Menudibeli.append(barang_interior[0])
            print('==== Menu yang dibeli ====')
            for b in range(0,len(Menudibeli)):
                print(f'{b+1}.{Menudibeli[b]}  1x')
                continue
        elif list_barang_interior == 2:
            Menudibeli.append(barang_interior[1])
            print('==== Menu yang dibeli ====')
            for b in range(0,len(Menudibeli)):
                print(f'{b+1}.{Menudibeli[b]}  1x')
                continue
        elif list_barang_interior == 3:
            Menudibeli.append(barang_interior[2])
            print('==== Menu yang dibeli ====')
            for b in range(0,len(Menudibeli)):
                print(f'{b+1}.{Menudibeli[b]}  1x')
                continue
        else:
            print("=====================")
            print("Menu tidak tersedia\n")
            continue
    elif menu_pilihan == "3":
        print("=====================")
        print("Anda memilih nomor 3 : Barang Eksterior")
        print("Pilih Barang Eksterior anda :")
        barang_eksterior = ["Lampu Taman","Kayu","Batu"]
        for a in range(0, len(barang_eksterior)):
            print(f'{a + 1}.{barang_eksterior[a]}')
        list_barang_eksterior = int(input('Pilih Menu 1-3:\n'))
        if list_barang_eksterior == 1:
            Menudibeli.append(barang_eksterior[0])
            print('==== Menu yang dibeli ====')
            for b in range(0,len(Menudibeli)):
                print(f'{b+1}.{Menudibeli[b]}    1x')
                continue
        elif list_barang_eksterior == 2:
            Menudibeli.append(barang_eksterior[1])
            print('==== Menu yang dibeli ====')
            for b in range(0,len(Menudibeli)):
                print(f'{b+1}.{Menudibeli[b]}    1x')
                continue
        elif list_barang_eksterior == 3:
            Menudibeli.append(barang_eksterior[2])
            print('==== Menu yang dibeli ====')
            for b in range(0,len(Menudibeli)):
                print(f'{b+1}.{Menudibeli[b]}    1x')
                continue
        else:
            print("=====================")
            print("Menu tidak tersedia\n")
            continue
    else:
        print("Menu tidak tersedia")
        continue
    validasi_menu = input('Ada yang ingin ditambahkan ? Y/n\n')
    if validasi_menu == "Y" or validasi_menu == "y":
        print("=====================")
        continue
    else:
        print("Pesanan anda Segera di antar")
        break