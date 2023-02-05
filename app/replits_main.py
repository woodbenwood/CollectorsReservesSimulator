"""
Click Run and enter your CL# to see what Reserves box/pack/case you're in
From the research done by VinKelsier (read this article):
https://snap.fan/guides/identifying-your-next-s4-card-location/
"""
from Fortuna import RandomValue
from app.drs_dict import dr_dict
from app.random_opening import roll_reserve, pick_a_box

if __name__ == '__main__':
    start = 1006
    # the collection level (CL1006) where reserves begin
    choice = input("Enter your Collection Level:")
    if choice == "Dr":
        CL = 3294
    elif choice == "random":
        print("a randomized opening of Reserves through Case 5:")
        CL = 3394
    else:
        CL = int(choice)
    box_count = 0
    pack_count = 1
    case_count = 0
    # start the counts at 0. A case is 10 "packs" of 4 "boxes" each
    # (a "box" is 12 CL's incl Boosters, Credits, and a Reserve)
    while start < CL + 1:
        # runs until it reaches your CL, then stops
        new_list = []
        # instantiate new list of boxes per loop
        pack_count += 1
        # keeps track of which pack we're counting
        box = pick_a_box()()
        # for the random option, this picks which Reserve the card appears in
        for i in [1, 2, 3, 4]:
            # every 4 Reserves from 1006:
            if choice == "Dr":
                if start in dr_dict.keys():
                    memory = start
                    new_list.append(dr_dict[start])
                    # print to the list of Reserves the card opened there
                else:
                    new_list.append(start)
                    # OR add the no. representing the Reserve to the list
                start += 12
                # a reserve (box) occurs every 12 CL
            elif choice == "random":
                if box == i:
                    memory = start
                    roll = roll_reserve()
                    new_list.append(roll())
                else:
                    new_list.append(start)
                start += 12
            else:
                new_list.append(start)
                # add the no. representing the Reserve to the list
                start += 12
                # a reserve (box) occurs every 12 CL
        if (start - 1054) % 480 == 0:
            # 1054 is very first CL of the second "pack" in case 1. [It makes the math work.]
            pack_count = 1
            # reset the pack count and start on the next case:
            case_count += 1
            print(f'   --------- Case {case_count} ---------   ')
        print(f"pack {pack_count}: ", new_list)
    if not str(new_list[0]).isnumeric():
        # this codeblock makes sure a card name (if any) is converted back into a number, for math:
        new_list.pop(0)
        new_list.insert(0, memory)
    box_count = ((CL - new_list[0]) // 12) + 1
    # your CL minus the no. of the first Reserve, with math to arrive at a 1-4
    if choice == "Dr":
        print(f"DrStrangePhD's Collection is on box {box_count} of pack {pack_count} in case {case_count}...")
        print("...having reached series 3 completion at CL 3262")
        print(f"(bought with tokens: Miles Morales, Cerebro, Jane Foster...\n"
              "...Mister Negative, Wave, Psylocke, Daredevil, Rogue)")
    elif choice == "random":
        print(f"This randomized account has also accumulated 8000 tokens.")
        print(f"Already acquired from Collectors Caches: {roll()} (feature under construction)")
    else:
        print(f"CL {CL} is box {box_count} of pack {pack_count} in case {case_count}")
