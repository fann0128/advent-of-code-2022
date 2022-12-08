f = open("input-1.txt", "r")
Lines = f.readlines()
my_map = []
# Strips the newline character
for line in Lines:
    my_map.append([int(char) for char in line.strip()])
f.close

width = len(my_map[0])
height = len(my_map)

number_of_visible = 0

for x in range(width):
    for y in range(height):
        # print(x, y)
        if x == 0 or y == 0 or x == width-1 or y == height-1 :
            number_of_visible += 1
        else :
            # make sure the number is the biggest at least in one direction
            current_tree = my_map[x][y]
            # left
            left = my_map[x][0:y]
            # right
            right = my_map[x][y+1:]
            # up
            up = []
            for distance_to_top in range (x):
                up.append(my_map[distance_to_top][y])
            # down
            down = []
            for distance_to_bottom in range (x+1,width):
                down.append(my_map[distance_to_bottom][y])

            if max(left) < current_tree or max(right) < current_tree or max(up) < current_tree or max(down) < current_tree :
                number_of_visible += 1

print(number_of_visible)