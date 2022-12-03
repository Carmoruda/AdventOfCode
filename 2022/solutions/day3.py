def totalSum(priority):
    totalSum = 0

    for item in priority:  # Calculate the total sum
        if item[0].isupper():
            totalSum += ord(item[0]) - 38  # Add uppercase values
        else:
            totalSum += ord(item[0]) - 96  # Add lowercase values

    return totalSum


def part1(text):
    priorityList = []  # Priority items

    for line in text:
        length = int(len(line) / 2)  # Rucksack length
        priorityItem = set(line[:-length]) & set(line[-length:])
        priorityList.append(list(priorityItem))

    print(f" * Part one - Answer: {totalSum(priorityList)}")


def part2(text):
    priorityList = []  # Priority items
    line = 0  # Line number

    length = int(len(text) / 3)  # Loop total length
    for ii in range(length):
        priorityItem = set(text[line]) & set(text[line + 1]) & set(text[line + 2])
        priorityList.append(list(priorityItem))
        line += 3
    print(f" * Part two - Answer: {totalSum(priorityList)}")


if __name__ == "__main__":
    with open("./AdventOfCode/2022/inputs/202203", "r") as file:
        # Read the lines from input and remove the newline character
        text = [line[:-1] for line in file.readlines()]

    print("[--- Day 3: Rucksack Reorganization ---]")
    part1(text)
    part2(text)
