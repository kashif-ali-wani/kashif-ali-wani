import math


n = float(input("Enter a number: "))

square = n ** 2
cube = n ** 3
square_root = math.sqrt(n) if n >= 0 else "Not defined for negative numbers"
cube_root = n ** (1/3)


if n >= 0 and n.is_integer():
    factorial = math.factorial(int(n))
else:
    factorial = "Not defined (requires a non-negative integer)"


print("\nResults:")
print(f"Square of {n} = {square}")
print(f"Cube of {n} = {cube}")
print(f"Square root of {n} = {square_root}")
print(f"Cube root of {n} = {cube_root}")
print(f"Factorial of {n} = {factorial}")
