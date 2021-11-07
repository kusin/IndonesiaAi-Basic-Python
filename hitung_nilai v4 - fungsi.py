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

# DEKLARASI Fungsi 
# fungsi hitung nilai akhir
def func_nilai_akhir(param_formatif, param_uts, param_uas):
    # default nilai akhir = 0
    hasil = 0

    # rumus menghitung nilai akhir
    hasil = param_formatif*0.4 + param_uts*0.3 + param_uas*0.3

    # return value nilai akhir
    return hasil

def func_huruf_mutu(param_nilai_akhir):
    # default huruf mutu = E
    hasil = 'E'

    if(param_nilai_akhir >= 80):
        hasil = 'A'
    elif(param_nilai_akhir >=70):
        hasil = 'B'
    elif(param_nilai_akhir >=60):
        hasil = 'C'
    elif(param_nilai_akhir >=50):
        hasil = 'D'
    else:
        hasil = 'E'

    # return value huruf mutu
    return hasil

# DEKLARASI Variabel
nim = ""
nama = ""
formatif = ""
uts = ""
uas = ""
nilai_akhir = ""
huruf_mutu = ""

# ALGORITMA
if __name__=="__main__":
    # Hapus layar / clear screen
    # Baris pertama dari keluaran program adalah masukan program bukan path directory program. 
    os.system('cls' if os.name == 'nt' else 'clear')

    # Masukan Program
    print("Masukan program ...")
    
    # validasi. Kika variabel tersebut tidak diisii, Maka program akan meminta masukan kembali
    while nim == "":
        nim = input("Masukan nim : ")
    
    # validasi. Kika variabel tersebut tidak diisii, Maka program akan meminta masukan kembali
    while nama == "":
        nama = input("Masukan nama : ")
    
    # validasi. Kika variabel tersebut tidak diisii, Maka program akan meminta masukan kembali
    while formatif == "":
        formatif = input("Nilai Formatif : ")
    
    # validasi. Kika variabel tersebut tidak diisii, Maka program akan meminta masukan kembali
    while uts == "":
        uts = input("Nilai UTS : ")
    
    # validasi. Kika variabel tersebut tidak diisii, Maka program akan meminta masukan kembali
    while uas == "":
        uas = input("Nilai UAS : ")
    
    # membuat baris baru 
    print("\n")

    # PROSES Nilai Akhir
    # akan memanggil fungsi 'func_nilai_akhir' dengan parameter formatif, uts, uas 
    nilai_akhir = func_nilai_akhir(float(formatif), float(uts), float(uas))

    # PROSES Huruf Mutu
    # akan memanggil fungsi 'func_huruf_mutu' dengan parameter nilai akhir 
    huruf_mutu = func_huruf_mutu(float(nilai_akhir))
    
    # Keluaran
    print("Keluaran program ...")
    print("NIM anda     : "+str(nim))
    print("Nama anda    : "+str(nama))
    print("Nilai Akhir  : "+str(nilai_akhir))
    print("Huruf Mutu   : "+str(huruf_mutu))

    print("\n")