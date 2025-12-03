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
