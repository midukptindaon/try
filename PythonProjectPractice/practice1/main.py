from math import *
from Chef import Chef
from Student import Student
from Question import Question
from ChinesseChef import ChinesseChef
import usefultools
print("1.__SETUP AND HELLO WORLD__")

print("Hello World")

print("2.__DRAWING AND SHAPE__")

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

print("3.__VARIABLE AND DATA TYPES__")

character_name = "Masha"
character_age = "5"
character_man_gender = "girl"
print("There once was a " + character_man_gender + " named " + character_name + ", ")
print("she was " + character_age + " years old. ")
print("She really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")

print("4.__WORKING WITH STRING__")

print("Bear Academy")
print("Bear\nAcademy")
print("Bear\"Academy")
phrase = "Bear Academy"
print(phrase + " is cool.")
print(phrase.upper())
print(phrase.lower())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print("Note: len stands for (length) of the function by index")
print(phrase[0])
print(phrase[1])
print(phrase[2])
print(phrase.index("B"))
print(phrase.index("y"))
print(phrase.index("Academy"))
print(phrase.replace("Bear", "Bunny"))
print(phrase.replace("Bear", "Wolf"))

print("5.__GETTING INPUT FROM USER__")

print("Note: to get some information from user is just type (input) statement")
print("Note: e.g. input(object)")

print("6.__WORKING WITH NUMBERS (THESE DATAS CLASSED BY 'FROM MATH IMPORT *' STATEMENTS ON THE FILE'S TOP__ ")


print(2)
print(2.136)
print(-2.454)
print(3+5-2)
print(4*2+3)
print(1347 % 372)
print(7 % 2)
print(4/2)
my_num = -3
print(str(my_num) + " is My Favorite Number")
print(pow(3, 3))
print(pow(3, 2) + (pow(2, 2)) + 5)
print(abs(my_num))
print("Note: abs stands for absolute")
print(max(4, 1))
print(min(6, 4))
print(round(4.1))
print(round(4.8))
print(floor(3.7))
print(ceil(3.7))
print(sqrt(81))
print("Note: int statement stands for integer number")

print("7.__UNTITLED__")

print("roses are red")
print("Violet is blue ")
print("I love U")

print("8.__LIST__")

fellowship = ["Masha", "Bear", "Bunny", "Hedgehog", "Squirrel", "Pig", "Goat"]
numbers = [34, 15, 38, 86, 83, 273, 732, 82]
print(fellowship[0])
print(fellowship[1])
print(fellowship[2])
print(fellowship[-1])
print(fellowship[-2])
print(fellowship[0:4])
print(fellowship[1:-2])
fellowship[0] = "Alien"
print(fellowship[0])
fellowship.extend(numbers)
print(fellowship)
fellowship.append(numbers)
print(fellowship)
fellowship.remove("Alien")
print(fellowship)
fellowship.insert(0, "Naruto")
print(fellowship)
fellowship.remove(numbers)
fellowship.remove("Naruto")
fellowship.insert(0, "Masha")
print(fellowship)
fellowship.remove(34)
print(fellowship)
fellowship.remove(15)
fellowship.remove(38)
fellowship.remove(86)
fellowship.remove(83)
fellowship.remove(273)
fellowship.remove(732)
fellowship.remove(82)
print(fellowship)
fellowship.pop(2)
print(fellowship)
fellowship.pop()
print(fellowship)
fellowship.insert(2, "Bunny")
fellowship.insert(2, "Bunny")
print(fellowship)
print(fellowship.count("Bunny"))
fellowship.remove("Bunny")
print(fellowship)
fellowship.sort()
print(fellowship)

print("9.__LIST FUNCTION__")

Numbers = [1, 0, 3, 8, 5, 9, 2, 7, 4, 6]
Numbers.sort()
print(Numbers)
fellowship.reverse()
print(fellowship)
fellowship.copy()
fellowship2 = fellowship.copy()
print(fellowship2)

print("10.__TUPLES__")

coordinates = (4, 5)
print(coordinates[0])
print(coordinates[1])
print("Note: tuple can be neither changed, nor removed, erased, copied, etc.")
coordinates = [(4, 5), (9, 2), (5, 7)]
print(coordinates[0])

print("11.__FUNCTION__")


def sayhi(name, character, age):
    print("Hello " + name)
    print(" , you are " + character + " and only " + str(age) + "-year-old.")


sayhi("Masha", "Naughty", 7)
print("Note: Masha, Naughty, 7 are as a parameter.")
print("Note: parameter is the information that we need to give to the function/s")
print("Note: def is used for all the code after (sayhi) will be inside the function. other than that, ")
print("Note: def is only execute the (spesific) function task that we want to execute")

print("12.__RETURN STATEMENT__")


def cube(value):
    return value*value*value


print(cube(3))
print("Note: return is about to to execute the function of what we name it as the value,otherwise it results none")

print("13.__IF STATEMENT__")

is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a Male or tall")
elif is_male and not is_tall:
    print("you are a short male")
elif not is_male and is_tall:
    print("you are not male but tall")
else:
    print("You are neither male, nor tall")

print("Note: True and False statement is about to determine the condition either be true or false")
print("Note: elif stands for (else-if)")
print("Note: else statement has the same meaning for otherwise")
print("Note: you could replace the (or) statement to be (and) with a bit difference")

print("14.__IF STATEMENT AND COMPARISON__")


