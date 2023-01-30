
if __name__ == '__main__':
    start = 1006
    # the collection level (CL1006) where reserves begin
    CL = int(input("Enter your Collection Level as an integer:"))
    box_count = 0
    pack_count = 1
    case_count = 0
    # start the counts at 0. A case is 10 "packs" of 4 "boxes" each
    # (a "box" is 12 CL's incl Boosters, Credits, and a Reserve)
    while start < CL + 1:
        # runs until it reaches your CL, then stops
        new_list = []
        # instantiate new list of boxes per loop
        box_count = 0
        # resets the box count going into the next pack
        pack_count += 1
        # keeps track of which pack we're counting
        for _ in range(4):
            # every 4 reserves from 1006:
            new_list.append(start)
            # add the no. representing the reserve to the list
            start += 12
            # a reserve (box) occurs every 12 CL
        if (start - 1054) % 480 == 0:
            # 1054 is very first CL of the second "pack" in case 1. [It makes the math work.]
            pack_count = 1
            # reset the pack count and start on the next case:
            case_count += 1
            print(f'Cracking open Case {case_count}:')
        print(f"pack {pack_count}: ", new_list)
    box_count = ((CL - new_list[0]) // 12) + 1
    print(f"Your Collection is on box {box_count} of pack {pack_count} in case {case_count}")

