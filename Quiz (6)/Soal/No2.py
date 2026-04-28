i = [["Nasi goreng", 15000], ["Es teh", 5000], ["Mie goreng", 10000], ["Ayam penyet", 13000], ["Susu sapi segar", 9000]]

print(i[0])

def pesanan():
    for x in range (4):
        x += 1
        if x == 5:
            break
        print(i[x])


pesanan()

def pesan():
    print("Ketik 0 untuk berhentikan program")
    t = int(input("Masukan pilihan (1 - 5): "))

    while t == 0:
        break

    if t <= 5:
        print(i[t])
    elif t < 0 | t >= 6:
        print("nomor tidak valid")

t = pesan()

while t != 0:
    pesan()

while t == 0:
    break