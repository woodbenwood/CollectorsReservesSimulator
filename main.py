# just literally wanted to do the math on Marvel Snap's Collectors Reserves,
# to know which 'pack' of 4 reserves/boxes I'm currently in...

if __name__ == '__main__':
    start = 1006
    # the collection level (CL1006) where reserves begin
    casecount = 0
    # a case is 10 "packs" of 4 "boxes" each (a "box" is 12 CL's with 1 Reserve)
    while start < 2591:
        # my collection is currently CL 2590
        newlist = []
        # instantiate a new list to replace the last one
        for _ in range(4):
            # every 4 reserves from 1006
            newlist.append(start)
            start += 12
            # a reserve (box) occurs every 12 CL
        if (start - 1054) % 480 == 0:
            # 1054 is very first CL of the second "pack" in case 1. [It makes the math work.]
            casecount += 1
            print(f'cracking open case {casecount}:')
        print(newlist)

"""
Results: [1006, 1018, 1030, 1042] ... [2590, 2602, 2614, 2626]
We can see from this that my CL2590 is 1 "box" into the 4th "pack" of "case" 4 overall.
"""
