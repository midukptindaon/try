x = 9
a = bool(x ** 2 for x in range(8) if not x % 2)
print(a)


e = [e for e in range(2)]
num = []
for i in e:
    num.append(i)
print(sum(num))


def x(word):
    translation = ""
    for y in word:
        if y in "aiueo":
            translation = translation + y + "g" + y
        else:
            translation = translation + y
    return translation


print(x("unstoppable"))

reading = False
try:
    access = open("../practice2/main2.py", "r")
    print(access.readable())
    data = access.readlines()
    access.close()
    for reading in data:
        if reading is True:
            print(reading)
except IOError:
    print("no good syntax")

access = open("../practice2/main2.py", "r")
print(access.readable())
data = access.readlines()
access.close()

for reading in data:
    if reading is True:
        print(reading)

decimal = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
hexa = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        "A", "B", "C", "D", "E", "F")
hexarange = [hexarange for hexarange in hexa]
hexvalue = [3]
for value in hexvalue:
    if hexvalue[0]:
        16 ** decimal[0]
    hexvalue[1] = 16**decimal[1]
    hexvalue[2] = 16**decimal[2]
    hexvalue[3] = 16**decimal[3]
    hexvalue[4] = 16**decimal[4]
    hexvalue[5] = 16**decimal[5]
    hexvalue[6] = 16**decimal[6]
    hexvalue[7] = 16**decimal[7]
    hexvalue[8] = 16**decimal[8]
    hexvalue[9] = 16**decimal[9]
    hexvalue[10] = 16**decimal[10]
    hexvalue[11] = 16**decimal[11]
    hexvalue[12] = 16**decimal[12]
    hexvalue[13] = 16**decimal[13]
    hexvalue[14] = 16**decimal[14]
    hexvalue[15] = 16**decimal[15]
    hexvalue[16] = 16**decimal[16]