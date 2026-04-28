class Suplemen:
    def __init__(self, nama, perhari, manfaat):
        self.nama = nama
        self.perhari = perhari
        self.manfaat = manfaat

    def makan(self):
        print("Dengan", end = " ")
        print("makan", self.nama, end = " ")
        print("sebanyak", self.perhari, end = " ")
        print("perhari, kita mendapatkan manfaat", self.manfaat)

    def ajakan(self):
        print("Ayo makan", self.nama)
        kenapa = self.makan()

p1 = Suplemen("Biotin", "1 pil", "rambut kuat")
p1.ajakan()