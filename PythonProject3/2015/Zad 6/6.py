import re
with open("/home/osaluc/PycharmProjects/PythonProject3/2015/Zad 6/data") as f:
    text = f.readlines()

line_num = 0 # numer linijki
grid = {} # siatka lampek
for x in range(0,1000): #uzupelniam slownik koordynatami od 0,0 do 999,999 i dopisuje do nich False
    for y in range(0,1000):
        grid[x, y] = False

for line in text: # pętla dla każdej linijki w pliku tekstowym
    line_num += 1
    print(line_num)
    input_type = 0 #domyślna wartość rodzaju operacji (3 możliwości)
    matches = re.findall(r"(\d+),(\d+) through (\d+),(\d+)", line)
    data = [int(x) for group in matches for x in group]

    # w zależności od instrukcji w linijce wybieram jedną z 3 operacji: włącz, wyłącz, przełącz światło
    if re.findall(r"turn on", line):
        input_type = 0
    elif re.findall(r"turn off", line):
        input_type = 1
    elif re.findall(r"toggle", line):
        input_type = 2

    #wykonuję operację i nadpisuję wartość w słowniku
    for y in range(data[0], data[2] + 1):
        for x in range(data[1], data[3] + 1):
            if input_type == 0: grid[x,y] = True
            elif input_type == 1: grid[x, y] = False
            elif input_type == 2: grid[x, y] = not grid[x,y]

print(sum(grid.values())) # drukuję sumę włączonych lampek