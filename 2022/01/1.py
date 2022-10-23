# --- Skeleton for aoc python code ---

with open('input_1.txt') as f:
    cals = f.read().strip().split("\n")

# Logic
total_calories = []
sumatory = 0

for c in cals:
    if c != '':
        sumatory += int(c)
    else:
        total_calories.append(sumatory)
        sumatory = 0

    
def part_one():
    print(f"The highest num of calories is {max(total_calories)}")

def part_two():
    total_calories.sort(reverse=True)
    top_three = 0
    for i in range(3):
        top_three += total_calories[i]

    print(f"The addition of the top 3 highest calories is {top_three}")

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()