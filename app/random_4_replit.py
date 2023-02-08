from random import random, choice
from drs_dict import s5_set, s4_set, s3_set


def s5chance(percent=.0111):
    return random() <= percent


def s4chance(percent=.025):
    return random() <= percent


def twenty_five_percent_chance(percent=.25):
    # only really needed this one for sanity-checking
    return random() <= percent


def pick_a_box():
    four_boxes = [1, 2, 3, 4]
    return choice(four_boxes)


def pick_a_pack():
    ten_packs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return choice(ten_packs)


def roll_cache():
    return choice(s3_set)


def cache_pull():
    pull = roll_cache()
    if pull in s3_set:
        s3_set.remove(pull)
    # elif pull in s4_set:
    #     s4_set.remove(pull)
    # this code is dead, see note above in def roll_reserve
    else:
        s5_set.remove(pull)
    return pull
    # this s5 "else" is redundant code: atm not possible to roll an s5


def roll_reserve():
    if s5chance():
        return choice(s5_set)
    # elif s4chance():
    #     return choice(s4_set)
    else:
        return choice(s3_set)
    # it wasn't perfectly accurate to roll the 2.5% odds each time. Marvel Snap bakes it in to a specific pack, ala:


def s4_timer():
    return choice(s4_set)


def timer_card():
    rip = s4_timer()
    s4_set.remove(rip)
    return rip


if __name__ == '__main__':
    print("\n")
    print("10 random s3's with a 1.11% chance each of being s5's:")
    print("\n")
    for i in range(10):
        rolling = roll_reserve()
        print(rolling)

    print("\n")
    print("Number of s5's rolled randomly in 100K rolls (1.11%):")
    count = 0
    for i in range(100000):
        roll_s5 = s5chance()
        if roll_s5:
            count += 1
    print(f"{count}")

    print("\n")
    print("Number of s4's rolled randomly in 100K rolls (2.5%):")
    count = 0
    for i in range(100000):
        roll_s4 = s4chance()
        if roll_s4:
            count += 1
    print(f"{count}")
