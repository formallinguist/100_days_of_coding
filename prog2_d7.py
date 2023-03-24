nums = [25, 12, 36, 95, 14]

nums[0]

nums[4]

nums[2:]

nums[-1]

nums[-5]

names = ['Naveen','Kiran','John']

print(names)

values = [9.5,"Ravi",25]

print(values)

mil = [nums,names]

print(mil)

nums.append(45) #append function appends at the end.

print(nums)

nums.insert(2,77) # inserts value at the second number.

print(nums)

nums.remove(14)

print(nums)

nums.pop(1) # remove element with  the index.

print(nums)

nums.pop() # removes last element if we donot use index.

print(nums)

del nums[2:]

print(nums)

nums.extend([29,12,34,56])#when we want to add multiple values.

print(nums)

print(min(nums))

print(max(nums))

print(sum(nums))

nums.sort()

print(nums)
