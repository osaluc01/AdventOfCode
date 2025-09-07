import re
with open("/home/osaluc/PycharmProjects/PythonProject3/2016/zad 1/data") as f:
    text = f.read()
text = text.split(",")
cache = {(0,0)}
coords = [0,0] # LEWY DOLNY RÓG. NORTH TO +, EAST TO +
directions = ["North", "East", "South", "West"]
dir_index = 0 # Startowo patrzymy na północ
check_again = True

for command in text:
    if check_again:
        command = command.strip()
        if command[0] == "L":
            dir_index -= 1
        elif command[0] == "R":
            dir_index += 1

        if dir_index == 4:  # poruszamy się w zakresie index direction, czyli od 0 do 3.
            dir_index = 0
        elif dir_index == -1:
            dir_index = 3

        steps = re.findall(r"(\d+)", command)
        print(steps[0])
        for x in range(1, int(steps[0]) + 1):
            if check_again:
                if (coords[0], coords[1]) in cache and (coords[0], coords[1]) != (0,0):
                    print("bingo")
                    location = [coords[0], coords[1]]
                    print("location",location)
                    print(abs(location[0]) + abs(location[1]))
                    check_again =False
                else:
                    cache.add((coords[0], coords[1]))
                    #print(cache)
                    if dir_index == 0:
                        coords[1] += 1
                    elif dir_index == 1:
                        coords[0] += 1
                    elif dir_index == 2:
                        coords[1] -= 1
                    elif dir_index == 3:
                        coords[0] -= 1
                    print("coords",coords, x)









