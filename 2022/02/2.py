# A -> Rock -> X (1 point)
# B -> Paper -> Y (2 points)
# C -> Scissors -> Z (3 points)

with open('input_2.txt') as f:
    data = f.read().split('\n')
    shapes = [shape.split(" ") for shape in data if shape]
def part_one():
# A beats Z (0 + 3), draws X (3 + 1) and loses Y (6 + 2)
# B beats X (0 + 1), draws Y (3 + 2) and loses Z (6 + 3)
# C beats Y (0 + 2), draws Z (3 + 3) and loses X (6 + 1) 
    score = 0
    for i, j in shapes:
        if i == 'A':
            if j == 'Z':
                score += 3
            if j == 'X':
                score += 4
            if j == 'Y':
                score += 8
        if i == 'B':
            if j == 'X':
                score += 1
            if j == 'Y':
                score += 5
            if j == 'Z':
                score += 9
        if i == 'C':
            if j == 'Y':
                score += 2
            if j == 'Z':
                score += 6
            if j == 'X':
                score += 7

    print(f"1. Score is {score}")


def part_two():
# A = Rock     (1 p)
# B = Paper    (2 p)
# C = Scissors (3 p)
# X = Lose     (0 p)
# Y = Draw     (3 p)
# Z = Win      (6 p)
    score = 0
    for i, j in shapes:
        if i == 'A': #Rock
            if j == 'X': # Loses against C
                score += (0 + 3)
            if j == 'Y': # Draws against A
                score += (3 + 1)
            if j == 'Z': # Wins against B
                score += (6 + 2)
        if i == 'B': #Paper
            if j == 'X': # Loses against A
                score += (0 + 1)
            if j == 'Y': # Draws against B
                score += (3 + 2)
            if j == 'Z': # Wins against C
                score += (6 + 3)
        if i == 'C': # Scissors
            if j == 'X': # Loses against B
                score += (0 + 2)
            if j == 'Y': # Draws against C
                score += (3 + 3)
            if j == 'Z': # Wins against A
                 score += (6 + 1)
    print(f"2. Score is {score}")


def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()