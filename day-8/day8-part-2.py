f = open("input-1.txt", "r")
Lines = f.readlines()
my_map = []
# Strips the newline character
for line in Lines:
    my_map.append([int(char) for char in line.strip()])
f.close

width = len(my_map[0])
height = len(my_map)

highest_score = 0

for x in range(width):
    for y in range(height):
        # print(x, y)
        if x != 0 and y != 0 and x != width-1 and y != height-1 :
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

            number_visible_tree_right = 0
            for i in range(len(right)):
                number_visible_tree_right += 1
                if current_tree <= right[i] :
                    break

            number_visible_tree_left = 0
            left = left[::-1]
            for i in range(len(left)):
                number_visible_tree_left += 1
                if current_tree <= left[i] :
                    break
            
            number_visible_tree_down = 0
            for i in range(len(down)):
                number_visible_tree_down += 1
                if current_tree <= down[i] :
                    break

            number_visible_tree_up = 0
            up = up[::-1]
            for i in range(len(up)):
                number_visible_tree_up += 1
                if current_tree <= up[i] :
                    break
            
            temp_score = number_visible_tree_right*number_visible_tree_left*number_visible_tree_up*number_visible_tree_down
            highest_score = highest_score if highest_score > temp_score else temp_score

print(highest_score)