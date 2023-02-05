# import random
from app.drs_dict import s5_set, s4_set, s3_set
from Fortuna import RandomValue, percent_true


def s5chance():
    return percent_true(.25)


def s4chance():
    return percent_true(2.5)


def roll_reserve():
    if s5chance():
        return RandomValue(s5_set)
    elif s4chance():
        return RandomValue(s4_set)
    else:
        return RandomValue(s3_set)


# as written in random library:
# def s5chance(percent=.25):
#     return random.randrange(100) < percent
#
#
# def s4chance(percent=2.5):
#     return random.randrange(100) < percent


def pick_a_box():
    four_boxes = {1, 2, 3, 4}
    return RandomValue(four_boxes)


if __name__ == '__main__':
    for i in range(10):
        rolling = roll_reserve()
        print(rolling())

    count = 0
    for i in range(100000):
        roll_s5 = s5chance()
        if roll_s5:
            count += 1
    print(f"Total s5's: {count}")

    count = 0
    for i in range(100000):
        roll_s4 = s4chance()
        if roll_s4:
            count += 1
    print(f"Total s4's: {count}")

