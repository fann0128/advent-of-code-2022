f = open("input.txt", "r")
Lines = f.readlines()

# Strips the newline character
number_of_overlapped = 0
for line in Lines:
    first,last = line.strip().split(',')
    first_start, first_end = first.split('-')
    last_start, last_end = last.split('-')

    task_1 = [*range(int(first_start),int(first_end)+1)] if int(first_start) != int(first_end) else [int(first_start)]
    task_2 = [*range(int(last_start),int(last_end)+1)] if int(last_start) != int(last_end) else [int(last_start)]

    repeat = set(task_1) & set(task_2)
    if len(repeat) :
        number_of_overlapped += 1
f.close

print(number_of_overlapped)