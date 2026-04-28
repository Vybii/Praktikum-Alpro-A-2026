class orang():
    def __init__(self, nama, umur, tinggi, berat = 48):
        self.nama = nama
        self.umur = umur
        self.tinggi = tinggi
        self.berat = berat

objekSatu = orang('Devin', 18, 178, 58)
objekDua = orang("Balqis", 18, 160)
print(objekSatu.nama)
print(objekSatu.umur)
print(objekSatu.tinggi)
print(objekSatu.berat)
print(objekDua.berat)

print(end = "\n\n")

class bus():
    pass

objekAja = bus()
objekAja.nama = "TAM"
objekAja.ban = 8

print(objekAja.nama)
print(objekAja.ban)