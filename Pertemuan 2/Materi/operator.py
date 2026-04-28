sum1 = 100 + 250
sum2 = sum1 + 25
sum3 = sum2 + sum2

#arithmetic operator
x = 11
y = 3
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#assignment operators
x = 22
print(x)
x += 3
print(x)
x -= 4
print(x)
x *= 7
print(x)
x /= 8
print(x)
x %= 13
print(x)
x //= 4
print(x)
x **= 7
print(x := y)

#comparison operators
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(1 < x < 10)
print(1 < x and x < 10)

#logical operators
print(x > 0 and x < 10)
print(x < 5 or x > 10)
print(not(x > 3 and x < 10))

#identity operators
x = ["Biotin", "Zink"]
y = ["Biotin", "Zink"]
z = x
print(x is z)
print(x is y)
print(x == y)
print(x is not y)

#member operators
suplement = ["Biotin", "Zink", "Magnesium"]
print("Zink" in suplement)

suplement = ["Biotin", "Zink", "Magnesium"]
print("Besi" not in suplement)

text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)

#bitwise operators
print(6 & 3)
print(6 | 3)
print(6 ^ 3)

#operator precedence
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
print(5 + 4 - 7 + 3)