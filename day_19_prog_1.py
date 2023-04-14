#Array 
#remember to specify a proper type code.
import array as ar

from array import*

#Here we are using 'i' for integer.
values = array('i',[5,9,-8,4,2])

for i in range(len(values)):
    print(values[i])
    
#Here we are using characters.

char = array('u',['a','e','i','o','u'])

for i in range(len(char)):
    print(char[i])
    
vals = array('i',[5,9,-8,4,2])

new_array = array(vals.typecode,(a*a for a in vals))

for i in new_array:
    print(i)
    
#Using while loop for the above operation.

i = 0 

while i < len(new_array):
    print(new_array[i])
    i += 1
    