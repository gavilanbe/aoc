# --- Skeleton for aoc python code ---
import string

with open('input_3.txt') as f:
    lines = f.read().split()

## Part 1

supplies = [[line[:len(line) // 2],line[len(line) // 2:]] for line in lines]
    
# Alphabet
alphabet = [letter for letter in list(string.ascii_lowercase) + list(string.ascii_uppercase)]
alphabet_dict = { k: v for v, k in enumerate(alphabet,1) }

def repeated_letters(supplies: list) -> string:
    repeated = ""
    for supply in supplies:
        for letter in supply[0]:
            if letter in supply[1]:
               repeated += letter
               break
    return repeated

def score(repeated: str) -> int:
    score = 0
    for char in repeated:
        score += alphabet_dict[char]
    return score

def part_one():
    print(f"Part 1. The score is: {score(repeated_letters(supplies))}")

## Part 2

group_of_three = []
counter = 0
for i in lines:
    group_of_three.append([lines[counter],lines[counter+1],lines[counter+2]])
    counter += 3
    if counter == len(lines):
             break

def three_repeated_letters(supplies: list) -> string:
    repeated = ""
    for supply in supplies:
        for letter in supply[0]:
            if letter in supply[1] and letter in supply[2]:
               repeated += letter
               break
    return repeated

def part_two():
    print(f"Part 2: {score(three_repeated_letters(group_of_three))}")

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()

