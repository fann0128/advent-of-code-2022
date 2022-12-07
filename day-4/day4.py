f = open("input.txt", "r")
Lines = f.readlines()

# Strips the newline character
number_of_overlapped = 0
for line in Lines:
    first,last = line.strip().split(',')
    first_start, first_end = first.split('-')
    last_start, last_end = last.split('-')

    if int(first_start) <= int(last_start) and int(first_end) >= int(last_end) :
        number_of_overlapped +=1
    elif int(last_start) <= int(first_start) and int(last_end) >= int(first_end) :
        number_of_overlapped +=1
f.close

print(number_of_overlapped)