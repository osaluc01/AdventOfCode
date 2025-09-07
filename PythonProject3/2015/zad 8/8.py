import re
import ast
with open("/home/osaluc/PycharmProjects/PythonProject3/2015/zad 8/data") as f:
    text = f.readlines()
sum = 0

for line in text:
    a = line.strip()
    ast_str = ast.literal_eval(line)
    str_len = len(ast_str)
    sum += len(a) - str_len
    print(a)
    print(a.encode("unicode_escape").decode())


print(sum)