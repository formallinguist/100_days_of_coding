# Using Break statement.

available = 7

x = int(input('How many candies do you need?'))

i = 1
while i <= x:
    if i > available:
        print('sorry, out of stock')
        break
    print('candy')

    i += 1

print('bye')

#Using continue.

for i in range (101):
    if i % 3 == 0:
        continue
    print(i)
print('bye')

#Using pass:

for i in range (0,100):

    if i % 2 == 0:
        pass
    
    else:
        print(i)
print('bye')