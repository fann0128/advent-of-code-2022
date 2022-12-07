f = open("input-1.txt", "r")
Lines = f.readlines()

my_folder = {}
my_cursor = ''

def find_second_last(text, pattern):
    return text.rfind(pattern, 0, text.rfind(pattern))
# Strips the newline character
for line in Lines:
    if line.strip()[:1] == '$' :
        # cd or ls
        if line.strip()[:5] == '$ cd ' and line.strip()[5:] != '..' :
            my_cursor += line.strip()[5:]+'/' if line.strip()[5:] != '/' else '/'
        elif line.strip()[:5] == '$ cd ' and line.strip()[5:] == '..' :
            my_cursor = my_cursor[:find_second_last(my_cursor, '/')+1]
    else :
        if line.strip()[:3] != 'dir' :
            file_size, file_name = line.strip().split(' ')
            my_folder[my_cursor+file_name] = int(file_size)

my_folder_size = {}
my_cursor = ''
for line in Lines:
    if line.strip()[:1] == '$' :
        # cd or ls
        if line.strip()[:5] == '$ cd ' and line.strip()[5:] != '..' :
            my_cursor += line.strip()[5:]+'/' if line.strip()[5:] != '/' else '/'
        elif line.strip()[:5] == '$ cd ' and line.strip()[5:] == '..' :
            my_cursor = my_cursor[:find_second_last(my_cursor, '/')+1]
        
        my_folder_size[my_cursor] = 0

        for key in my_folder.keys() :
            if key.startswith(my_cursor) :
                my_folder_size[my_cursor] += my_folder[key]

f.close

print(sum([x for x in my_folder_size.values() if x <= 100000]))