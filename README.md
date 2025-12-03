# Module 4: Functions & Modules in Python
This assignment demonstrates the use of **functions** and the **math module** in Python through two tasks.

## Task 1: Calculate Factorial Using a Function

### Problem Statement
Write a Python program that:
1. Defines a function named ‘factorial’ that takes a number as an argument and calculates its factorial using a loop or recursion.
2. Returns the calculated factorial.
3. Calls the function with a sample number and prints the output.

### Solution Approach
- The program asks the user to enter a number.
- Input validation ensures only positive integers are accepted.
- A function ‘factorial(num)’ is defined:
  - Uses a loop to multiply numbers from ‘1’ to ‘num’.
  - Returns the factorial result.
- The result is printed in a formatted message.

### Sample Input/Output
Enter a number: 5 
Factorial of 5 is: 120

### How to Run
1. Save the script as `factorial.py`.
2. Run in terminal:
    factorial.py


Task 2: Using the Math Module for Calculations

Problem Statement
Write a Python program that:

1.	Asks the user for a number as input.
2.	Uses the math module to calculate:
    -	Square root of the number
    -	Natural logarithm (log base e) of the number
    -	Sine of the number (in radians)
3.	Displays the calculated results.

Solution Approach: 
-	The program accepts integer or float input (positive or negative).
-	It uses built-in functions from the math module:
o	math.sqrt() for square root
o	math.log() for natural logarithm
o	math.sin() for sine

****Edge cases handled:

      - Zero input: log is undefined, sqrt is 0, sine is 0
      -	Negative input: sine works, but sqrt/log are not defined in real numbers
      -	Input validation ensures only numeric values are accepted.

Sample Input/Output:
    Enter a number: 4
    The square root of 4.0 is: 2.0
    The Natural logarithm 4.0 is: 1.3862943611198906
    The sin of 4.0 is: -0.7568024953079282

How to Run:

1.	Save the script as math_calculations.py.
2.	Run in terminal:

math_calculations.py

Notes
•	Task 1 only accepts positive integers.
•	Task 2 accepts floats and handles negative values gracefully for sine but warns for sqrt/log.
•	Input validation ensures users don’t enter characters or invalid formats.
