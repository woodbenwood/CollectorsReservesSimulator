from app.drs_dict import dr_CL
from app.functions import run_dr, run_random, run_basic
# importing and instantiating the Run class isn't even necessary, can just run its class functions:

choice = input("Enter your Collection Level or 'random':")

if choice == "Dr":
    cl = dr_CL
    run_dr()
elif choice == "random":
    run_random()
else:
    cl = int(choice)
    run_basic(1006, cl)
