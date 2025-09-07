import re

grid = {}
for x in range(0,10):
    for y in range(0,10):
        grid[x, y] = False

input_type = 0
a = "toggle 6,5 through 9,6"

matches = re.findall(r"(\d+),(\d+) through (\d+),(\d+)", a)
data = [int(x) for group in matches for x in group]
print(data)

if re.findall(r"turn on", a):
    input_type = 0
elif re.findall(r"turn off", a):
    input_type = 1
    print("turn off")
elif re.findall(r"toggle", a):
    input_type = 2
    print("toggle")

for y in range(int(data[0]), int(data[2]) + 1):
    for x in range(int(data[1]), int(data[3]) + 1):
        if input_type == 0: grid[x,y] = True
        elif input_type == 1: grid[x, y] = False
        elif input_type == 2: grid[x, y] = not grid[x,y]


print(["  0    1    2    3    4    5    6    7    8    9"])
index_y = 0
for x in range(0,10):
    line = []
    for y in range(0,10):
        if grid[x,y] == True:
            line.append("X")
        if grid[x,y] == False:
            line.append(".")
    print(index_y, line)
    index_y += 1
