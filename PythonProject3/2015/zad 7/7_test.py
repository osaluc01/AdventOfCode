import re
with open("/home/osaluc/PycharmProjects/PythonProject3/2015/zad 7/data") as f:
    text = f.readlines()

dic = {}
new_dic = {}
memo = {}

def evaluate(wire):
    if wire in memo:
        return memo[wire]
    else:
        for key, value in dic.items():
            if value.strip() == wire.strip():
                key = key.strip()
                if key.isdigit():
                    result = int(key) & 0xFFFF
                    memo[wire] = result
                    return result
                elif "&" in key:
                    left,op,right = key.split()
                    result = (evaluate(left) & evaluate(right)) & 0xFFFF
                    memo[wire] = result
                    return result
                elif "~" in key:
                    op, right = key.split()
                    result = ~evaluate(right) & 0xFFFF
                    memo[wire] = result
                    return result
                elif "|" in key:
                    left, op, right = key.split()
                    result = (evaluate(left) | evaluate(right)) & 0xFFFF
                    memo[wire] = result
                    return result
                elif "<<" in key:
                    left, op, right = key.split()
                    result = (evaluate(left) << int(right)) & 0xFFFF
                    memo[wire] = result
                    return result
                elif ">>" in key:
                    left, op, right = key.split()
                    result = (evaluate(left) >> int(right)) & 0xFFFF
                    memo[wire] = result
                    return result



for line in text:
    line = line.strip()
    left, right = line.split("->")
    dic[left] = right.strip()

for key, value in dic.items():
    new_key= key.strip().replace("AND", "&").replace("OR", "|").replace("LSHIFT", "<<").replace("RSHIFT", ">>").replace("NOT", "~")
    new_dic[new_key] = value

dic = new_dic

for key, val in dic.items():
    print(evaluate(val))


