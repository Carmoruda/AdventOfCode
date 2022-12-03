def part1(play, points):
    gameDict = {"X": "A", "Y": "B", "Z": "C"}  # Shape equivalences
    totalSum = 0  # Total sum of round points

    for round in play:
        totalSum += points[round[1]]  # Add score of the selected shape

        if round[0] == round[1]:  # Draw
            totalSum += 3
        elif (
            (round[0] == "C" and round[1] == "A")
            or (round[0] == "B" and round[1] == "C")
            or (round[0] == "A" and round[1] == "B")
        ):  # Player 2 wins
            totalSum += 6
    print(f" * Part one - Answer: {totalSum}")


def part2(play, points):
    winDict = {"A": "C", "B": "A", "C": "B"}  # Winning shape
    loseDict = {"A": "B", "B": "C", "C": "A"}  # Losing shape
    totalSum = 0  # Total sum of round points

    for round in play:
        if round[1] == "A":  # Lose
            shape = winDict[round[0]]  # Choose losing shape
            totalSum += points[shape]  # Add points
        elif round[1] == "B":  # Draw
            shape = round[0]  # Choose same shape
            totalSum += points[shape] + 3  # Add points
        else:
            shape = loseDict[round[0]]  # Choose winning shape
            totalSum += points[shape] + 6  # Add points
    print(f" * Part two - Answer: {totalSum}")


def main():
    puntDict = {"A": 1, "B": 2, "C": 3}  # Points per shape
    finalSplit = []  # List for player's plays

    with open("./AdventOfCode/2022/inputs/202202", "r") as file:
        text = file.readlines()

        for line in text:
            # Change player 2 shape to equivalent
            changeLine = ["".join([gameDict.get(c, c) for c in line])]
            for i in changeLine:
                # Split player 1 and 2 plays
                finalSplit.append(changeLine[0].split())

    print("[--- Day 2: Rock Paper Scissors ---]")
    part1(finalSplit, puntDict)
    part2(finalSplit, puntDict)


main()
