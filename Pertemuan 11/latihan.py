def linear(yes, tujuan):
    for i in range (len(yes)):
        if yes[i] == tujuan:
            return i
    return -1

pasien = [
"Budi Santoso", "Siti Rahayu", "Ahmad Fauzi", "Dewi Lestari", "Eko Prasetyo", "Fitri Handayani", "Gilang Ramadan", "Hana Pertiwi", "Irfan Maulana", "Joko Susilo"
]
x = input("Masukkan nama pasien yang dicari: ")

status = linear(pasien, x)

if status != -1:
    print(f"{x} ditemukan di urutan {status + 1}")
else:
    print(f"{x} tidak ada dalam daftar hari ini.")