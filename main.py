# just literally wanted to do the math on Marvel Snap's Collectors Reserves,
# to know which 'pack' of 4 reserves/boxes I'm currently in...

if __name__ == '__main__':
    start = 1006
    # the collection level (CL1006) where reserves begin
    while start < 2543:
        # my collection is currently CL 2542
        newlist = []
        # instantiate a new list to replace the last one
        for _ in range(4):
            # every 4 reserves from 1006
            newlist.append(start)
            start += 12
            # a reserve (box) occurs every 12 CL
        print(newlist)

"""
Results: [1006, 1018, 1030, 1042] ... [2446, 2458, 2470, 2482]
We can see from this that my CL2470 is 3 "boxes" into a "pack" of 4 Collector's Reserves (box).
To find out what "case" of 10 boxes you're on, on line 14 use "start += 480
(12 CL's per box (Reserve), 4 per "pack", 10 packs per case aka 12*4*10 = 480)
This code will still sort the results into lists of four, but that's not relevant for cases.
"""
