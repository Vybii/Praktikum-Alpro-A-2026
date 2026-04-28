#if
a = 6
b = 12
if b > a:
  print("b adalah bilangan kelipatan a")

number = 14
if number > 0:
  print("Angkanya positif")
  print("Hello")

is_logged_in = False
if is_logged_in:
  print("Welcome back!")
else:
  print("Oh hell nah")

#elif
a = 67
b = 67
if b > a:
  print("b lebih besar dari a")
elif a == b:
  print("a dan b setara")
elif a == 67:
  print("Six sevenn")

score = 90
if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

#else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

number = 7
if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

#shorthand if
a = 2
b = 330
print("A") if a > b else print("B")

a = 67
b = 69
bigger = a if a > b else b
print("Bigger is", bigger)

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#pass statement
a = 22
b = 77
if b > a:
  pass

age = 16
if age < 18:
  pass # TODO:
else:
  print("Access granted")