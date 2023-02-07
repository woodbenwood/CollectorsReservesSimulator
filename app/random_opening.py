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
    # elif s4chance():
    #     return RandomValue(s4_set)
    else:
        return RandomValue(s3_set)


# it wasn't perfectly accurate to roll the 2.5% odds each time. Marvel Snap presets it in a pack ala the timer below.


def cache_pull():
    pull = roll_reserve()()
    if pull in s3_set:
        s3_set.remove(pull)
    else:
        s5_set.remove(pull)
    return pull


def s4_timer():
    return RandomValue(s4_set)


def timer_card():
    rip = s4_timer()()
    s4_set.remove(rip)
    return rip


def pick_a_box():
    four_boxes = {1, 2, 3, 4}
    return RandomValue(four_boxes)


def pick_a_pack():
    ten_packs = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    return RandomValue(ten_packs)


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

