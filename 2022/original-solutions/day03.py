def totalSum(priority):
    totalSum = 0

    # Calculate the total sum
    for item in priority:
        if item[0].isupper():
            totalSum += ord(item[0]) - 38  # Add uppercase values
        else:
            totalSum += ord(item[0]) - 96  # Add lowercase values

    return totalSum


def part1(text):
    priorityList = []

    for line in text:
        length = int(len(line) / 2)  # Rucksack length
        rucksackFirst = set(line[:-length])  # 1st rucksack
        rucksackSecond = set(line[-length:])  # 2nd rucksack
        priorityItem = rucksackFirst & rucksackSecond  # Priority item
        priorityList.append(list(priorityItem))  # Add to priority list

    print(f" * Part one - Answer: {totalSum(priorityList)}")


def part2(text):
    groupRucksacks = []
    totalRucksacks = []
    priorityList = []

    for line in text:
        if len(groupRucksacks) < 3:
            groupRucksacks.append(line)
        else:
            priorityItem = (
                set(groupRucksacks[0]) & set(groupRucksacks[1]) & set(groupRucksacks[2])
            )
            priorityList.append(list(priorityItem))
            groupRucksacks.clear()
            groupRucksacks.append(line)

    priorityItem = (
        set(groupRucksacks[0]) & set(groupRucksacks[1]) & set(groupRucksacks[2])
    )
    priorityList.append(list(priorityItem))

    print(f" * Part two - Answer: {totalSum(priorityList)}")


def main():
    with open("./AdventOfCode/2022/inputs/202203", "r") as file:
        # Read the lines from input and remove the newline character
        text = [line[:-1] for line in file.readlines()]

    print("[--- Day 3: Rucksack Reorganization ---]")
    part1(text)
    part2(text)


main()
