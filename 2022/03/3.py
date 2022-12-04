# --- Skeleton for aoc python code ---
import string

with open('input_3.txt') as f:
    lines = f.read().split()

## PART 1

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

def count_score(repeated: str) -> int:
    score = 0
    for char in repeated:
        score += alphabet_dict[char]
    return score

def part_one():
    print(f"PART 1. The score is: {count_score(repeated_letters(supplies))}")

## Part 2

group_of_three = [line for line in lines]

def part_two():
    print("part two is Z")

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()
