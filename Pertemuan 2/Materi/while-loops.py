i = 1
while i < 6:
  print(i)
  i += 1

i = 9
while i < 10:
  print(i)
  if i == 9:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")