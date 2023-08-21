#!/usr/bin/env python
# coding: utf-8


# In[ ]:


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

print("Simple Calculator")
print("Operations:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Select an operation (1/2/3/4): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operation == '1':
    print("Result:", add(num1, num2))
elif operation == '2':
    print("Result:", subtract(num1, num2))
elif operation == '3':
    print("Result:", multiply(num1, num2))
elif operation == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid operation")


# In[ ]:





# In[ ]:




