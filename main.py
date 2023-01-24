# just literally wanted to do the math on Marvel Snap's Collectors Reserves,
# to know which 'box' of 4 reserves I'm currently in...

if __name__ == '__main__':
    start = 1006
    # the collection level (CL1006) where reserves begin
    while start < 2411:
        # my collection is currently CL 2410
        newlist = []
        # instantiate a new list to replace the last one
        for _ in range(4):
            # every 4 reserves from 1006
            newlist.append(start)
            start += 12
        print(newlist)

"""
Results: [1006, 1018, 1030, 1042] ... [2398, 2410, 2422, 2434]
We can see from this that my CL2410 is 2 "packs" into a "box" of 4 Collector's Reserves.
"""
