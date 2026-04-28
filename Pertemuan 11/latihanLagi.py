id_karyawan = [
1021, 1045, 1089, 1102, 1157, 1203, 1245, 1312, 1378, 1401, 1456, 1502, 1567, 1634, 1700
]

def idkaryawan(id, tujuan):
    kanan = 0
    kiri = len(id) - 1
    b = 0

    while kanan <= kiri:
        tengah = (kanan + kiri) // 2
        b += 1

        if id[tengah] == tujuan:
            return tengah, b

        if id[tengah] < tujuan:
            kanan = tengah + 1
        else:
            kiri = tengah - 1
    return -1, b

x = int(input("Masukkan ID karyawan yang dicari: "))

letak, banding = idkaryawan(id_karyawan, x)

if letak != -1:
    print(f"Proses perbandingan: {banding} kali")
    print(f"ID {x} ditemukan! Posisi ke-{letak + 1} dalam daftar.")
else:
    print(f"Proses perbandingan: {banding} kali")
    print(f"ID {x} tidak terdaftar sebagai karyawan.")