# PROGRAM Soal-3.py
# Format tranlasi algoritma notasi bahasa alami menjadi kode program mengikuti contoh 
#   "Munir R, Lidya L. 2016. Algoritma & Pemrogram: Dalam Bahasa Pascal, C dan C++. Edisi 6. Bandung(ID): Informatika"
''' proses bisnis
    program ini untuk menentukan kelulusan siswa.
    Dimana program akan menerima masukan berupa nama, nilai teori, nilai praktikum
    Suatu siswa dinyatakan lulus apabila nilainya lebih dari 70.
    Keluaran program berupa keterangan lulus atau tidak lulus 
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
# ex. var nilai teori dan nilai praktikum
def only_number(param):
    # statment only number
    
    # return value
    return param

# fungsi untuk memeriksa kelulusan siswa
def cek_lulus(var_teori, var_praktikum):
    # deklarasi variabel local
    var_hasil = []

    # cek kelulusan teori
    if var_teori >= 70:
        var_hasil.append("Lulus teori")
    else:
        var_hasil.append("Gagal teori")
    
    # cek kelulusan praktikum
    if var_praktikum >= 70:
        var_hasil.append("Lulus praktikum")
    else:
        var_hasil.append("Gagal praktikum")
    
    # return value kelulusan siswa
    return var_hasil

# DEKLARASI Variabel
nama = ""
teori = ""
praktikum = ""
hasil = []

# ALGORITMA
if __name__=="__main__":
    # Hapus layar / clear screen
    # Baris pertama dari keluaran program adalah masukan program bukan path directory program. 
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Masukan
    print("Masukan program ...")

    # validasi. Kika variabel tersebut tidak diisii, Maka program akan meminta masukan kembali
    while nama == "":
        nama = input("Masukan nama  : ")

    # validasi. Kika variabel tersebut tidak diisii, Maka program akan meminta masukan kembali
    while teori == "":
        teori = input("Nilai teori  : ")
    
    # validasi. Kika variabel tersebut tidak diisii, Maka program akan meminta masukan kembali
    while praktikum == "":
        praktikum = input("Nilai praktikum : ")
    
    print("\n")

    # Proses
    hasil = cek_lulus(int(teori), int(praktikum))

    # Keluaran
    print("Keluaran program ...")
    print("Nama anda : "+nama)
    [print(x) for x in hasil]

    print("\n")

