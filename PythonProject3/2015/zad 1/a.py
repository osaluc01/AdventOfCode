with open("/home/osaluc/PycharmProjects/PythonProject3/2015/zad 1/data") as f:
    text = f.read()

floor = 0

for i in range(len(text)):
    if text[i] == '(':
        floor += 1
    elif text[i] == ')':
        floor -= 1

    if floor == -1:
        print(i + 1)