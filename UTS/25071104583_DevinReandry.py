DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]


#===========================BAGIAN A=========================#
def tebak_angka(angka_rahasia, maks_percobaan):
    '''Cek tebakan benar atau salah'''
    sisa_percobaan = maks_percobaan

    while sisa_percobaan > 0:
        try:
            tebakan = int(input(f" Sisa percobaan: {sisa_percobaan}"))
        except ValueError:
            print("Input angka")
            continue

        if tebakan < angka_rahasia:
            print("Terlalu kecil")
        elif tebakan > angka_rahasia:
            print("Terlalu besar")
        else:
            print("Benar!")
            return True, sisa_percobaan
        sisa_percobaan -= 1
    return False, 0

def hitung_skor(berhasil, sisa_percobaan):
    '''hitung skor yang didaparkan'''
    if berhasil:
        return sisa_percobaan * 10
    return 0

def main_satu_ronde(nama, nomor_ronde):
    '''ronde yang dimainkan'''
    indeks = nomor_ronde % len(DAFTAR_ANGKA)
    angka_rahasia = DAFTAR_ANGKA[indeks]
    berhasil, sisa = tebak_angka(angka_rahasia, 7)
    skor = hitung_skor(berhasil, sisa)
    return [nama, skor]

#===========================BAGIAN B=========================#
def tampilkan_riwayat(riwayat):
    '''output tabel history'''
    if len(riwayat) == 0:
        print("Belum ada riwayat")
        return
    print("No\tNama\tSkor")
    for i in range(len(riwayat)):
        print(f"{i+1}\t{riwayat[i][0]}\t{riwayat[i][1]}")


#===========================BAGIAN C=========================#
def selection_sort_riwayat(riwayat):
    '''salinan list riwayat'''
    hasil = riwayat.copy()
    n = len(hasil)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if hasil[j][1] > hasil[max_idx][1]:
                max_idx = j
        hasil[i], hasil[max_idx] = hasil[max_idx], hasil[i]
    return hasil


def tampilkan_leaderboard(riwayat):
    if len(riwayat) == 0:
        print("Belum ada data leaderboard.")
        return
    urut = selection_sort_riwayat(riwayat)
    print("Rank\tNama\tSkor")
    for i in range(len(urut)):
        tanda = " *" if i == 0 else ""
        print(f"{i+1}\t{urut[i][0]}\t{urut[i][1]}{tanda}")


def main():
    nama = input("Masukkan nama pemain: ")
    riwayat = []
    ronde = 0

    while True:
        print(f"\n=== RONDE {ronde + 1} ===")
        hasil = main_satu_ronde(nama, ronde)
        riwayat.append(hasil)
        ronde += 1
        lanjut = input("Main lagi? (y/n): ").lower()
        if lanjut != 'y':
            break

    tampilkan_riwayat(riwayat)
    tampilkan_leaderboard(riwayat)


main()