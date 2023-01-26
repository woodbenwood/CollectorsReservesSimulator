# just literally wanted to do the math on Marvel Snap's Collectors Reserves,
# to know which 'pack' of 4 reserves/boxes I'm currently in...

if __name__ == '__main__':
    start = 1006
    # the collection level (CL1006) where reserves begin
    casecount = 0
    # a case is 10 "packs" of 4 "boxes" each (a "box" is 12 CL's with 1 Reserve)
    while start < 2543:
        # my collection is currently CL 2542
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
Results: [1006, 1018, 1030, 1042] ... [2542, 2554, 2566, 2578]
We can see from this that my CL2542 is 1 "box" into a "pack" of 4 Collector's Reserves (box).
To find out what "case" of 10 boxes you're on, on line 17 use "start += 480"
(12 CL's per box (Reserve), 4 per "pack", 10 packs per case aka 12*4*10 = 480)
This code will still sort the results into lists of four, but that's not relevant for cases.
"""
