f = open("input.txt", "r")
Lines = f.readlines()

res_map = {
    'A X':4,
    'A Y':8,
    'A Z':3,
    'B X':1,
    'B Y':5,
    'B Z':9,
    'C X':7,
    'C Y':2,
    'C Z':6,
}
# Strips the newline character
score = 0
for line in Lines:
    score += res_map[line.strip()]

f.close

print(score)