def maxnum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(maxnum(10, 20, 30))
print("Note: other addition statements are like (!=) means not equal to, (==), (<=), etc. ")

print("15.__BUILDING A BETTER CALCULATOR__")

number1 = 5
op = "*"
number2 = 6

if op == "+":
    print(number1 + number2)
elif op == "-":
    print(number1 - number2)
elif op == "/":
    print(number1 / number2)
elif op == "*":
    print(number1 * number2)
else:
    print("Error")

print("Note: (op) means operator")
print("Note: float means to convert the function")

print("16.__DICTIONARIES__")

dayConversion = {
    "Sun": "Sunday",
    "Mon": "Monday",
    "Tues": "Tuesday",
    "Wed": "Wednesday",
    "Thu": "Thursday",
    "Fri": "Friday",
    "Sat": "Saturday"
}
print(dayConversion["Sun"])
print(dayConversion.get("Mon"))
print(dayConversion.get("nuv"))
print(dayConversion.get("nuv", "Not a valid key"))

print("Note: (get) fuction is subtly different with square parenthesis([])")
print("Note: (get) statement can spesify a specific default value if some value is not found")

print("17.__WHILE LOOP__")

i = 1
while i <= 10:
    print(i)
    i += 2

print("End With While Loop")

print("18.__BUILDING A GUESSING GAME__")

secretword = "Masha"
userguess = ""
userguesscount = 0
userguesslimit = 0
outofguess = False

while userguess != secretword and not outofguess:
    if userguesscount < userguesslimit:
        userguesscount += 1
        userguess = input("Enter the guess!")
    else:
        outofguess = True
        print("You lose!")

if not outofguess:
    print("You Win")

print("19.__FOR LOOP__")

for letter in "Bear Academy":
    print(letter)

for index in range(10):
    print(index)

friends = ["Masha", "Bear", "Squirrel"]

for index in friends:
    print(index)

for index in range(len(friends)):
    print(index)

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not First")

print("20.__EXPONENT FUNCTION__")


def raise_to_pow(basenum, pownum):
    realbasenum = 1
    for indexes in range(pownum):
        realbasenum = realbasenum * basenum
    return realbasenum


print(raise_to_pow(2, 3))
print("Note: because the user doesn't decide the value of pownum still, that is the way why - ")
print("we consider the (value) = 1")

print("21.__2D LISTS AND NESTED LOOPS__")

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for B in A:
    for C in B:
        print(C)

print("22.__BUILD A TRANSLATOR__")


def translate(word):
    translation = ""
    for letters in word:
        if letters in "AEIUOaeiuo":
            translation = translation + "g"
        else:
            translation = translation + letters
    return translation


print(translate("Masha"))

print("23.__COMMENT__")

print("we can comment in the python programme without python execute the object out")
'''
1st.e.g. shfuvobaganergbe
    hgenbgaeonbe
'''
# 2nd.e.g.jahfngjnqasjkhRbgiebgub

print("24.__TRY EXCEPT__")

# number = int(input("Enter the number!"))
# print(number)
# this programme will cause error, to test our programme which can be possibly error we -
# can find it out with using TRY and EXCEPT
# try:
#     number = int(input("Enter the number!"))
#     print(number)
# except ValueError:
#     print("invalid value")
# try:
#     answer = 9 / 0    # 9 / 0 isn't possible which causes  error programme
#     number = int(input("Enter the number"))
#     print(number)
# except ZeroDivisionError:
#     print("zero division")
# except ValueError:
#     print("invalid value")

print("25.__READING FILES__")

myfile = open("myfile.txt", "r")  # r = read, w = write, a = append, r+ = read and write
print(myfile.readable())
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
print(myfile.read(3))
print(myfile.readlines())
print(myfile.readlines())
# or we can use the statement of: for friends in myfile.readlines():
#                                 print(friends)
myfile.close()

print("26.__WRITING FILES__")

myfile = open("MashaFamilyMEmbers", "w")
myfile.write("\npig = 7")
myfile.write("<p>This is HTML</p>")
# when using "a", \n is needed, otherwise the appended line will be appended next to the last-existing-line.
# using "w" is just basically will override our previous texts in myfile.txt
# another thing about "w" is if we edit/change the title in open statement as like myfile1.txt -
# will render new file in python.
myfile.close()

print("27.__MODULES AND PIP__")

print(usefultools.rolldice(6))  # import useful tools is at the top of file

print("28.__CLASSES AND OBJECTS__")

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)

print(student1.is_on_probation, student1.gpa)
print(student2.is_on_probation)

print("29.__BUILDING A MULTIPLE CHOICE QUIZ__")

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = question.prompt  # with input()
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")


run_test(questions)

print("30.__OBJECT FUNCTIONS__")

student3 = Student("Oscar", "Accounting", 3.1, True)
student4 = Student("Phyllis", "Business", 3.8, True)

print(student3.on_honor_roll())
print(student4.on_honor_roll())
print(student3.name)

print("31.__INHERITANCE__")

my_Chef = Chef()
my_Chef.make_special_dish()

my_CinesseChef = ChinesseChef()
my_CinesseChef.make_special_dish()

print("32.__PYTHON INTERPETER__")


# %s means substitute
# %d indicates the integer should be substitute
fuckingchef = open("../practice1/Chef.py", "r")
print(fuckingchef.readable())
print(fuckingchef.readlines())
print(len(fuckingchef.readlines()))
fuckingchef.close()
r = range(10)
