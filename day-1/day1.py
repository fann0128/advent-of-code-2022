f = open("input.txt", "r")
Lines = f.readlines()

tmp = 0
highest = 0
# Strips the newline character
for line in Lines:
    if line.strip() == '' :
        if tmp > highest :
            highest = tmp
        tmp = 0
    else :
        tmp += int(line.strip())

f.close

print(highest)