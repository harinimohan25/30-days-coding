# Python program to find the factorial of a number using recursion

def factorial(n):
   if n == 1:
        return n
   else:
       return n*factorial(n-1)

# Change this value for a different result
num = int(raw_input())
print factorial(num)