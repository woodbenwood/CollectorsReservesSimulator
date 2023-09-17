dr_CL = 10000

s3_set = ['Absorbing Man', 'Adam Warlock', 'Aero', 'Agatha Harkness', 'Agent Coulson', 'Arnim Zola', 'Attuma',
          'Baron Mordo', 'Bast', 'Black Panther', 'Beast', 'Black Bolt', 'Black Cat', 'Black Widow', 'Brood',
          'Captain Marvel', 'Cerebro', 'Colleen Wing', 'Crossbones', 'Crystal', 'Dagger', 'Daredevil', 'Dazzler',
          'Deadpool', 'Death', 'Debrii', 'Destroyer', 'Doctor Doom', 'Doctor Octopus', 'Dracula', 'Drax', 'Electro',
          'Falcon', 'Gambit', 'Ghost', 'Ghost Rider', 'Giganto', 'Goose', 'Green Goblin', 'Hazmat', 'Hela',
          'Helicarrier', 'Hell Cow', 'Human Torch', 'Invisible Woman', 'Jane Foster', 'Juggernaut', 'Kingpin', 'Leader',
          'Lockjaw', 'Luke Cage', 'M\'Baku', 'Magik', 'Magneto', 'Maria Hill', 'Maximus', 'Miles Morales',
          'Mister Negative', 'Mojo', 'Moon Knight', 'Mysterio', 'Mystique', 'Nick Fury', 'Omega Red', 'Orka', 'Patriot',
          'Polaris', 'Psylocke', 'Quake', 'Quinjet', 'Red Skull', 'Rescue', 'Rockslide', 'Rogue', 'Ronan the Accuser',
          'Sauron', 'Sentry', 'Sera', 'Shadow King', 'Shanna', 'She-Hulk', 'Shuri', 'Silver Surfer', 'Spider-Man',
          'Super Skrull', 'Taskmaster', 'The Hood', 'Thor', 'Titania', 'Typhoid Mary', 'Ultron', 'Valkyrie', 'Venom',
          'Viper', 'Wasp', 'Wave', 'Wong', 'Yellowjacket', 'Zero']

s4_set = ['DARKHAWK', 'KNULL', 'LEGION', 'MASTER MOLD', 'MIRAGE', 'M.O.D.O.K.', 'NEGASONIC TEENAGE WARHEAD',
          'NIMROD', 'SNOWGUARD', 'SPIDER-HAM', 'SPIDER-MAN 2099', 'STATURE', 'STEGRON', 'ZABU']

s5_set = ['ALIOTH', 'DAKEN', 'ECHO', 'GALACTUS', 'GHOST-SPIDER', 'HIGH EVOLUTIONARY', 'HIT-MONKEY', 'HOWARD the DUCK',
          'IRON LAD', 'JEAN GREY', 'JEFF the BABY LAND SHARK', 'KANG', 'KITTY PRYDE', 'LADY DEATHSTRIKE',
          'THE LIVING TRIBUNAL', 'LOKI', 'NEBULA', 'SILK', 'THANOS', 'X-23']

token_buys = ["Miles Morales", "Cerebro", "Jane Foster", "Mister Negative", "Wave", "Psylocke", "Daredevil",
              "Rogue", "SHURI", "GALACTUS", "THANOS", "KANG", "VALKYRIE", "HIGH EVOLUTIONARY", "SPIDER-HAM",
              "JEFF the BABY LAND SHARK", "LEGION", "MIRAGE", "SPIDER-MAN 2099", "HOWARD the DUCK"]

seasonal_s3_claims = ['Super Skrull', 'Sentry', 'Shanna']

compensation_reward = ['KITTY PRYDE']

bundle_buys = ['SILVER SURFER', 'ZABU', 'M.O.D.O.K.', 'NIMROD', 'HIT-MONKEY', 'NEBULA', 'GHOST-SPIDER', 'PHOENIX FORCE',
               'DAKEN', 'LOKI']

