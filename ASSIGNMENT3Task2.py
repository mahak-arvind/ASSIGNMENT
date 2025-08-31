import math
#Task 2: Using the Math Module for Calculations
from math import*
num=int(input('enter your number : '))
sq=math.sqrt(num)
log=math.log(num,2)
s=math.sin(float(num))

print(f'square root of {num} is {sq}')
print(f'logarithm of {num} is {log}')
print('sine: ',s)

