# PROGRAM Informasi Kontak
''' proses bisnis
    .................................
    .................................
    .................................
    https://docs.google.com/document/d/1PTGJrG-eE-M4ETtqQbNfmLJHRFZHL1zk/edit
'''

# DEKLARASI Pustaka
import os # os, pustaka mengenali os yg digunakan

# DEKLARASI Fungsi
def menu1():
    print("Nama", "\t\t", "Telp")
    print("--------------------------------------")
    # menampilkan dataset
    for i in range(len(nama)):    
        print(str(nama[i]), "\t" ,str(telp[i]))

def menu2():
    nama.append(input('Masukan nama : '))
    telp.append(input('Masukan telp : '))
    print('Kontak berhasil ditambahkan')
    
# DEKLARASI Variabel
# variabel global
ulangi = "Ya"

# jika menggunakan format DataFrame sebagai media penyimpanan data
nama = ['Kagome Chan', 'Kikyo Sama']
telp = ['0818-xxx', '0819-xxx']

# ALGORITMA
if __name__=="__main__":
    
    # Program akan terus berulang sampai pengguna tidak lagi ingin menjalankan program ini
    while ulangi == "Ya":
        
        # Hapus layar / clear screen
        # Baris pertama dari keluaran program adalah masukan program bukan path directory program. 
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # tampilan awal program
        print("Selamat Datang \n")
        
        print("-- Menu --")
        print("1. Daftar Kontak")
        print("2. Tambah Kontak")
        print("3. Keluar")
        
        # meminta masukan pilihan menu dari pengguna
        menu = input("Masukan pilihan menu : ")
        print(" ")
        
        # cek pilihan menu
        if(menu == "1"):
            menu1() # memanggil menu 1 untuk menampilkan data kontak
            
        elif(menu == "2"):
            menu2() # menampilkan mmenu 2 untuk menambah data kontak
            
        elif(menu == "3"):
            # menampilkan pesan terima kasih
            print("Terima Kasih")
            
            # keluar dari program
            exit()
        
        else:
            # menampilkan pesan menu salah
            print("Pilihan menu salah")
        
        # Jika pengguna memasukan "Ya", maka program akan mengulang kembali program
        print(" ")
        ulangi = input("Ulangi proses : ")