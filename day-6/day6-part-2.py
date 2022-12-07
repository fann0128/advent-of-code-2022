f = open("input.txt", "r")
Lines = f.readlines()

# Strips the newline character
for line in Lines:
    input = [char for char in line.strip()]
    
    for i in range(len(input) - 14):
        my_set = {*input[i:i+14]}
        # print(input[i:i+4])
        if len(my_set) == 14 :
            print(i+14)
            break

f.close