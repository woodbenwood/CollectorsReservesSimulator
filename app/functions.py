from drs_dict import dr_CL, dr_dict, s3_set
from app.random_4_replit import s4chance, s5chance, pick_a_pack, roll_cache, roll_reserve, pick_a_box, \
     cache_pull, s4_timer, timer_card


def run_dr(start=1006):
    cl = dr_CL
    pack_count = 0
    case_count = 0
    # start the relevant counts at 0
    new_list = []
    memory = None
    # redundant assignments to appease linter
    while start < cl + 1:
        # runs until it reaches your CL, then stops
        new_list = []
        # instantiate new list of boxes per loop
        pack_count += 1
        # keeps track of which pack we're counting
        if (start - 1006) % 480 == 0:
            # this math determines when a new case is starting
            pack_count = 1
            # reset the pack count and start on the next case:
            case_count += 1
            print("\n", f'     --------- Case {case_count} ---------   ')
            # this print statement displays the case counts on the console
        for i in range(4):
            # every 4 Reserves from 1006:
            if start in dr_dict.keys():
                memory = start
                new_list.append(dr_dict[start])
                # print to the list of Reserves the card opened there
            else:
                new_list.append(start)
                # OR add the no. representing the Reserve to the list
            start += 12
            # a reserve (box) occurs every 12 CL
        print(f"pack {pack_count}: ", new_list)
        #         # this print statement displays the pack counts on the console, with their box numbers bracketed
    if not str(new_list[0]).isnumeric():
        # this codeblock makes sure a card name (if any) is converted back into a number, for math:
        new_list.pop(0)
        new_list.insert(0, memory)
    box_count = ((cl - new_list[0]) // 12) + 1
    # your CL minus the no. of the first Reserve, with math to arrive at a 1-4
    print("\n")
    print(f"DrStrangePhD's Collection is on box {box_count} of pack {pack_count} in case {case_count} "
          f"having reached series 3 completion at CL 3262.")
    print(f"(bought with tokens: Miles Morales, Cerebro, Jane Foster, "
          f"Mister Negative, Wave, Psylocke, Daredevil, Rogue, SHURI)")


def run_random(start=1006):
    cl = 3400
    # this Collection Level will output 5 cases
    box_count = 0
    pack_count = 0
    case_count = 0
    # start the counts at 0
    new_list = []
    memory = None
    pack = None
    # redundant assignments to appease linter
    print("\n")
    print(f"Acquired prior from Collector's Caches (486-994):")
    for _ in range(4):
        cache_pull_list = []
        for _ in range(7):
            cache_pull_list.append(cache_pull())
        print(cache_pull_list)
    print("\n")
    print("A randomized opening of Reserves through Case 5:")
    print("(Series 4 cards (and s5, if any) in uppercase)")
    while start < cl + 1:
        # runs until it reaches your CL, then stops
        new_list = []
        # instantiate new list of boxes per loop
        pack_count += 1
        # keeps track of which pack we're counting
        box = pick_a_box()
        # for the random option, this picks which Reserve the card appears in
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
            if pack == pack_count and box == i + 1:
                memory = start
                timer = timer_card()
                new_list.append(timer)
            elif box == i + 1:
                memory = start
                roll = cache_pull()
                new_list.append(roll)
            else:
                new_list.append(start)
            start += 12
        print(f"pack {pack_count}: ", new_list)
        # this print statement displays the pack counts on the console, with their box numbers bracketed
    if not str(new_list[0]).isnumeric():
        # this codeblock makes sure a card name (if any) is converted back into a number, for math:
        new_list.pop(0)
        new_list.insert(0, memory)
    print("\n")
    print(f"In 5 cases (and various rewards before & during), approximately 8000 tokens are acquired.")
    print('\n')
    print("These remaining Series 3 cards (at 1000 tokens each) "
          "gets this Collection to Series 3 completion:")
    print("\n")
    print(f"{sorted(s3_set)}")
