#!/usr/bin/env python3

def is_safe(levels):
    differences = []
    for i in range(len(levels) - 1):
        differences.append(int(levels[i + 1]) - int(levels[i]))
    return all(-3 <= increment <= -1 for increment in differences) or all(1 <= increment <= 3 for increment in differences)

def main():
    with open ('input.txt', 'r') as input:
        # Calculate the number of safe reports
        safe = 0
        for report in input:
            levels = report.split()
            if is_safe(levels):
                safe += 1
            # Calculate the number of additional safe reports with the dampener
            else:
                for i in range(len(levels)):
                    dampened = levels[:i] + levels[i+1:]
                    if is_safe(dampened):
                        safe += 1
                        break
        print(safe)

if __name__ == "__main__":
    # execute only if run as a script
    main()