# this is the order DrStrangePhD got the s3 cards

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
    3814: "500 tokens",
    3874: "600 tokens",
    3898: "200 tokens",
    3958: "300 tokens",
    3994: "600 tokens",
    4066: "SAURON",
    4102: "500 tokens",
    4126: "200 tokens",
    4210: "Helicarrier",
    4222: "500 tokens",
    4294: "600 tokens",
    4330: "KNULL",
    4366: "400 tokens",
    4438: "400 tokens",
    4486: "300 tokens",
    4522: "BAST",
    4594: "200 tokens",
    4618: "600 tokens",
    4666: "500 tokens",
    4738: "600 tokens",
    4786: "400 tokens",
    4798: "400 tokens",
    4846: "300 tokens",
    4918: "300 tokens",
    4942: "SHADOW KING",
    5026: "200 tokens",
    5074: "500 tokens",
    5086: "300 tokens",
    5206: "600 tokens",
    5230: "500 tokens",
    5254: "500 tokens",
    5266: "BLACK PANTHER",
    5314: "600 tokens",
    5326: "GHOST",
    5338: "200 tokens",
    5386: "400 tokens",
    5398: "DARKHAWK",
    5446: "400 tokens",
    5470: "200 tokens",
    5494: "400 tokens",
    5590: "600 tokens",
    5614: "300 tokens",
    5686: "600 tokens",
    5722: "400 tokens",
    5794: "300 tokens",
    5818: "STATURE",
    5830: "400 tokens",
    5854: "500 tokens",
    5914: "200 tokens",
    5962: "200 tokens",
    6022: "500 tokens",
    6070: "400 tokens",
    6106: "500 tokens",
    6130: "MASTER MOLD",
    6178: "600 tokens",
    6214: "200 tokens",
    6274: "400 tokens",
    6298: "200 tokens",
    6334: "300 tokens",
    6394: "500 tokens",
    6442: "600 tokens",
    6466: "Dazzler",
    6514: "300 tokens",
    6538: "NEGASONIC",
    6550: "600 tokens",
    6610: "300 tokens",
    6646: "500 tokens",
    6670: "400 tokens",
    6730: "400 tokens",
    7138: "SNOWGUARD",
    7390: "STEGRON",
    7462: "THE LIVING TRIBUNAL",
    7690: "JEAN GREY",
    7810: "ECHO",
    7930: "Baby Nebula",
    8050: "variant Kang",
    8170: "IRON LAD",
    8290: "LADY DEATHSTRIKE",
    8410: "1000 tokens",
    8530: "SILK",
    8650: "Chibi Nebula",
    8770: "X-23",
    8890: "SILVER SAMURAI",
}

# removed from dr_dict:
# 5158: "100 tokens???",
# 5170: "Steampunk Yellowjacket??",
# Not sure what happened during that promotion, but missing rewards from Packs 3 and 7 seemed to be replaced in Pack 9

if __name__ == '__main__':
    start = 1006
    # the collection level (CL1006) where reserves begin
    CL = input("Enter your Collection Level:")
    if CL == "Dr":
        CL = dr_CL
        box_count = 0
        pack_count = 1
        case_count = 0
        # start the counts at 0. A case is 10 "packs" of 4 "boxes" each
        # (a "box" is 12 CL's incl Boosters, Credits, and a Reserve)
        new_list = []
        # a redundancy to appease the PyCharm linter
        while start < CL + 1:
            # runs until it reaches your CL, then stops
            new_list = []
            # instantiate new list of boxes per loop
            pack_count += 1
            # keeps track of which pack we're counting
            for _ in range(4):
                # every 4 reserves from 1006:
                if start in dr_dict.keys() and start > 7689 and ((start - 7690) % 120 == 0):
                    # clumsy 3-conditional statement could be arrived at with much simpler logic todo: do that!
                    new_list.append(f"*{dr_dict[start]}*")
                    # add to the list the card/variant opened there, with *'s to demarcate Spotlight Caches (Reserves)
                    # [Spotlight Caches were introduced July 2023. Cache 7690 was the first Spotlight for Dr's acct]
                elif start in dr_dict.keys():
                    new_list.append(dr_dict[start])
                    # add to the list of Reserves the card opened there
                elif start > 7689 and ((start - 7690) % 120 == 0):
                    new_list.append(f"*{start}*")
                    # denotes future Spotlight Caches with bookending asterisks
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
                if case_count == 15:
                    print("* = Spotlight Caches (begin at Reserve 7690)")
                print("\n", f'     --------- Case {case_count} ---------   ')
            print(f"pack {pack_count}: ", new_list)
        box_count = ((CL - new_list[0]) // 12) + 1
        # your CL minus the no. of the first reserve, with math to arrive at a 1-4
        print(f"\nDrStrangePhD's Collection is on box {box_count} of pack {pack_count} in case {case_count}")
        print(f"\nBought with tokens: {token_buys} \n"
              f"Bought with bundles: {bundle_buys}")
#
# if __name__ == '__main__':
#     count = 0
#     for i in s5_set:
#         count += 1
#     print(count)
