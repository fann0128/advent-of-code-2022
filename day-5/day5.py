f = open("input.txt", "r")
Lines = f.readlines()

initial = [
    ['M', 'J', 'C', 'B', 'F', 'R', 'L', 'H'],
    ['Z', 'C', 'D'],
    ['H', 'J', 'F', 'C', 'N', 'G', 'W'],
    ['P', 'J', 'D', 'M', 'T', 'S', 'B'],
    ['N', 'C', 'D', 'R', 'J'],
    ['W', 'L', 'D', 'Q', 'P', 'J', 'G', 'Z'],
    ['P', 'Z', 'T', 'F', 'R', 'H'],
    ['L', 'V', 'M', 'G'],
    ['C', 'B', 'G', 'P', 'F', 'Q', 'R', 'J']
    ]

# Strips the newline character
for line in Lines:
    # move 3 from 2 to 1
    number_to_move, temp = line.strip().split(' from ')
    number_to_move = int(number_to_move.split('move ')[1])
    from_index, to_index = temp.split(' to ')
    from_index = int(from_index) - 1
    to_index = int(to_index) - 1

    for x in range(number_to_move) :
        initial[to_index].append(initial[from_index].pop())

f.close

print(initial)