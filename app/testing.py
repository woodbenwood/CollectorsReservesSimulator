from app.drs_dict import dr_dict, dr_CL, s3_set, s4_set, s5_set
from app.random_4_replit import s4chance, s5chance, pick_a_pack, roll_cache, roll_reserve, pick_a_box, \
     cache_pull, s4_timer, timer_card
from app.functions import run_dr, run_random


start = 1006
# the collection level (CL1006) where reserves begin
box_count = 0
pack_count = 0
case_count = 0
# start the counts at 0. A case is 10 packs of 4 boxes each
# these terms from VinKelsier's article: https://snap.fan/guides/identifying-your-next-s4-card-location/
new_list = []
# honestly, this is just to appease PyCharm's linter. It kept warning later that this might be undefined...

choice = input("Enter your Collection Level or 'random':")
if choice == "Dr":
    cl = dr_CL
    run_dr()
elif choice == "random":
    cl = 3400
    run_random()
else:
    cl = int(choice)
    while start < cl + 1:
        # runs until it reaches your CL, then stops
        new_list = []
        # instantiate new list of boxes per loop
        pack_count += 1
        # keeps track of which pack we're counting
        if (start - 1006) % 480 == 0:
            # this math determines when a new case is starting
            pack = pick_a_pack()
            # this decides which pack in the case contains the Series 4 card.
            pack_count = 1
            # reset the pack count and start on the next case:
            case_count += 1
            print("\n", f'     --------- Case {case_count} ---------   ')
            # this print statement displays the case counts on the console
        for i in range(4):
            # every 4 Reserves from 1006:
            new_list.append(start)
            start += 12
        print(f"pack {pack_count}: ", new_list)
        # this print statement displays the pack counts on the console, with their box numbers bracketed
    box_count = ((cl - new_list[0]) // 12) + 1
    print(f"CL {cl} is box {box_count} of pack {pack_count} in case {case_count}")


# if __name__ == '__main__':
#     start = 1006
#     # the collection level (CL1006) where Reserves begin
#     choice = input("Enter your Collection Level, 'Dr', or 'random':")
#     if choice == "Dr":
#         CL = 3600
#     elif choice == "random":
#         print('\n')
#         print("A randomized opening of Reserves through Case 5:")
#         print("~ Series 4 cards (and s5, if any) in uppercase ~")
#         CL = 3394
#     else:
#         CL = int(choice)
#     box_count = 0
#     pack_count = 0
#     case_count = 0
#     # start the counts at 0. A case is 10 "packs" of 4 "boxes" each
#     # (a "box" is 12 CL's incl Boosters, Credits, and a Reserve)
#     while start < CL + 1:
#         # runs until it reaches your CL, then stops
#         new_list = []
#         # instantiate new list of boxes per loop
#         pack_count += 1
#         # keeps track of which pack we're counting
#         box = pick_a_box()()
#         # for the random option, this picks which Reserve the card appears in
#         if (start - 1006) % 480 == 0:
#             # this math determines when a new case is starting
#             pack = pick_a_pack()()
#             # this decides which pack in the case contains the Series 4 card.
#             pack_count = 1
#             # reset the pack count and start on the next case:
#             case_count += 1
#             print('\n', f'   --------- Case {case_count} ---------   ')
#             # this print statement displays the case counts on the console
#         for i in range(4):
#             # every 4 Reserves from 1006:
#             if choice == "Dr":
#                 if start in dr_dict.keys():
#                     memory = start
#                     new_list.append(dr_dict[start])
#                     # print to the list of Reserves the card opened there
#                 else:
#                     new_list.append(start)
#                     # OR add the no. representing the Reserve to the list
#                 start += 12
#                 # a reserve (box) occurs every 12 CL
#             elif choice == "random":
#                 if pack == pack_count:
#                     if box == i + 1:
#                         memory = start
#                         timer = timer_card()
#                         new_list.append(timer)
#                     else:
#                         new_list.append(start)
#                     # start += 12
#                 elif box == i + 1:
#                     memory = start
#                     roll = cache_pull()
#                     new_list.append(roll)
#                 else:
#                     new_list.append(start)
#                 start += 12
#             else:
#                 new_list.append(start)
#                 # add the no. representing the Reserve to the list
#                 start += 12
#                 # a reserve (box) occurs every 12 CL
#         print(f"pack {pack_count}: ", new_list)
#         # this print statement displays the pack counts on the console, with their box numbers bracketed
#     if not str(new_list[0]).isnumeric():
#         # this codeblock makes sure a card name (if any) is converted back into a number, for math:
#         new_list.pop(0)
#         new_list.insert(0, memory)
#     box_count = ((CL - new_list[0]) // 12) + 1
#     # your CL minus the no. of the first Reserve, with math to arrive at a 1-4
#     if choice == "Dr":
#         print(f"DrStrangePhD's Collection is on box {box_count} of pack {pack_count} in case {case_count}...")
#         print("...having reached series 3 completion at CL 3262")
#         print(f"(bought with tokens: Miles Morales, Cerebro, Jane Foster...\n"
#               "...Mister Negative, Wave, Psylocke, Daredevil, Rogue)")
#     elif choice == "random":
#         cache_pull_list = []
#         for _ in range(28):
#             cache_pull_list.append(cache_pull())
#         print('\n')
#         print("In 5 cases (and various rewards thus far), you've also acquired 8000 tokens. At 1000 apiece, "
#               "buying these remaining Series 3 cards would make you Series 3 complete:")
#         print(f"{sorted(s3_set)}")
#         print('\n')
#         print(f"Acquired prior from Collectors Caches: {sorted(cache_pull_list)}.")
#     else:
#         print(f"CL {CL} is box {box_count} of pack {pack_count} in case {case_count}")
