import random

feetinmile = 5280
metersinkilometers = 1000
beatles = ["Jhon Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]


def getfileext(filename):
    return filename[filename.index(",") + 1:]


def rolldice(num):
    return random.randint(1, num)  # randint > random integer