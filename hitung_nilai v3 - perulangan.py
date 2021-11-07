# PROGRAM Hitung Nilai
''' proses bisnis
    Sebuah program sederhana untuk menentukan nilai akhir dan huruf mutu.
    Dimana program akan meminta masukan berupa nim, nama, formatif, uts, uas
    Kemudian untuk menghitung nilai akhir, memiliki rumus
        nilai akhir = 40% formatif + 30% UTS + 30% UAS
    Kemudian untuk menenntukan huruf mutu
        jika nilai lebih besar dari 80 maka mendapat nilai A
        jika nilai lebih besar dari 70 maka mendapat nilai B
        jika nilai lebih besar dari 60 maka mendapat nilai C
        jika nilai lebih besar dari 50 maka mendapat nilai D
        jika nilai kurang dari 50 maka mendapat nilai E
    Program tersebut memiliki keluaran berupa nim, nama, nilai akhir dan huruf mutu
'''

# DEKLARASI Pustaka
import os # os, pustaka mengenali os yg digunakan
import math # math, pustaka untuk melakukan proses aritmatika

# DEKLARASI Variabel Global
ulangi = "Ya"

# ALGORITMA
if __name__=="__main__":
    
    # Program akan terus berulang sampai pengguna tidak lagi ingin menjalankan program ini
    while ulangi == "Ya":
        
        # DEKLARASI Variabel lokal
        # untuk mereset masukan, ketika program mengulangi proses
        nim = ""
        nama = ""
        formatif = ""
        uts = ""
        uas = ""
        nilai_akhir = ""
        huruf_mutu = ""
                
        # Hapus layar / clear screen
        # Baris pertama dari keluaran program adalah masukan program bukan path directory program. 
        os.system('cls' if os.name == 'nt' else 'clear')

        # Masukan Program
        print("Masukan program ...")

        # validasi. Kika variabel tersebut tidak diisii, Maka program akan meminta masukan kembali
        while nim == "":
            nim = input("Masukan nim        : ")
        
        # validasi. Kika variabel tersebut tidak diisii, Maka program akan meminta masukan kembali
        while nama == "":
            nama = input("Masukan nama       : ")
        
        # validasi. Kika variabel tersebut tidak diisii, Maka program akan meminta masukan kembali
        while formatif == "":
            formatif = input("Nilai Formatif     : ")
        
        # validasi. Kika variabel tersebut tidak diisii, Maka program akan meminta masukan kembali
        while uts == "":
            uts = input("Nilai UTS          : ")
        
        # validasi. Kika variabel tersebut tidak diisii, Maka program akan meminta masukan kembali
        while uas == "":
            uas = input("Nilai UAS          : ")
        
        # membuat baris baru 
        print("\n")

        # PROSES Nilai Akhir ------------------------------------------------------------
        nilai_akhir = float(formatif)*0.4 + float(uts)*0.3 + float(uas)*0.3
        
        # PROSES Huruf Mutu ------------------------------------------------------------
        if(nilai_akhir >= 80):
            huruf_mutu = 'A'
        elif(nilai_akhir >=70):
            huruf_mutu = 'B'
        elif(nilai_akhir >=60):
            huruf_mutu = 'C'
        elif(nilai_akhir >=50):
            huruf_mutu = 'D'
        else:
            huruf_mutu = 'E'

        # Keluaran ------------------------------------------------------------
        print("Keluaran program ...")
        print("NIM anda     : "+str(nim))
        print("Nama anda    : "+str(nama))
        print("Nilai Akhir  : "+str(nilai_akhir))
        print("Huruf Mutu   : "+str(huruf_mutu))

        # membuat baris baru
        print("\n")

        
        # Jika pengguna memasukan "Ya", maka program akan mengulang kembali program
        ulangi = input("Ulangi proses : ")
    
    