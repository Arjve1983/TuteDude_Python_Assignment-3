'''                             Module 4: Functions & Modules in Python 

Task 1: Calculate Factorial Using a Function 

Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.'''

User_input=input("Enter a number: ")
if User_input.isdigit():
        num=int(User_input)
        def factorial(num):
            result=1
            for i in range(1,num+1):
                result*=i
            return result
        print(f"Factorial of {num} is: {factorial(num)}")
else:
     print("Enter a Positive number not a character!")


'''                                         Task 2: Using the Math Module for Calculations
 
Problem Statement: Write a Python program that:

1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
'''
import math
user_input=input("Enter a number: ")
if user_input.lstrip('-').replace('.',"",1).isdigit():
    num=float(user_input)
    if num == 0:
        print("Square root of 0 is 0")
        print("Logarithm is undefined for zero!")
        print("Sine of 0 is 0")

    elif num>0:
        Sqrt_result=math.sqrt(num)
        log_result=math.log(num)
        Sin_result=math.sin(num)
        print(f"The square root of {num} is: {Sqrt_result}")
        print(f"The Natural logarithm {num} is: {log_result}")
        print(f"The sin of {num} is: {Sin_result}")
    else:

        print(f"Sine of {num} (in radians) is: {math.sin(num)}")
        print("Square root and logarithm are not defined for negative numbers in real math!")
else:
    print("Invalid input! Please enter a number only")

