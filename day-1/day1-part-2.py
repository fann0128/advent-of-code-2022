f = open("input.txt", "r")
Lines = f.readlines()

tmp = 0
highest = []
# Strips the newline character
for line in Lines:
    if line.strip() == '' :
        highest.append(tmp)
        tmp = 0
    else :
        tmp += int(line.strip())

f.close

highest.sort()
print(sum(highest[-3:]))