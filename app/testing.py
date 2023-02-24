from app.drs_dict import dr_dict, dr_CL, s3_set, s4_set, s5_set
from app.random_4_replit import s4chance, s5chance, pick_a_pack, roll_cache, roll_reserve, pick_a_box, \
     cache_pull, s4_timer, timer_card
from app.functions import run_dr, run_random, run_basic
from app.run_as_a_class import Run
from Fortuna import percent_true


def currency_box():
    credits_300 = 0
    credits_400 = 0
    gold_200 = 0
    roll_currency = percent_true()
    if roll_currency <= 40:
        credits_300 += 1
        return "300 Credits"
    elif 40 < roll_currency <= 60:
        credits_400 += 1
        return "400 Credits"
    else:
        gold_200 += 1
        return "200 Gold"


# using this file as a quick calculator
if __name__ == '__main__':
    credits_300 = 0
    credits_400 = 0
    gold_200 = 0
    # credits_per_box = 50
    credits_per_pack = currency_box()
    for _ in range(100):
        credits_per_pack
    print(f"300 Credits: {credits_300}",
          f"400 Credits: {credits_400}",
          f"200 Gold: {gold_200}")
