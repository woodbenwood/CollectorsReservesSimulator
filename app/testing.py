from app.drs_dict import s3_set, dr_dict, token_buys

if __name__ == '__main__':
    count = 0
    for item in s3_set:
        if item in dr_dict.values() or item.upper() in dr_dict.values() or item in token_buys:
            count += 1
        else:
            print(item)

    print(count)