"""
    --- Day 5: Doesn't He Have Intern-Elves For This? ---
    Santa needs help figuring out which strings in his text file are naughty or nice.

    A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
    For example:

    ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
    aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
    jchzalrnumimnmhp is naughty because it has no double letter.
    haegwjzuvuyypxyu is naughty because it contains the string xy.
    dvszwmarrgswjxmb is naughty because it contains only one vowel.
    How many strings are nice?
"""
import re
with open("/home/osaluc/PycharmProjects/PythonProject3/2015/zad 5/data") as f:
    text = f.readlines()
#vowels = "aeiou".split()
nice_counter = 0
doubles = ["qq","ww","ee","rr","tt","yy","uu","ii","oo","pp","aa","ss","dd","ff","gg","hh","jj","kk","ll","zz","xx","cc","vv","bb","nn","mm"]
forbidden = ["ab", "cd", "pq", "xy"]
for line in text:
    print(len(line))
    vowels = list("aeiou")
    vow_count = 0
    for i in range(len(line)):
        if line[i] in vowels:
            vow_count += 1
    if vow_count >= 3:
        double_count = False
        for i in doubles:
            a = re.findall(i, line)
            if len(a) > 0:
                double_count = True
        if double_count:
            forbidden_count = 0
            for i in forbidden:
                b = re.findall(i, line)
                if len(b) > 0:
                    forbidden_count += 1
            if forbidden_count == 0:
                nice_counter += 1
                print("nice")

print(nice_counter)





