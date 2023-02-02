"""
Click Run and enter your CL# to see what Reserves box/pack/case you're in
From the research done by VinKelsier (read this article):
https://snap.fan/guides/identifying-your-next-s4-card-location/
"""

from app.drs_dict import dr_dict

if __name__ == '__main__':
    start = 1006
    # the collection level (CL1006) where reserves begin
    choice = input("Enter your Collection Level:")
    if choice == "Dr":
        CL = 3086
    elif choice == "random":
        pass
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
        for _ in range(4):
            # every 4 Reserves from 1006:
            if choice == "Dr":
                if start in dr_dict.keys():
                    new_list.append(dr_dict[start])
                    # print to the list of Reserves the card opened there
                else:
                    new_list.append(start)
                    # OR add the no. representing the Reserve to the list
                start += 12
                # a reserve (box) occurs every 12 CL
            elif choice == "random":
                pass
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
    box_count = ((CL - new_list[0]) // 12) + 1
    # your CL minus the no. of the first Reserve, with math to arrive at a 1-4
    if choice == "Dr":
        print(f"Doc's Collection is on box {box_count} of pack {pack_count} in case {case_count}")
        print(f"Bought with tokens: Miles Morales, Cerebro, Jane Foster, \n"
              "Mister Negative, Wave, Psylocke, Daredevil, Rogue")
    elif choice == "random":
        pass
    else:
        print(f"Your Collection is on box {box_count} of pack {pack_count} in case {case_count}")
