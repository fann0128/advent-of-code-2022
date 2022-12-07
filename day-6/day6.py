f = open("input.txt", "r")
Lines = f.readlines()

# Strips the newline character
for line in Lines:
    input = [char for char in line.strip()]
    
    for i in range(len(input) - 4):
        my_set = {input[i], input[i+1], input[i+2], input[i+3]}
        if len(my_set) == 4 :
            print(i+4)
            break

f.close

# print(initial)