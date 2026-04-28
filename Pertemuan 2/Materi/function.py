#Function
def my_function():
  print("Hello from a function")

def my_function():
  print("Hello from a function")
my_function()

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)


#argument
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")


#*args / **kwargs
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")


def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

#scope
def myfunc():
  x = 300
  print(x)
myfunc()

x = 300
def myfunc():
  print(x)
myfunc()
print(x)

def myfunc():
  global x
  x = 300
myfunc()
print(x)

x = "global"
def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)
outer()
print("Global:", x)

#decorators
def changecase(func):
  def myinner():
    return func().upper()
  return myinner
@changecase
def myfunction():
  return "Hello Sally"
print(myfunction())

#lambda
x = lambda a : a + 10
print(x(5))

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)


#recursion
def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)
countdown(5)


#generators
def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)