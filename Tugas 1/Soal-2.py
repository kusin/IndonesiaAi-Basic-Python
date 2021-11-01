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
# fungsi cek format masukan, jika variabel tsb hanya berisi angka
# ex. var jari-jari
def only_number(param):
    # statment only number
    
    # return value
    return param

# fungsi hitung luas lingkaran
def hitung_luas(var_jari_jari):
    # Deklarasi local fungsi
    var_hasil = ""

    # cek jari-jari
    if float(var_jari_jari) % 7 == 0:
        # jika kelipatan == 7 maka menggunakan phi = 22/7
        phi = 22/7
    else:
        # jika kelipatan != 7 maka menggunakan phi = 3.14
        phi = 3.14
    
    # hitung luas lingkaran
    var_hasil = phi * float(var_jari_jari) * float(var_jari_jari)

    # return value fungsi
    return var_hasil


# DEKLARASI Variabel
jari_jari = ""
luas = ""
phi = 0.0

# ALGORITMA
if __name__=="__main__":
    # Hapus layar / clear screen
    # Baris pertama dari keluaran program adalah masukan program bukan path directory program. 
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Masukan
    print("Masukan program ...")
    
    # validasi. Kika variabel tersebut tidak diisii, Maka program akan meminta masukan kembali
    while jari_jari == "":
        jari_jari = input("Masukan jari-jari  : ")

    print("\n")

    # Proses
    luas = hitung_luas(jari_jari)

    # Keluaran
    print("Keluaran program ...")
    print("Jari-Jari        : "+jari_jari)
    print("Luas Lingkaran   : "+"{:.2f}".format(luas))

    print("\n")