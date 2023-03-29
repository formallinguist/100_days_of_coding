#Number system conversion.

print(bin(25))

print(oct(25))

print(hex(10))

print(11001)

#swapping numbers.
a = 5
b = 6

temp = a

a = b
b = temp

print(a)
print(b)

#Swapping variables without using a third variable.

a = a + b
b = a - b
a = a - b

print(a)
print(b)

#Reversing by rotation.
a,b = b,a

print(a)
print(b)