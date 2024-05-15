#!/usr/bin/env python3
import sys

# Check the number of command-line arguments
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
else:
    # Assign arguments to variables
    name = sys.argv[1]
    age = sys.argv[2]

    # Print the output
    print(f'Hi {name}, you are {age} years old.')

