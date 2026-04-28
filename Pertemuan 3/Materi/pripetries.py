class makanan:
    asal = "Indonesia"
    rasa = ""

    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

makananSatu = makanan("Rendang", 15000)
makananDua = makanan("Lontong", 12000)
print(makananSatu.nama)
print(makananSatu.harga)
del makananSatu.harga
#print(makanannSatu.harga)  akan error 
#karena propertinya sudah dihapus
print(makananDua.asal)
makananSatu.rasa = "pedas"
print(makananSatu.rasa)
makananSatu.nama = "Sate"
print(makananSatu.nama)
makananDua.kuah = "Berkuah"
print(makananDua.kuah)