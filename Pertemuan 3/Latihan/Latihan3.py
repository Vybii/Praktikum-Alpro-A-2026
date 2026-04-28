class Manusia:
    def __init__(self, nama, umur, tinggi, berat, ukaki):
        self.nama = nama
        self.umur = umur
        self.tinggi = tinggi
        self.berat = berat
        self.ukuranKaki = ukaki

    def Sapa(self):
        print("halo selamat sore", self.nama)

    def Umur(self):
        print("umur kamu adalah:", self.umur)

    def ukuranKaki(self):
        print("ukuran kaki mu adalah:", self.ukuranKaki, "cm")

p1 = Manusia("devin", 18, 178, 59, 15)
p2 = Manusia("said", 18, 175, 70, 14)
p3 = Manusia("angga", 18, 175, 59, 15)

p1.umur = 19
p1.Umur()