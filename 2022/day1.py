def part1(CalCount):
    maxCal = max(CalCount)
    print(f" * Part one - Answer: {maxCal}")


def part2(calCount):
    top3Sum = 0
    for elf in range(3):
        top3Sum += max(calCount)
        calCount.remove(max(calCount))

    print(f" * Part two - Answer: {top3Sum}")


def main():
    elfCalCount = []
    currentCalCount = 0

    with open("./AdventOfCode/2022/input/day1-input", "r") as file:
        text = file.readlines()
        for line in text:
            if line == "\n":
                elfCalCount.append(currentCalCount)
                currentCalCount = 0
            else:
                currentCalCount += int(line)

    print("[--- Day 1: Calorie Counting ---]")
    part1(elfCalCount)
    part2(elfCalCount)


main()
