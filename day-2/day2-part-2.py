f = open("input.txt", "r")
Lines = f.readlines()

res_map = {
    'A X':3,
    'A Y':4,
    'A Z':8,
    'B X':1,
    'B Y':5,
    'B Z':9,
    'C X':2,
    'C Y':6,
    'C Z':7,
}
# Strips the newline character
score = 0
for line in Lines:
    score += res_map[line.strip()]

f.close

print(score)