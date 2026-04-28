def tambah_matriks(A, B):
    baris, kolom = len(A), len(A[0])
    hasil = [[A[i][j] + B[i][j] for j in range(kolom)] for i in range(baris)]
    return hasil

def kurang_matriks(A, B):
    baris, kolom = len(A), len(A[0])
    hasil = [[A[i][j] - B[i][j] for j in range(kolom)] for i in range(baris)]
    return hasil

def kali_matriks(A):
    baris, kolom = len(A), len(A[0])
    hasil = [[A[i][j] * 4 for j in range(kolom)] for i in range(baris)]
    return hasil

A = [[5, 3, 1], [2, 8, 4], [6, 0, 7]]
B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("matriks tambah")
C_tambah = tambah_matriks(A, B)
for baris in C_tambah:
    print(baris)

print("----------")
print("matriks kurang")
C_kurang = kurang_matriks(A, B)
for baris in C_kurang:
    print(baris)

print("----------")
print("Perkalian matriks")
C_kali = kali_matriks(A)
for baris in C_kali:
    print(baris)