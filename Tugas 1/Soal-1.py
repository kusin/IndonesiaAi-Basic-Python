# PROGRAM Soal-1.py
# Format tranlasi algoritma notasi bahasa alami menjadi kode program mengikuti contoh 
#   "Munir R, Lidya L. 2016. Algoritma & Pemrogram: Dalam Bahasa Pascal, C dan C++. Edisi 6. Bandung(ID): Informatika"
''' proses bisnis
    Program dapat menerima masukan berupa nama, umur, tinggi.
    Kemudian keluaran program adalah menampilkan masukan data dari pengguna.
'''

# DEKLARASI Pustaka
import os # os, pustaka mengenali os yg digunakan
import re # regex, untuk melihat pola masukan

# DEKLARASI Fungsi
# fungsi cek format masukan, jika variabel tsb hanya berisi huruf
# ex. var nama
def only_letter(param):
    # statment only letter

    # return value
    return param

# fungsi cek format masukan, jika variabel tsb hanya berisi angka
# ex. var umur dan tinggi
def only_number(param):
    # statment only number
    
    # return value
    return param

# DEKLARASI Variabel
nama = ""
umur = ""
tinggi = ""
  
# ALGORITMA
if __name__=="__main__":
    # Hapus layar / clear screen
    # Baris pertama dari keluaran program adalah masukan program bukan path directory program. 
    #os.system('cls' if os.name == 'nt' else 'clear')
    
    # Masukan
    print("Masukan program ...")
    
    # validasi. Kika variabel tersebut tidak diisii, Maka program akan meminta masukan kembali
    while nama == "":
        nama = input("Masukan nama  : ")
    
    # validasi. Kika variabel tersebut tidak diisii, Maka program akan meminta masukan kembali
    while umur == "":
        umur = input("Masukan umur  : ")

    # validasi. Kika variabel tersebut tidak diisii, Maka program akan meminta masukan kembali
    while tinggi == "":
        tinggi = input("Masukan tinggi : ")
    
    print("\n")

    # Keluaran
    print("Keluaran program ...")
    print("Nama anda    : "+nama)
    print("Umur anda    : "+umur +"th")
    print("Tinggi anda  : "+tinggi+ "cm")

    print("\n")