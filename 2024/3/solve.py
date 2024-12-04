#!/usr/bin/env python3

import re

def main():
    with open('input', 'r') as input:
        results = 0
        enabled = True
        for i, j, k in re.findall(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))", input.read()):
            if i == "don't()":
                enabled = False
            elif i == "do()":
                enabled = True
            elif enabled: # or True
                results += int(j) * int(k)
        print(results)

if __name__ == "__main__":
    # execute only if run as a script
    main()
