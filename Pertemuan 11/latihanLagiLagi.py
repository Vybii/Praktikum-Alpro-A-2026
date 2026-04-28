rak_a = ["BK-045", "BK-012", "BK-078", "BK-033", "BK-091", "BK-027", "BK-056"]
rak_b = ["BK-011", "BK-023", "BK-035", "BK-047", "BK-059", "BK-071", "BK-083", "BK-095"]

def linearSearch(rak1, tujuan):
    for i in range(len(rak1)):
        if rak1[i] == tujuan:
            return i
    return -1

def binarySearch(rak2, tujuan):
    kiri, kanan = 0, len(rak2) - 1
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if rak2[tengah] == tujuan:
            return tengah
        elif rak2[tengah] < tujuan:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return -1

x = input("Masukkan kode buku yang dicari: ")

print("Mencari di Rak A (Linear Search)...")
kesatu = linearSearch(rak_a, x)
if kesatu != -1:
    print(f"{x} ditemukan di Rak A, posisi ke-{kesatu + 1}.")
else:
    print(f"{x} tidak ditemukan di Rak A.")

print("Mencari di Rak B (Binary Search)...")
kedua = binarySearch(rak_b, x)
if kedua != -1:
    print(f"{x} ditemukan di Rak B, posisi ke-{kedua + 1}.")
else:
    print(f"{x} tidak ditemukan di Rak B.")

if kesatu != -1 and kedua != -1:
    print(f"Kesimpulan: Buku {x} tersedia di Rak A dan Rak B.")
elif kesatu != -1:
    print(f"Kesimpulan: Buku {x} tersedia di Rak A.")
elif kedua != -1:
    print(f"Kesimpulan: Buku {x} tersedia di Rak B.")
else:
    print(f"Kesimpulan: Buku {x} tidak tersedia di kedua rak.")