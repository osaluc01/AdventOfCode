with open('/home/osaluc/PycharmProjects/PythonProject3/2015/zad3/data') as f:
    text = f.read()

x, y = 0, 0
x1, y1 = 0,0
santa = {(x, y)}  # zbiór odwiedzonych domów, na start (0,0)
robot = {(x1, y1)}
switch = 0
for move in text:
    if switch == 0: #santa
        if move == "v":
            y -= 1
        elif move == "^":
            y += 1
        elif move == "<":
            x -= 1
        elif move == ">":
            x += 1
        santa.add((x, y))  # dodajemy nową pozycję jako tuple
        switch = 1
    elif switch == 1: #robot
        if move == "v":
            y1 -= 1
        elif move == "^":
            y1 += 1
        elif move == "<":
            x1 -= 1
        elif move == ">":
            x1 += 1
        robot.add((x1, y1))  # dodajemy nową pozycję jako tuple
        switch = 0

print("santa", len(santa))
print("robot", len(robot))
print("oczekiwana suma", len(santa) + len(robot))
counter = 0
for i in robot:
    if i in santa:
        counter += 1

    else:
        #print("nie ma")
        santa.add(i)

print("counter", counter)
print("rzeczywista suma", len(santa))

