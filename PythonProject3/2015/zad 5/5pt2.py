import re
with open("/home/osaluc/PycharmProjects/PythonProject3/2015/zad 5/data") as f:
    text = f.readlines()

    alphabet = "abcdefghijklmnopqrstuwvxyz"
    #doubles = False
    nice_counter = 0
    line_num = 0
    for line in text:
        line_num += 1
        end = False

        while not end:
            for x in alphabet:
                for y in alphabet:
                    #doubles = False
                    b = re.findall((x + y), line)
                    if len(b) >= 2:
                        for a in alphabet:
                            c = re.findall(rf"{a}.{a}", line)
                            if len(c) >= 1:
                                nice_counter += 1
                                print("linijka", line_num, c, b, line)
                                end = True
                                break
                    if end:
                        break
                if end:
                    break

            end = True

print(nice_counter)
