#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to avoid an infinite loop
    return result

# Check if a command-line argument is provided
if len(sys.argv) < 2:
    print("Usage: ./factorial.py <number>")
    sys.exit(1)

# Convert the command-line argument to an integer and calculate the factorial
try:
    number = int(sys.argv[1])
    f = factorial(number)
    print(f)
except ValueError:
    print("Please provide a valid integer.")
    sys.exit(1)
