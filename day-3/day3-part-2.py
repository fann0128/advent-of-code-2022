f = open("input.txt", "r")
Lines = f.readlines()

letter_map = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25,
    'z':26,
    'A':27,
    'B':28,
    'C':29,
    'D':30,
    'E':31,
    'F':32,
    'G':33,
    'H':34,
    'I':35,
    'J':36,
    'K':37,
    'L':38,
    'M':39,
    'N':40,
    'O':41,
    'P':42,
    'Q':43,
    'R':44,
    'S':45,
    'T':46,
    'U':47,
    'V':48,
    'W':49,
    'X':50,
    'Y':51,
    'Z':52
}
# Strips the newline character
score = 0
tmp = []
for line in Lines:
    tmp.append(line.strip())
    if len(tmp) == 3 :
        string1 = [char for char in tmp[0]]
        string2 = [char for char in tmp[1]]
        string3 = [char for char in tmp[2]]
        repeat = set(string1) & set(string2) & set(string3)
        score += letter_map[next(iter(repeat))]
        tmp = []

f.close

print(score)