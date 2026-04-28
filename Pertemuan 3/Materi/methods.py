class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def informasi(self):
        return f"Dia bernama {self.nama} dan berumur {self.umur} tahun"
    def ulangtahun(self):
        self.umur += 1
        print(f"Selamat ulang tahun, sekarang kamu {self.umur} tahun")
    def __str__(self):
        return f"{self.nama} adalah Homo Sapiens yang berumur {self.umur} tahun"

Manusia = Manusia("Devin", 18)
print(Manusia.informasi())
Manusia.ulangtahun()
print(Manusia)

print("\n\n")

class Playlist:
    def __init__(self, nama):
        self.nama = nama
        self.lagu = []

    def tambahLagu(self, lagu):
        self.lagu.append(lagu)
        print(f"ditambahkan ke Playlist: {lagu}")

    def hapusLagu(self, lagu):
        if lagu in self.lagu:
            self.lagu.remove(lagu)
            print(f"Dihapus: {lagu}")

    def tunjukanLagu(self):
        print(f"Playlist '{self.nama}':")
        for lagu in self.lagu:
            print(f"- {lagu}")

Playlist = Playlist("Who Knows")
Playlist.tambahLagu("Chest Pain")
Playlist.tambahLagu("Yoake no uta")
Playlist.tambahLagu("I Thought I Saw Your Face Today")
Playlist.hapusLagu("Yoake no uta")
Playlist.tunjukanLagu()