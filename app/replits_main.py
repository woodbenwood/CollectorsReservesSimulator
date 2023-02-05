"""
Click Run and enter your CL# to see what Reserves box/pack/case you're in
From the research done by VinKelsier (read this article):
https://snap.fan/guides/identifying-your-next-s4-card-location/
"""

from app.drs_dict import dr_dict, s3_set, s4_set, s5_set
from app.random_opening import roll_reserve, pick_a_box


# DEFINE A FUNCTION TO PICK A PACK in the case TO CONTAIN AN S4 CARD (just under case count below)


def cache_pull():
    pull = roll_reserve()()
    if pull in s3_set:
        s3_set.remove(pull)
    elif pull in s4_set:
        s4_set.remove(pull)
    else:
        s5_set.remove(pull)
    return pull


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
                    roll = cache_pull()
                    new_list.append(roll)
                    # needs a pity timer function to award an s4 in pack 10 of each case if not already pulled
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
            # DEFINE A FUNCTION TO PICK A PACK in the case TO CONTAIN AN S4 CARD
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
        cache_pull_list = []
        for _ in range(28):
            cache_pull_list.append(cache_pull())
        print(f"Already acquired from Collectors Caches: {sorted(cache_pull_list)}.")
        print(f"In 5 cases, you've also acquired 5000 tokens. At 1000 apiece, buying these remaining Series 3 cards "
              f"would make you Series 3 complete: {sorted(s3_set)}.")
    else:
        print(f"CL {CL} is box {box_count} of pack {pack_count} in case {case_count}")
