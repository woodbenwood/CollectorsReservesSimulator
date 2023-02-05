from random import random


def s5chance(percent=.0025):
    return random() <= percent


def s4chance(percent=.025):
    return random() <= percent


def twenty_five_percent_chance(percent=.25):
    # only really needed this one for sanity-checking
    return random() <= percent


if __name__ == '__main__':
    print('s5\'s:')
    count = 0
    for _ in range(100000):
        roll_s5 = s5chance()
        if roll_s5:
            count += 1
    print(count)

    count = 0
    print('s4\'s:')
    for _ in range(100000):
        roll_s4 = s4chance()
        if roll_s4:
            count += 1
    print(count)

    count = 0
    print('25\'s:')
    for _ in range(100000):
        roll_25 = twenty_five_percent_chance()
        if roll_25:
            count += 1
    print(count)