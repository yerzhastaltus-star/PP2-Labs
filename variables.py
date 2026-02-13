x = 4
y = "Pudge"

print(x)
print(y)

a = str(3)
b = int(3)
c = float(3)
print(a, b, c)

d = 5
e = "John"
print(type(x))
print(type(y))

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


myvar = "Invoker"
my_var = "Lina"
_my_var = "Axe"
myVar = "IO"
MYVAR = "Enigma"
myvar2 = "Puck"
print(myvar, my_var, _my_var, myVar, MYVAR, myvar2)



x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))	
x = tuple(("apple", "banana", "cherry"))
x = range(6)	
x = dict(name="John", age=36)	
x = set(("apple", "banana", "cherry"))	
x = frozenset(("apple", "banana", "cherry"))	
x = bool(5)	
x = bytes(5)	
x = bytearray(5)	
x = memoryview(bytes(5))
x = None