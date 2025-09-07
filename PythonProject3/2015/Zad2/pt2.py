import re
f = open("/home/osaluc/PycharmProjects/PythonProject3/2015/Zad2/data", "r")
lines = f.readlines()

total = 0
for line in lines:
    dims = re.findall(r"(\d+)x(\d+)x(\d+)", line)
    l,w,h = int(dims[0][0]),int(dims[0][1]),int(dims[0][2])

    l1 = [l,w,h]
    c2 = l * w * h
    l1.remove(max(l1))

    total += l1[0] * 2 + l1[1] * 2 + c2

print(total)