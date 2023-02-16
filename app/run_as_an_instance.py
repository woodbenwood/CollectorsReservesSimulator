from app.drs_dict import dr_CL
from app.functions import run_dr, run_random, run_basic
from app.run_as_a_class import Run

choice = input("Enter your Collection Level or 'random':")
run_as_an_instance = Run()

if choice == "Dr":
    cl = dr_CL
    run_dr()
elif choice == "random":
    run_random()
else:
    cl = int(choice)
    run_basic(1006, cl)