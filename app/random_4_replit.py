from random import random, choice
from drs_dict import s3_set, s4_set, s5_set


def s5chance(percent=.0025):
    return random() <= percent


def s4chance(percent=.025):
    return random() <= percent


def twenty_five_percent_chance(percent=.25):
    # only really needed this one for sanity-checking
    return random() <= percent


def roll_reserve():
    if s5chance():
        return choice(s5_set)
    elif s4chance():
        return choice(s4_set)
    else:
        return choice(s3_set)


def pick_a_pack():
    ten_packs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return choice(ten_packs)


if __name__ == '__main__':
    for i in range(10):
        rolling = roll_reserve()
        print(rolling())

    # print('s5\'s:')
    # count = 0
    # for _ in range(100000):
    #     roll_s5 = s5chance()
    #     if roll_s5:
    #         count += 1
    # print(count)
    #
    # count = 0
    # print('s4\'s:')
    # for _ in range(100000):
    #     roll_s4 = s4chance()
    #     if roll_s4:
    #         count += 1
    # print(count)
    #
    # count = 0
    # print('25\'s:')
    # for _ in range(100000):
    #     roll_25 = twenty_five_percent_chance()
    #     if roll_25:
    #         count += 1
    # print(count)