
# these sets are lists now (on replit) to make random.choice work (replit doesn't have Fortuna)
# not really a need at this time to keep them as sets in PyCharm either...

dr_CL = 3885

s3_set = [
    'Absorbing Man', 'Adam Warlock', 'Aero', 'Agatha Harkness', 'Arnim Zola', 'Baron Mordo', 'Beast', 'Black Bolt',
    'Black Cat', 'Black Widow', 'Brood', 'Captain Marvel', 'Cerebro', 'Colleen Wing', 'Crossbones', 'Crystal', 'Dagger',
    'Daredevil', 'Deadpool', 'Death', 'Debrii', 'Destroyer', 'Doctor Doom', 'Doctor Octopus', 'Dracula', 'Drax',
    'Electro', 'Falcon', 'Gambit', 'Ghost Rider', 'Giganto', 'Goose', 'Green Goblin', 'Hazmat', 'Hela', 'Hell Cow',
    'Human Torch', 'Invisible Woman', 'Jane Foster', 'Juggernaut', 'Kingpin', 'Leader', 'Lockjaw', 'Luke Cage', 'Magik',
    'Magneto', 'Maximus', 'Miles Morales', 'Mister Negative', 'Mojo', 'Moon Knight', 'Mysterio', 'Mystique',
    'Nick Fury', 'Omega Red', 'Patriot', 'Polaris', 'Psylocke', 'Quake', 'Quinjet', 'Red Skull', 'Rescue', 'Rockslide',
    'Rogue', 'Ronan the Accuser', 'Sera', 'She-Hulk', 'Spider-Man', 'Taskmaster', 'The Hood', 'Thor', 'Titania',
    'Typhoid Mary', 'Ultron', 'Venom', 'Viper', 'Wasp', 'Wave', 'Wong', 'Yellowjacket', 'Zero']

s4_set = [
    'AGENT COULSON', 'ATTUMA', 'BAST', 'BLACK PANTHER', 'HELICARRIER', 'M\'BAKU', 'MARIA HILL', 'ORKA', 'SHURI',
    'SUPER SKRULL', 'VALKYRIE']

s5_set = [
    'DARKHAWK', 'DAZZLER', 'GALACTUS', 'KNULL', 'SAURON', 'SENTRY', 'SHANNA', 'SILVER SURFER', 'THANOS']

token_buys = ["Miles Morales", "Cerebro", "Jane Foster", "Mister Negative", "Wave", "Psylocke", "Daredevil", "Rogue", "SHURI"]


# this is the order I got the s3 cards

dr_dict = {
    486: "Dracula",
    498: "Deadpool",
    506: "The Hood",
    530: "Death",
    538: "Electro",
    546: "Nick Fury",
    570: "Magik",
    586: "Wong",
    610: "Crystal",
    626: "Green Goblin",
    650: "Dagger",
    658: "Venom",
    666: "Lockjaw",
    674: "Doctor Doom",
    698: "Taskmaster",
    714: "Invisible Woman",
    738: "Doctor Octopus",
    754: "Brood",
    766: "Black Cat",
    802: "Black Bolt",
    814: "Agatha Harkness",
    826: "Hell Cow",
    862: "Human Torch",
    898: "Red Skull",
    910: "Quake",
    934: "Wasp",
    958: "Goose",
    982: "Arnim Zola",
    1030: "Destroyer",
    1078: "Spider-Man",
    1102: "Kingpin",
    1186: "Mojo",
    1210: "MARIA HILL",
    1246: "Zero",
    1318: "Giganto",
    1378: "Omega Red",
    1414: "Rescue",
    1450: "Mysterio",
    1498: "Juggernaut",
    1534: "Quinjet",
    1582: "Debrii",
    1654: "Baron Mordo",
    1714: "Hela",
    1738: "Gambit",
    1786: "Mystique",
    1834: "Rockslide",
    1906: "Aero",
    1930: "AGENT COULSON",
    1966: "Colleen Wing",
    2026: "TITANIA",
    2086: "Beast",
    2146: "Magneto",
    2182: "Polaris",
    2242: "Hazmat",
    2290: "Black Widow",
    2314: "Adam Warlock",
    2374: "Yellowjacket",
    2434: "Thor",
    2446: "Ronan the Accuser",
    2530: "Moon Knight",
    2542: "Ghost Rider",
    2614: "Viper",
    2638: "Typhoid Mary",
    2698: "Ultron",
    2746: "Crossbones",
    2782: "Sera",
    2854: "ORKA",
    2878: "Leader",
    2926: "Drax",
    2986: "Maximus",
    3058: "Falcon",
    3082: "Captain Marvel",
    3130: "Luke Cage",
    3190: "Absorbing Man",
    3226: "Patriot",
    3262: "She-Hulk",
    3334: "400 tokens",
    3358: "ATTUMA",
    3418: "500 tokens",
    3466: "200 tokens",
    3538: "200 tokens",
    3586: "600 tokens",
    3598: "300 tokens?",
    3670: "400 tokens",
    3730: "M\'BAKU",
    3742: "300 tokens",
}

if __name__ == '__main__':
    start = 1006
    # the collection level (CL1006) where reserves begin
    CL = input("Enter your Collection Level:")
    if CL == "Dr":
        CL = 3226
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
                # every 4 reserves from 1006:
                if start in dr_dict.keys():
                    new_list.append(dr_dict[start])
                    # print to the list of Reserves the card opened there
                else:
                    new_list.append(start)
                    # OR add the no. representing the Reserve to the list
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
        # your CL minus the no. of the first reserve, with math to arrive at a 1-4
        print(f"DrStrangePhD's Collection is on box {box_count} of pack {pack_count} in case {case_count}")
        print("Bought with tokens: Miles Morales, Cerebro, Jane Foster... \n"
              "...Mister Negative, Wave, Psylocke, Daredevil, Rogue")
