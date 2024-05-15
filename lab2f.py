#!/usr/bin/env python3
# Author: Rob Akkerman
# Author ID: 106234206
# Date Created: 2024/5/15

import sys

# Check if the required command-line argument is provided
if len(sys.argv) < 2:
    print("Usage: {} <timer>".format(sys.argv[0]))
    sys.exit(1)

timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")

