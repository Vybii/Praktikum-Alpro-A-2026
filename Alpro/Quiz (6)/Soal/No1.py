i = [[], ["Nasi goreng", 15000], ["Es teh", 5000], ["Mie goreng", 10000], ["Ayam penyet", 13000], ["Susu sapi segar", 9000]]

for x in range (5):
    x += 1
    if x == 6:
        break
    print(i[x])

t = int(input("Masukan pilihan (1 - 5): "))

if t <= 5:
    print(i[t])
else:
    print("nomor tidak valid")