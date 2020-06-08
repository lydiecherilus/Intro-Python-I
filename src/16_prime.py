# Write a program to determine if a number, given on the command line, is prime.

# taking input from user
num = int(input("Enter a number: "))

# if given number is greater than 1 
if num > 1: 
       # iterate from 2 to n / 2  
   for i in range(2, num):          
       # if num is divisible by any number between 2 and n / 2, it is not prime  
       if (num % i) == 0: 
           print(num, "is not a prime number") 
           break
   else: 
       print(num, "is a prime number") 

# if the entered number is less than or equal to 1, it is not prime number
else: 
   print(num, "is not a prime number") 