#Calculate Factorial Using a Function recusion

num=int(input('enter your number : '))
def factorial(num):
    if num<2:
        return 1
    else:
        return num*factorial(num-1)

result=factorial(num)
print(f'factorial of {num}  is {result}')

#Calculate Factorial Using a Function recusion
num1=int(input('enter your number : ')) #5
n=1
for i in range(1,num1+1): #1,2,3,4,5,6
    n=n*i # n=1*1,1=1*2,2=2*3,6=6*4,24=24*5,

print(f'factorial of {num1} is {n}')


