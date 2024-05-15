#!/usr/bin/env python3
# Author: Rob Akkerman
# Author ID: 106234206
# Date Created: 2024/5/15

import sys

# Check if a command-line argument was provided
if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    # If no argument was provided, set the default timer value to 3
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
