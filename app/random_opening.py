import random
import re
from app.drs_dict import s5_set, s4_set, s3_set


def s5chance(percent=.25):
    return random.randrange(100) < percent


def s4chance(percent=2.5):
    return random.randrange(100) < percent


def roll_reserve():
    if s5chance():
        return random.choice(s5_set)
    elif s4chance():
        return random.choice(s4_set)
    else:
        return random.choice(s3_set)


if __name__ == '__main__':
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
    for i in range(100):
        rolling = roll_reserve()
        print(rolling)

