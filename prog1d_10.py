#Float
num = 2.5
print(type(num))
#Integers.
num = 5
print(type(num))
#Complex numbers.
num = 6 + 9j
print(type(num))

a = 5.6
b = int(a)

print(type(b))

k = float(b)
print(type(k))

k = 6
c = complex(b,k)
print(c)
print(type(c))

#Boolean
print(b<k)

bool = b < k
print(bool)
type(bool)

print(b > k)

print(int(True))

#List 
lst = [25,36,45,12]

print(type(lst))
#set
s = {25,36,45,15,12,25}
print(s)
print(type(s))

#Tuple
tup = (25,36,45,15,12,25)
print(tup)
print(type(tup))

#String.
str = "Ravi"
print(str)
print(type(str))

#Range:
range(0,10)
x = list(range(0,10))
print(x)

#Range of even numbers.
y = list(range(2,13,2))
print(y)

#Dictionary
d = {'ravi':'samsung','Teja':'Nokia','Navin':'Oneplus'}

print(d)

print(d['ravi'])

print(d.get('Teja'))
