# PROGRAM Hitung Nilai
''' proses bisnis
    Sebuah program sederhana untuk menentukan nilai akhir
    Dimana program akan meminta masukan berupa nim, nama, formatif, uts, uas
    Kemudian untuk menghitung nilai akhir, memiliki rumus
        nilai akhir = 40% formatif + 30% UTS + 30% UAS
    Program tersebut memiliki keluaran berupa nim, nama, nilai akhir.
'''

# DEKLARASI Pustaka
import os # os, pustaka mengenali os yg digunakan
import math # math, pustaka untuk melakukan proses aritmatika

# DEKLARASI Variabel
nim = ""
nama = ""
formatif = ""
uts = ""
uas = ""
nilai_akhir = ""

# ALGORITMA
if __name__=="__main__":
    # Hapus layar / clear screen
    # Baris pertama dari keluaran program adalah masukan program bukan path directory program. 
    os.system('cls' if os.name == 'nt' else 'clear')

    # Masukan Program
    print("Masukan program ...")
    
    nim = input("Masukan nim        : ")
    nama = input("Masukan nama       : ")
    formatif = input("Nilai Formatif     : ")
    uts = input("Nilai UTS          : ")
    uas = input("Nilai UAS          : ")
    
    # membuat baris baru 
    print("\n")

    # PROSES Nilai Akhir
    nilai_akhir = float(formatif)*0.4 + float(uts)*0.3 + float(uas)*0.3
    
    # Keluaran
    print("Keluaran program ...")
    print("NIM anda     : "+str(nim))
    print("Nama anda    : "+str(nama))
    print("Nilai Akhir  : "+str(nilai_akhir))

    print("\n")