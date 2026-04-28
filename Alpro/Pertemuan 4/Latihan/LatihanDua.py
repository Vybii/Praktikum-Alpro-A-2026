try:
    angkaPertama = int(input("Masukkan angka pertama: "))
    angkaKedua = int(input("Masukkan angka kedua: "))
    hasil = angkaPertama / angkaKedua
    print(f"Hasil: {hasil}")
except ValueError:
    print("Input harus angka")
except ZeroDivisionError:
    print("Penyebut tidak boleh nol")
except Exception as e:
    print(f"Error yang gak terduga: {e}")