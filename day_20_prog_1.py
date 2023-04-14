# getting the array from the user.

#import array

from array import*

arr = array('i',[])

n = int(input("Enter the length of the array"))

for i in range(n):
    x = int(input("Enter the next value "))
    arr.append(x)
    
print(arr)

value = int(input('Enter the input'))
k = 0
for i in arr:
    if i == value:
        print(k)
        break
    k += 1
    
# instead of the above code we can use the inbuilt function.
print(arr.index(value))