# PROGRAM Pendalaman-Perulangan


# DEKLARASI Pustaka
import builtins
import os # os, pustaka mengenali os yg digunakan

    
# ALGORITMA
if __name__=="__main__":
    # Hapus layar / clear screen
    # Baris pertama dari keluaran program adalah masukan program bukan path directory program. 
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # --------------------------------------------------------
    ''' proses nomor 1
        Buatlah program untuk menampilkan hasil berikut
        *
        *   *
        *   *   *
        *   *   *   *
        *   *   *   *   *
    '''
    print("Nomor 1 --------------------")
    
    # deklarasi variabel local dan masukan program
    rows = 5
    i = 0
    j = 0
    
    for i in range(1, rows + 1): # proses program
        for j in range(1, i + 1): # proses program
            print('*', end=' ') # output program berupa bilangan
        print('') # output program untuk membuat baris baru
    
    # --------------------------------------------------------
    ''' proses nomor 2
        Buatlah program untuk menampilkan hasil berikut
                        *
                    *   *
                *   *   *
            *   *   *   *
        *   *   *   *   *
    '''
    print("\nNomor 2 --------------------")
        
    n = 5
    k = 2*n - 2

    for i in range(0, n):
        
        for j in range(0, k):
            print(end=" ")
        
        k = k - 2
    
        for j in range(0, i+1):
            print("* ", end="")
        
        print("\r")
    
    
    # --------------------------------------------------------
    ''' proses nomor 3
        Buatlah program untuk menampilkan hasil berikut
        *
        *   *
        *   *   *
        *   *   *   *
        *   *   *   *   *
        *   *   *   *
        *   *   *
        *   *
        *
    '''
    print("\nNomor 3 --------------------")
    
    rows = 5
    for i in range(0, rows):
        for j in range(0, i + 1):
            print("*", end=' ')
        print("\r")

    for i in range(rows, 0, -1):
        for j in range(0, i - 1):
            print("*", end=' ')
        print("\r")