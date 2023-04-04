
#For else.
nums = [12,16,18,20,25]

for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print("Not found")
    
#Prime number.

num = 10

for i in range (2,num):
    print(i)
    if num % i == 0:
        print("not a prime number")
        break
else:
    print("prime number")

