#positive or negative num

i = int(input("Enter a number:"))

if i==0:
    print("zero")
elif i<0:
    print("neg")    
else:
    print("pos")    
------------------------------------------
# odd or even

n = int(input("Enter a num:"))

if n%2==0:
    print("even")
else:
    print("odd")    
-------------------------------------------
# sum of n natural no.s

num = int(input('Enter the number: '))
sum = 0

for i in range(1, num+1):
    sum = sum+i
print(sum)
-----------------------------------

# greatest of two no.s

n1, n2= 10, 34

if n1>n2:
    print("n1 is greater")
else:
    print("n2 is greater")

------------------------------------
# max of a num using func

n1, n2 = 10,4
print(max(n1,n2))

------------------------------------
# greatest of 3 nos

n1, n2, n3 = 67, 144, 8

if n1>n2:
    if n1>n3:
        print("n1 is greatest")
    else:
        print("n3 is greatest")
elif n2>n3:
    print("n2 is greatest")            
    
    # or

# greatest of 3 no.s

n1, n2, n3 = 30, 54, 32

if n1>n2 and n1>n3:
    print("n1 is greater")
elif n2>n1 and n2>n3:
    print("n2 is greater")
else:
    print("n3 is greater") 
-------------------------------------
# sum of all no.s in the given range

n1 = 3
n2 = 8
sum = 0

for i in range(n1, n2+1):
    sum = sum+i
print(sum)   

----------------------------------------
# leap year or not

year = 2024

if (year%4 ==0 and year%100!=0) or year%400==0:
    print("leap year")
else:
    print("not a leap year")

# or------

year = 2400

if year%400==0:
    print("leap year")
else:
    print("Not a leap year")   
--------------------------------------------------
# add two no.s

a = 1
b = 4

sum = a + b
print(f"sum of {a} and {b} is", sum)
-----------------------------------------
# even or odd

num = int(input("enter a num :"))

if num%2==0:
    print(f"{num} is even")
elif num%2!=0:
    print(f"{num} is odd")    
--------------------------------------------
# factorial using loop

num = int(input('Enter the number: '))
factorial = 1

for i in range(1, num+1):
    factorial = factorial*i
print(f"The factorial of {num} is {factorial}")       
-----------------------------------------------------
       
# type of none

None
type(None)
--------------------------------
# first n nat no.s using while loop

i = 1

while i<= 50:
    print(i)
    i = i+1
    
----------------------------------------
# patterns

n = 5

for i in range(n+1):
    print('*' * i)   
-----------------------------------------
# pattern 2

num = 3

for i in range(3):
    print(' ' * (num-i-1), end='')
    print('*' * (2*i+1), end='')
    print(' ' * (num-i-1))
-------------------------------------------
# sort

nums = [3, 8, 40, 4, 56, 78, 45, 67, 77]
nums.sort()
print(nums)
----------------------------------------
# prime or not

num = int(input("enter a num: "))

for i in range(2, num):
    if num % i ==0:
        print("not prime")
        break
    else:
        print("Prime")

# or-------

num = int(input('Enter a number: '))
prime = True

for i in range(2, num):
    if (num%i==0):
        prime = False
        break
if prime:
    print('This number is prime')    
else:
    print('This number is not prime')

------------------------------------------






