#!/usr/bin/env python3

def main():
    left = []
    right = []

    with open ('input.txt', 'r') as input:
        for line in input:
            left.append(int(line.split('   ')[0]))
            right.append(int(line.split('   ')[1]))

    left.sort()
    right.sort()

    # Calculate the total distance between the lists
    distance = 0
    for i in range(len(left)):
        distance += abs(left[i] - right[i])
    print(distance)

    # Calculate the similarity score between the lists
    similarity = 0
    for i in range(len(left)):
        similarity += left[i] * right.count(left[i])
    print(similarity)

if __name__ == "__main__":
    # execute only if run as a script
    main()
