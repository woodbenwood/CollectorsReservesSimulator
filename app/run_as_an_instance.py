from app.drs_dict import dr_dict, dr_CL, s3_set, s4_set, s5_set
from app.random_4_replit import s4chance, s5chance, pick_a_pack, roll_cache, roll_reserve, pick_a_box, \
     cache_pull, s4_timer, timer_card
from app.functions import run_dr, run_random, run_basic
from app.run_as_a_class import Run


choice = input("Enter your Collection Level or 'random':")
run_as_an_instance = Run()

if choice == "Dr":
    cl = dr_CL
    run_as_an_instance.run_dr()
elif choice == "random":
    run_random()
else:
    cl = int(choice)
    run_basic(1006, cl)